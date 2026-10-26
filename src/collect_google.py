import time
import pandas as pd
from google_play_scraper import reviews, Sort

# ----- Settings: change these to collect a different app -----
APP_ID = "au.com.ingdirect.android"
APP_NAME = "ING Australia Banking"
OUTPUT_FILE = "data/ing_reviews_google.csv"

all_reviews = []      # empty list to collect everything
token = None          # no token yet for the first call
print("Collecting:", APP_ID, "->", OUTPUT_FILE)

while len(all_reviews) < 3000:          # target number of reviews
    result, token = reviews(
        APP_ID,                          # CHANGED: use the variable
        lang="en",
        country="au",
        sort=Sort.NEWEST,
        count=200,
        continuation_token=token
    )

    if len(result) == 0:                 # nothing came back, so stop
        break

    all_reviews.extend(result)
    print("Collected so far:", len(all_reviews))

    if token is None:                    # no more pages, so stop
        break

    time.sleep(1)

print("Total:", len(all_reviews))

# Turn the list of dictionaries into a table
df = pd.DataFrame(all_reviews)

# Keep only the columns we need
df = df[["reviewId", "content", "score", "at", "appVersion", "thumbsUpCount", "replyContent"]]

# Rename them to clearer names
df = df.rename(columns={
    "reviewId": "review_id",
    "content": "text",                   # CHANGED: "text" instead of "reviews"
    "score": "rating",
    "at": "date",
    "appVersion": "app_version",
    "thumbsUpCount": "likes",
    "replyContent": "ing_reply",
})

# True if ING replied to the review, False if not
df["ing_replied"] = df["ing_reply"].notna()

# Label where the data came from
df["app"] = APP_NAME                     
df["store"] = "google_play"

# Save to the data folder
df.to_csv(OUTPUT_FILE, index=False)      

# Quick checks
print(df.shape)
print(df["rating"].value_counts().sort_index())
print("ING replied to:", df["ing_replied"].sum(), "reviews")
print(df["date"].min(), "to", df["date"].max())
df["date"] = pd.to_datetime(df["date"])
print(df["date"].dt.year.value_counts().sort_index())