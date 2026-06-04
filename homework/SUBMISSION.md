# Submission

## Repository
https://github.com/fidaash/rag-tutorial

## Dataset
Food.com Recipes — 2000 recipes, 5951 chunks after splitting.

## How to run
```bash
uv sync
uv run python scripts/ingest.py
uv run python scripts/build_index.py
uv run streamlit run app/main.py
```

## Demo questions and answers

**Q1: how to make chicken soup?**
Found: "7 can soup", "chicken noodle soup" — recipes with chicken broth and vegetables.

**Q2: how to bake chocolate cake?**
Found: "100 chocolate cake", "3 ingredient triple fudge cake" — recipes with cocoa powder and flour.

**Q3: what ingredients do I need for pasta?**
Found: "20 minute pasta bake", "3 cans and a box chili pasta" — recipes with pasta, sauce, cheese.

## Negative question

**Q: Какие переменные в датасете про безработицу?**
Answer: "В базе не найдено релевантных фрагментов. Ответить по данным невозможно."
— Correctly refused because the database contains only recipes, not economic data.

## Tests
11 tests passing green.
