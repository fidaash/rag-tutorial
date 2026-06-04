# Data Description

## Source
Food.com Recipes dataset from Kaggle.
URL: https://www.kaggle.com/datasets/shuyangli94/food-com-recipes-and-user-interactions

## What is indexed
- 2000 recipes from RAW_recipes.csv
- Each recipe contains: name, ingredients, steps, description, cooking time
- Total chunks after splitting: 5951

## Fields used
- name: recipe title
- ingredients: list of ingredients
- steps: cooking instructions
- description: short description
- minutes: cooking time in minutes

## Why this dataset
Recipes are a great use case for RAG — users can ask natural questions
like "how to make chocolate cake?" and get relevant recipes with ingredients
and steps as sources.
