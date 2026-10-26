import pandas as pd

df = pd.read_csv("data/ing_reviews_tagged.csv")

THEME = "PIN change"    # change this to check each theme

tagged = df[df[THEME] == True]
sample = tagged.sample(10, random_state=1)   # 10 random reviews; random_state makes it repeatable

for text in sample["text"]:
    print("-", text[:300])                    # first 300 characters
    print()