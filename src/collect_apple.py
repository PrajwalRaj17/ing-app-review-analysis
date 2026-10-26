import time
import requests
import pandas as pd

# ----- Settings -----
APP_ID = "6503263049"
APP_NAME = "Do your thing - ING Banking"
OUTPUT_FILE = "data/ing_reviews_apple_new.csv"

all_reviews = []
print("Collecting:", APP_ID, "->", OUTPUT_FILE)

for page in range(1, 11):                   # pages 1 to 10 (11 is not included)
    url = f"https://itunes.apple.com/au/rss/customerreviews/page={page}/id={APP_ID}/sortby=mostrecent/json"
    response = requests.get(url, timeout=20)

    if response.status_code != 200:         # stop if Apple says no
        break

    # .get() returns [] instead of crashing if there are no more reviews
    entries = response.json().get("feed", {}).get("entry", [])
    if len(entries) == 0:
        break

    for entry in entries:
        all_reviews.append({
            "review_id": entry["id"]["label"],
            "text": entry["title"]["label"] + ". " + entry["content"]["label"],
            "rating": int(entry["im:rating"]["label"]),
            "date": entry["updated"]["label"],
            "app_version": entry["im:version"]["label"],
        })

    print("Page", page, "- collected so far:", len(all_reviews))
    time.sleep(1)

df = pd.DataFrame(all_reviews)
df["app"] = APP_NAME
df["store"] = "applestore"                        # match the style of "google_play"

df.to_csv(OUTPUT_FILE, index=False)

# Quick checks
print(df.shape)
print(df["rating"].value_counts().sort_index())
print(df["date"].min(), "to", df["date"].max())