import pandas as pd

df = pd.read_csv("data/ing_reviews_all.csv")
df["date"] = pd.to_datetime(df["date"], utc=True)   # CSV turns dates back into text
print("Start:", len(df))

# 1. Make sure text is text, and remove extra spaces at the ends
df["text"] = df["text"].astype(str).str.strip()

# 2. Remove duplicate reviews (same review ID in the same store)
df = df.drop_duplicates(subset=["review_id", "store"])
print("After removing duplicates:", len(df))

# 3. Remove very short reviews like "good" or "ok"
df = df[df["text"].str.len() >= 15]           # try 15 characters
print("After removing short reviews:", len(df))

# 4. Sentiment from stars
def get_sentiment(rating):
    if rating <= 2:
        return "Negative"
    elif rating == 3:
        return "Neutral"
    else:
        return "Positive"

df["sentiment"] = df["rating"].apply(get_sentiment)

# 5. Month column for trend charts (e.g. "2026-03")
df["month"] = df["date"].dt.strftime("%Y-%m")

# 6. Lowercase copy of the text, for keyword searching
df["text_lower"] = df["text"].str.lower()

# Check
print(df["sentiment"].value_counts())
print(df.groupby("app")["sentiment"].value_counts(normalize=True).round(2))

df.to_csv("data/ing_reviews_clean.csv", index=False)