import pandas as pd
import json

df = pd.read_csv('data/raw/RAW_recipes.csv')
df = df.head(2000)

datasets = []
for i, row in df.iterrows():
    name = str(row['name'])
    ingredients = str(row['ingredients'])
    steps = str(row['steps'])
    description = str(row.get('description', ''))
    minutes = str(row['minutes'])

    text = f"Recipe: {name}\nIngredients: {ingredients}\nSteps: {steps}\nDescription: {description}\nCooking time: {minutes} minutes"

    datasets.append({
        "id": int(row['id']),
        "name": name,
        "text": text
    })

result = {"datasets": datasets}

with open('data/raw/datasets.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f'Done! Created {len(datasets)} recipes')
