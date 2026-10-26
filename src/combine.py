import pandas as pd

files = [
    "data/ing_reviews_google.csv",
    "data/ing_reviews_google_new.csv",
    "data/ing_reviews_apple.csv",
    "data/ing_reviews_apple_new.csv",
]

frames = []
for file in files:
    df = pd.read_csv(file)
    # Convert dates in each file separately, then make them all UTC
    df["date"] = pd.to_datetime(df["date"], utc=True)
    frames.append(df)
    print(file, "->", len(df), "reviews")

# Stack all four tables on top of each other
combined = pd.concat(frames, ignore_index=True)

print("\nTotal:", len(combined))
print(combined.columns.tolist())
print(combined.groupby(["app", "store"]).size())

combined.to_csv("data/ing_reviews_all.csv", index=False)