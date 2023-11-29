#!/usr/bin/env python3

import requests as rq
import os.path as os
import sys
import pandas as pan

anos = range(1917,2018)

#URL base do site
url_planilhas = "http://www.leb.esalq.usp.br/exceldados/{}{}.xls"

# Diretorio atual para salvar as planilhas
diretorio_de_download = os.dirname(sys.argv[0])

# Loop de 1917 a 2023 e definicao dos links de download
for ano in anos:
    if ano < 2000:
        url = url_planilhas.format("ROB", str(ano)[2:])
    else:
        url = url_planilhas.format("DCE", str(ano))

    #Faca a solicitacao para o servidor
    solicitacao_dos_dados = rq.get(url)

    #Verifique se a solicitacao foi bem-sucedida
    if solicitacao_dos_dados.status_code == 200:
        # Nomeie o arquivo de acordo com o ano e a extensao .xls
        nome = f"{diretorio_de_download}{ano}.xls"

        # Salve a planilha no diretorio especificado
        with open(nome, "wb") as file:
            file.write(solicitacao_dos_dados.content)
        print(f"Planilha do ano {ano} baixada com sucesso!")

    else:
        print(f"Nao foi possivel baixar a planilha do ano {ano}.")

print("Download de planilhas concluido.")

