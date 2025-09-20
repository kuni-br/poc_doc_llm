# Importa classe para maninpular datas
from datetime import datetime
# Importa classe para o download
from classe_download_do_csv import classe_download_do_csv
# Faz o download dos arquivos csv do diário oficial
# de agosto até dezembro de 2024
#for mm in range(8, 13):
# for dd in range(1, 32):
#     # chama o download do arquivo csv passando o ano (YYYY),
#     # o mês (mm) com zero à esquerda, e o dia (dd) com zero à esquerda
#     rc = classe_download_do_csv('2024','01',str(dd).zfill(2))
#     del rc
# Faz o download do csv do diário oficial de hoje
hoje = datetime.today()
classe_download_do_csv(str(hoje.year),str(hoje.month).zfill(2),str(hoje.day).zfill(2))
# Data sem conteúdo
#download_do_csv('2025','09','06')