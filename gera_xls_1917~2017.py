#!/usr/bin/env python3

import requests as rq
import os

# URL base do site
url_das_planilhas = "http://www.leb.esalq.usp.br/exceldados/{}{}{}.xls"

# Diretório onde você deseja salvar as planilhas
diretorio_de_download = os.getcwd() + "/"

# Loop de 1917 a 2023
for ano in range(1917, 2018):
    if ano < 2000:
        url = url_das_planilhas.format("ROB", str(ano)[2:], "")
    else:
        url = url_das_planilhas.format("DCE", str(ano), "")

    # Faça a solicitação para o servidor
    solicitacao_dos_dados = rq.get(url)

    # Verifique se a solicitação foi bem-sucedida
    if solicitacao_dos_dados.status_code == 200:
        # Nomeie o arquivo de acordo com o ano e a extensão .xls
        nome = f"{diretorio_de_download}{ano}.xls"

        # Salve a planilha no diretório especificado
        with open(nome, "wb") as file:
            file.write(solicitacao_dos_dados.content)
        print(f"Planilha do ano {ano} baixada com sucesso!")

    else:
        print(f"Não foi possível baixar a planilha do ano {ano}.")

print("Download de planilhas concluído.")

