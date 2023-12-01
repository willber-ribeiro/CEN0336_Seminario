#!/usr/bin/env python3

import pandas as pd

# Carregue a planilha
df = pd.read_excel('Precipi_Total.xlsx')

# Remova espaços extras nos nomes das colunas
df.columns = df.columns.str.strip()

# Solicite ao usuário o mês e ano desejados
ano_desejado = int(input('Digite o ano desejado (1917-2017): '))
mes_desejado = input('Digite o mês desejado (JAN-DEZ): ').upper().strip()

# Filtrar dados com base no ano e mês inseridos pelo usuário
dados_filtrados_mes = df[(df['ANO'] == ano_desejado) & (df['MES'].str.strip().str.upper() == mes_desejado)]
dados_filtrados_ano = df[(df['ANO'] == ano_desejado)]

#Calcular os valores de média mensal e anual
media_precipitacao_mes = dados_filtrados_mes['PRECIPI-'].mean()
precipitacao_max_mes = dados_filtrados_mes['PRECIPI-'].max()
#precipitacao_min_mes = dados_filtrados_mes['PRECIPI-'].min()

media_precipitacao_ano = dados_filtrados_ano['PRECIPI-'].mean()
precipitacao_max_ano = dados_filtrados_ano['PRECIPI-'].max()
#precipitacao_min_ano = dados_filtrados_ano['PRECIPI-'].min()

# Exibir resultados
print(f'A média mensal de precipitação para {mes_desejado}-{ano_desejado} é: {media_precipitacao_mes:.2f} mm')
print(f'A precipitação máxima ocorrida em {mes_desejado}-{ano_desejado} é: {precipitacao_max_mes:.2f} mm')
#print(f'A precipitação mínima ocorrida em {mes_desejado}-{ano_desejado} é: {precipitacao_min_mes:.2f} mm')

print(f'A média anual de precipitação para {ano_desejado} é: {media_precipitacao_ano:.2f} mm')
print(f'A precipitação máxima ocorrida em {ano_desejado} é: {precipitacao_max_ano:.2f} mm')
#print(f'A precipitação mínima ocorrida em {ano_desejado} é: {precipitacao_min_ano:.2f} mm')
    # De maneira geral, a precipitação mínima em um mês ou ano sempre vai ser zero, então não acho que seja necessário o script verificar isso. De qualquer forma eu deixei o código aqui, é só tirar o # que o script volta a incluir a precipitação mínima.