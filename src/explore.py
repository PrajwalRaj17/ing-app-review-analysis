import pandas as pd

# Read the saved reviews (no downloading)
df = pd.read_csv("data/ing_reviews_google.csv")

# Dates load from CSV as plain text, so convert them back to dates
df["date"] = pd.to_datetime(df["date"])

# Reviews per year
df["year"] = df["date"].dt.year
print(df["year"].value_counts().sort_index())

# Average rating per year
print(df.groupby("year")["rating"].mean().round(2))