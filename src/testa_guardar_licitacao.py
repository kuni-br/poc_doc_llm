import requests
import io
import pandas as pd
from bs4 import BeautifulSoup
import re
import PyPDF2

def url_to_text(link):
    if link is None:
        return ''
    response = requests.get(link)
    content_type = response.headers.get('content-type')
    if 'text/html' in content_type:
        soup = BeautifulSoup(response.text, 'html.parser')
        texto_bruto = soup.get_text()
        return re.sub(r'\s+', ' ', texto_bruto).strip()
    elif 'application/pdf' in content_type:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(response.content))
        paginas = pdf_reader.pages
        paginas_texto = ''
        for pagina in range(len(paginas)):
            pagina_atual = paginas[pagina].extract_text()
            paginas_texto += pagina_atual
        return paginas_texto
    return ''

for dia in range(19,20):
    # Acessa site do diário oficial para pegar diário oficial de uma data
    data_referencia=f'{str(dia).zfill(2)}/09/2025'
    stream_arquivo_do_csv = requests.post(
        'https://diariooficial.prefeitura.sp.gov.br/md_epubli_controlador.php',
        headers={'Content-Type': 'application/x-www-form-urlencoded',},
        params={'acao': 'edicao_download',},
        data={
            'hdnDtaEdicao': f'{data_referencia}',
            'hdnTipoEdicao': 'C',
            'hdnBolEdicaoGerada': 'false',
            'hdnIdEdicao': '',
            'hdnInicio': '0',
            'hdnFormato': 'csv',
        },
    )
    if len(stream_arquivo_do_csv.content) != 0:
        # Carrega data frame pandas com arquivo csv lido do site do diário oficial
        arquivo_do_csv = io.StringIO(stream_arquivo_do_csv.text)
        df_diario_oficial = pd.read_csv(arquivo_do_csv, sep=';', encoding='utf-8-sig', quoting=1)
        # df_diario_oficial['Texto'] = ''
        # df_diario_oficial['Links_Externos'] = ''
        # Filtrar coluna séries a partir da string 'Ata da Licita&ccedil;&atilde;o (NP)'
        ata_da_licitacao = 'Ata da Licita&ccedil;&atilde;o (NP)'
        documentos_para_importar = df_diario_oficial[df_diario_oficial['Série']==f'{ata_da_licitacao}'].copy()
        documentos_para_importar['Data_Publicacao'] = data_referencia
        documentos_para_importar['Texto'] = ''
        #documentos_para_importar['Qtd_Links_Externos'] = 0
        documentos_para_importar['Links_Externos'] = ''
        documentos_para_importar['Texto_Links_Externos'] = ''
        # Acessa o link com o texto do diário oficial extrai somente o texto 
        # a partir do html com o BeautifulSoup e
        # trata o texto tirando os \n, \t, etc e substitui por espaço
        for i, row in documentos_para_importar.iterrows():
            #print(i)
            html_documentos_para_importar = requests.get(documentos_para_importar.at[i,'Link']).text
            soup_documentos_para_importar = BeautifulSoup(html_documentos_para_importar,'html.parser')
            documentos_para_importar.at[i,'Texto'] = re.sub(r'\s+', ' ',soup_documentos_para_importar.get_text()).strip()
            soup_a = soup_documentos_para_importar.find_all('a')
            links_externos = []
            textos_links_externos = []
            qtd_links = len(soup_a)
            if qtd_links > 1:
                for soup_link_externo in soup_a:
                    link_externo = soup_link_externo.get('href')
                    links_externos.append(link_externo)
                    textos_links_externos.append(ulr_to_text(link_externo))
                    print(i,link_externo)    
                documentos_para_importar.at[i,'Links_Externos'] = links_externos
                documentos_para_importar.at[i,'Texto_Links_Externos'] = textos_links_externos
            if qtd_links == 1:
                link_externo = soup_a[0].get('href')
                documentos_para_importar.at[i,'Links_Externos'] = link_externo
                #print(i,link_externo)
                documentos_para_importar.at[i,'Texto_Links_Externos'] = url_to_text(link_externo)
            #documentos_para_importar['Qtd_Links_Externos'] = qtd_links
        #documentos_para_importar[['Texto','Link']]
        #documentos_para_importar.to_csv(f'teste_documentos_para_importar/teste_documentos _para_importar{data_referencia.replace("/","")}.csv', sep=';' ,encoding='utf-8-sig', index=False, header=True)
        documentos_para_importar.to_parquet(f'teste_documentos_para_importar/teste_documentos _para_importar{data_referencia.replace("/","")}.parquet', engine='fastparquet')