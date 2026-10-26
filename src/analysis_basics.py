import pandas as pd

df = pd.read_csv("data/ing_reviews_clean.csv")
df["date"] = pd.to_datetime(df["date"], utc=True)

# 1. Fair comparison: same period only (2026)
recent = df[df["date"].dt.year == 2026]
print("=== 2026 only: average rating by app and store ===")
print(recent.groupby(["app", "store"])["rating"].agg(["mean", "count"]).round(2))

# 2. Monthly trend for both apps, from 2025
from_2025 = df[df["date"].dt.year >= 2025]
print("\n=== Monthly average rating (2025 onwards) ===")
monthly = from_2025.groupby(["month", "app"])["rating"].mean().unstack().round(2)
monthly = from_2025.groupby(["month", "app"])["rating"].agg(["mean", "count"]).round(2)
print(monthly)

# 3. Which versions of the new app were worst?
new_app = df[df["app"] == "Do your thing - ING Banking"]
versions = new_app.groupby("app_version")["rating"].agg(["mean", "count"])
versions = versions[versions["count"] >= 20]     # ignore versions with very few reviews, try 20
print("\n=== New app: rating by version (20+ reviews) ===")
print(versions.sort_values("mean").round(2))