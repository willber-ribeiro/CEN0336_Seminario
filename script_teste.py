#!/usr/bin/env python3

import pandas as pd

df_1917 = pd.read_excel('1917.xls')
df_1917.columns = df_1917.iloc[0]
print(df_1917.loc[pd.to_numeric(df_1917['No'], errors = 'coerce').notnull(),['No','ANO     ','DIA     ','MES     ','PRECIPI-']])
