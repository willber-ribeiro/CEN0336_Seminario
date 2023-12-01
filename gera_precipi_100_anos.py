#!/usr/bin/env python3

import pandas as pd

anos = range(1917,2018)

vazio = {}
v = pd.DataFrame(vazio)

print('Processando Dataframes...')

for ano in anos:
    df = pd.read_excel(f'{ano}.xls')
    df.columns = df.iloc[0]
    df = df.loc[pd.to_numeric(df['No'], errors = 'coerce').notnull(),['No','ANO     ','DIA     ','MES     ','PRECIPI-']]
    v = v._append(df)
v.to_excel('Precipi_Total.xlsx')

print('Concluído.')
