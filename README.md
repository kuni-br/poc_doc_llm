# Prova de conceito para ler o Diário Oficial da Cidade de São Paulo e extrair dados das atas de abertura das licitações por meio de API de uma LLM
## Descrição
Esta prova de conceito faz a ingestão de dados a partir do site do Diário Oficial da Cidade de São Paulo e seleciona as atas de abertura das licitações para extrair dados relacionados à licitação por meio de API de uma LLM
## Estrutura do projeto
## Clone do repositório
## Acesso o diretório
## Crie e ative o ambiente virual
```env
python -m venv venv
Linux: source ./venv/bin/activate
Windows: ./venv/scripts/activate
```
## Para gerar as dependências
```env
pip install pipreqs
pipreqs . --force
```
## Instale as dependências
```env
pip install -r requirements.txt
```
## Variáveis de ambiente (.env)
Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:
```env

```
## curl para baixar o csv do diário oficial
```bash
curl -o <YYYYMMDD>C.csv -d 'hdkDtaEdicao=DD/MM/YYYY' -d 'hdnTipoEdicao=C' -d 'hdnBolEdicaoGerada=false' -d 'hdnIdEdicao=' -d 'hdnInicio=0' -d 'hdnFormato=csv' https://diariooficial.prefeitura.sp.gov.br/md_epubli_controlador.php?edicao_download
```
## Ferramenta para converter o curl para chamadas em outras linguagens
[Conversão de curl online](https://curlconverter.com/)
