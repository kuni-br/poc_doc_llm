import requests
from bs4 import BeautifulSoup
import re

urls = [
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?IIfGp_B9XNN9FgiCDTdCIh5oI7K2SO2LwoobhrzEmZKtRYWAXinecmVJpA1_zKCbK_sLNWdaSmf9GOUqo3KUh7b4AplQ-KiXm5daezD2RlhOIoopyn8Bl7cciWK7V1pT',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?mCEFuDG5e_lwO-ZALOr4tNdjn9lRPC8QirDpCql1f-k8YhMHxl1jADAu5xx82P7bG3etZ5zILLOUn5bZx8xria_Q5-XXFsi2D9CmhdAVo57ZxDSUN6tDepcLNNAwLjvO',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?6jGTiPSScALH-PmU6IITU_zylbdNoboftORaQEeL3VfLq9RHDSv0yXwsZu0Jl7nkK1wyqTVdJqWWGmUzsgST-eEmAKWQlScJo6Lm8pwiOXj6FGUd9gDcLoNOdLLaVh4x',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?9NgPATylGvlK0GZnTFifTYCc0j2sWJ2vq7dnj2_DnwlJV-nAv1F3xdy2aX8aq3dC_XOxR9G7EdOHM2EmOed04iGgunaR4xqvM2Jo95k6ykw-fC9F5Z-Lw4XCPo-jGH5_',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?7JEej4upd9Ad6tYzFF_hdXtShz3dYfRgyQXkCPVUiS-nj9J5RyIuGWbMSciSzks28HpIigVNJaS1A37MIl5OYGhTcdU5Bw-yVcG1OHDgy_kGR0yL24Bt3OCcKpBpyNTW',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?tCDXwN2rdA4_Pnf77syfngR-KbyEuYNEnY1uBw0SsDkJNviXhwyRpcIeD41B1Gc70JcMdAn8wMcVxdlhq-F4u-5NUwB83FTHO7a_oWCPxGv3kgx025zzGj3GzG9SOpEk',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?barwOqxTuxh-P16leKcOoAqJkmRzrfQ-5ic9blthxPMdNmgx5biSKNKqcNOsqTojwCz1U0pyDnkFpBrn9b_Y9aqVyNTC5B7pIdYsqwUPWUFzDY7wuatPeIxJb7Qfmwk9',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?Z-VHaiD0ucbt0lOqHF2WEEpGqKeVnkZL0JpKPU42vk9-04yqlOljkJwdLYyQCJREA9WFaGGZB3IoWH3O-PkS7FzSebvMKA5Af99VJ_7S4ZqdsnB5GOTN6qV_ZnV37jPS',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?kgRGDS_gJtj-S5rCEI423Xy7l3-NtaU2G-RAYa3ulWiZaWc5CTRnGG1Y3j-I9DTsA-oOAqTVKyP7dY_6zzsSesCLDFOY62mE_kup9so3BRZYJkxkdJ2cWJYlNGlCxsQu',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?2tjwvTSvxBvnqWvP7ORtxZp2lO_aC3L05u27Sd7WNCFtbOU6rsCE_5AmYlj8yxKUShQallTqGFJf_AnJp0wpBguE9O8yxnRS6M5kqDbt4RdzvcN-k0RxU3a3hG-V6dnA',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?6EocmOVfJYn1YG6ueHLxPWQOiqALs7E4EYPbqap8lwhAl2PkgRixxny2jg8naSqPP-nHLDt2IQOhO_VZil9w3Uuaf9SSVbXQ6BDEWkuAAxRf-3sxGqdSRsUBFHGMPr2_',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?fL1wBb_j51igRsOANNwyVjvKIPE8v97dRmIcVt7BXUNfS8bzPjESrIgZi1p5CYAmyEK9AC8p8zklkJNV2V68ka-1g_6X4AJMeRbCQ1PsVRJhOt-2fuzFDimsqxjS7F4l',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?fLgUuzIHjRpNonL9a8kHy8uF1GW3KSWc3egwIanH4Qb3Cha7yJEQDfzPDMcwrA4HZb1NbhA04Z2NQCnknNWctKwHwjIu-NTHtljinzHpmiNb8LzD-oTdbrl5bZ1-Szlu',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?XcciJA-xGbxto_0841TiK33zdJVEjjp_ZqkC4dh4VxRiHaMT82APE_4klFBxq3ND9SK7eaBz1Bx--VpbtOz3j92Ca5JyjZFD9I14fATrDF6d1xogXm94Ga7kkA7PwykX',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?kOpTMDaUqUYwJBoggx5e890QJuCh-efB52LBC_WTPJaOQM0_-tUbD8gbkpS4cyLHWEFPL0B2SdKNrjU5M_62Qu61lmyxJ18ehtC3rzrBMFCT24_7GXOmQFMLzdo00X2k',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?85vnF4Bm-ZOAXaHDqkni5BkUj45dBktYhJwp3i08vWdVh25XXDqW9-2H4ym7g6SsrZ6d7NI_ihIfsjKi5oRdcnfeHsKS6wcoEQuEolHC2pG0VsdlA-tsVrImVlWdKDqO',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?5Q6hAQlREBLw40PSMbBgamB63dKJoX2GTeLjnyvabn9rwiWvjTxhvIshPCC_Se2GBQ2dXqbIs0eb1N2vvN3LOI3vME0_UAbir2yTIWEugOgITqcnxsF2SBEh6KY1E3Xu',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?YzfiJy8yfVPzAE3_cFIM8xQzEv1XE9Y78Busv2E1gaZXXYfZdLF1XJbgC0LeOr-Cx222pNubUei-Bm9B2_jwUcMObnA-MsDv_54hKENyzUrzSRW6ED7O_2QgcqcdtNRc',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?8YCOUjK1w_FVTrR6EUFJYJurA4YIaKRPCdQfuBuXSvQMeN2cq7pIesFAA29XZVovnJLOoG1hJ41VA2qJWZ82EsZcs4RNHoU_4aH0CyVXtaHYOB6V548MGVxIAL25D-LZ',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?5Q0c40Srf3hLtxKLiR0cp3amz5IVPuzgEK6Z4UIvtS1IjH1vY8sPvbTzFZIUCpym_y-hAx-b8kQCuQRkAAk8kQxc3_xWnU62REX3HMkgiAWJUOt5-8huoo6GCqqBTvTm',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?HBZN_YbnrWXBwMnqktYRplrbstRDLrYfsCRmRC7KXQsdRbRVLhncwMymGOjlDFEYmL_JawCeShFccLarA5ftDEcTPXQqzMxtzy2fRKeHCaESqxZUq4_YQLvGcOBmGKqO',
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?0wb125xanQ5C-M4JxxPsJtDbGpnLWJveJUcTh3gWZJbEKjHsWoxwiJYNogzzNE4pOZgKMENrL_hiDwYNfj3GIu78kfhf2a9ZFQS4lpz4wcKvnmSj2qZ9SF0588C4-0wI'
]
# Ata de licitação com vários lotes com anexo em pdf
urls= [
    'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?5Q0c40Srf3hLtxKLiR0cp3amz5IVPuzgEK6Z4UIvtS1IjH1vY8sPvbTzFZIUCpym_y-hAx-b8kQCuQRkAAk8kQxc3_xWnU62REX3HMkgiAWJUOt5-8huoo6GCqqBTvTm'
]
# Arquivo pdf
# urls = [
#     'http://diariooficial.prefeitura.sp.gov.br/md_epubli_visualizar.php?GBSgp-84nv1hCPfDBhFdnH-oz272g0AdlRJt47XaSGGqy46FXZB-7aY0R_vxf1bm7vF2tm-gj8UT8sB09nsu7HwANC_rErQ6FE08KryGM_df2Zt794yGLvP9T6vDPF0k'
# ]
# Recebe as página HTML
for url in urls:
    response = requests.get(url)
    # Analisa o código html
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extrai o texto da página html
    texto_bruto = soup.get_text()
    # Exclui quebras de páginas, tabulações, etc. e substitui por espaço
    text = re.sub(r'\s+', ' ', texto_bruto).strip()
    #text = re.sub(r'\s+', ' ', BeautifulSoup(requests.get(url).text, 'html.parser').get_text()).strip()
    # Print the plain text
    print('\n\n\n')
    print(text)
    # Extrai os links existentes na página
    for link in soup.find_all('a'):
        print(link.get('href'))