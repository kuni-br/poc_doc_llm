import requests
import io
import PyPDF2
# Carrega arquivo pdf da internet
#arquivo_pdf = requests.get('http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?UopFTElpAg8gNAU7xbvEAqOKPSGX6kZjObTn9WLo4ZoJOE-EkFumBNPCJGKu-iShH55L6mQ5OQhH2ScidxekJm_5TD2kySJGL1PcbQpKxduOdyX4KtAF6Q72pm7RVR0l')
arquivo_pdf = requests.get('http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?KUCmajueA9Zdc-s4zZeSxRPK-IJv88hwyaiVk7w4l-5ZZZcYbompmULzeqjZhlDjju_teYcMa8O-xOW4Y2mM96W4gLWFW1Kb5bjC2ce2jot4lwp4l-JHwOwMWEhinJhD')
# Le arquivo no formato pdf
pdf_reader = PyPDF2.PdfReader(io.BytesIO(arquivo_pdf.content))
#print('Número de páginas', len(pdf_reader.pages))
paginas = pdf_reader.pages
paginas_texto = ''
for pagina in range(len(paginas)):
    pagina_atual = paginas[pagina].extract_text()
    paginas_texto += pagina_atual
print(paginas_texto)