# Biblioteca usada para fazer as chamadas no site do diário oficial
import requests 
# Biblioteca usada para fazer a consistência de datas
from datetime import datetime 
# Classe para fazer o logging
from classe_logger import classe_logger
# Faz o download do arquivo csv da data passada pelo parâmetro
# a partir do site do diário oficial
class classe_download_do_csv():
    # Configura logging
    def __init__ (
        self,
        # ano no formato yyyy
        yyyy,
        # mes no formato mm
        mm,
        # dia no formato dd
        dd,
        logger_name = 'download_do_csv_logger',
        logger_file_name = 'download_do_csv_logger'
        ):
        self.__yyyy = yyyy
        self.__mm = mm
        self.__dd = dd
        # Valida parâmetro logger_name
        if len(str(logger_name)) > 0:
            self.__logger_name = logger_name
        else:
            self.__logger_name = 'download_do_csv_logger'
        # Valida parâmetro logger_file_name
        if len(str(logger_file_name)) > 0:
            self.__logger_file_name = logger_file_name
        else:
            self.__logger_file_name = 'download_do_csv_logger'
        # Valida data no formato dd/mm/YYYY
        def is_valid_date(date_string):
            try:
                datetime.strptime(date_string, "%d/%m/%Y")
                return True
            except ValueError:
                return False
        # Define string com a data no formato dd/mm/yyyy
        dataEdicao = f'{self.__dd}/{self.__mm}/{self.__yyyy}'
        # Se a data for válida faz a requisição do arquivo csv no site do diário oficial
        if is_valid_date(dataEdicao):
            # Cria um logger com a data
            self.__logger_name = (f'{self.__logger_name}{self.__yyyy}{self.__mm}{self.__dd}')
            logger = classe_logger(
                self.__logger_name,
                classe_logger.DEBUG,
                self.__logger_file_name
            )
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded',
            }
            params = {
                'acao': 'edicao_download',
            }
            data = {
                'hdnDtaEdicao': dataEdicao,
                'hdnTipoEdicao': 'C',
                'hdnBolEdicaoGerada': 'false',
                'hdnIdEdicao': '',
                'hdnInicio': '0',
                'hdnFormato': 'csv',
            }
            response = requests.post(
                'https://diariooficial.prefeitura.sp.gov.br/md_epubli_controlador.php',
                headers=headers,
                params=params,
                data=data,
            )
            # Se a resposta tiver algum conteúdo grava o arquivo csv
            if(len(response.content)!=0):
                try:
                    logger.info(f'Grava arquivo csv ./do_csv/{yyyy}{mm}{dd}C.csv do dia {dataEdicao}')
                    with open(f'./do_csv/{yyyy}{mm}{dd}C.csv', 'wb') as f:
                        f.write(response.content)
                except Exception as e:
                    logger.error(f'Erro na gravação do arquivo csv ./do_csv/{yyyy}{mm}{dd}C.csv do dia {dataEdicao}: {e}')
            else:
                logger.warning(f'Data sem conteúdo {dataEdicao} arquivo ./do_csv/{yyyy}{mm}{dd}C.csv não gravado')
        else:
            # Erro! Data inválida, cria uma entrada no logger sem a data
            logger = classe_logger(
                'erro_data_invalida',
                classe_logger.DEBUG,
                self.__logger_file_name
            )
            logger.error(f'Data inválida: {dataEdicao}')