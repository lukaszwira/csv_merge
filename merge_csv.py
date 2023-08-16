import pandas as pd

df1 = pd.read_csv('plik1.csv')

df2 = pd.read_csv('plik2.csv')

df = df1.merge(df2, how='outer')
df_no_duplicates = df.drop_duplicates()
df_no_duplicates.to_csv('plik_merge.csv')
