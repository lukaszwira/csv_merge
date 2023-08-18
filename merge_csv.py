import pandas as pd

content_a = pd.read_csv('Translation.csv')
content_b = pd.read_csv('plik1.csv')

df = pd.concat([content_a, content_b])
df = df.applymap(lambda x: x.replace('"', '') if isinstance(x, str) else x)

df.drop_duplicates(subset=['language','source_text'], inplace=True)

df.to_csv('plik_merge.csv', index=False)
