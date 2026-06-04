import pandas as pd
import json

df = pd.read_csv('data/raw/RAW_recipes.csv')
print('Колонки:', df.columns.tolist())
print('Строк:', len(df))
print(df.head(2))