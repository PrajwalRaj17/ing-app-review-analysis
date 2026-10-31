import pandas as pd

df = pd.read_csv("data/ing_reviews_tagged.csv")

# Readable names for the dashboard
df["app_short"] = df["app"].replace({
    "Do your thing - ING Banking": "New app",
    "ING Australia Banking": "Original app",
})
df["store"] = df["store"].replace({
    "applestore": "App Store", "app_store": "App Store", "google_play": "Google Play",
})

# Turn True/False into 1/0, so the AVERAGE in Tableau = % of reviews
tag_columns = ["Prefer old app", "Transactions & balance", "Crashes & bugs",
               "Login problems", "Design & navigation", "Churn intent",
               "Account Name", "Forced migration", "Switching accounts",
               "No running balance", "Balance preview removed", "PIN change"]   # your PIN column name
df[tag_columns] = df[tag_columns].astype(int)

df["date"] = pd.to_datetime(df["date"], utc=True).dt.strftime("%Y-%m-%d")

# Keep only what the dashboard needs
keep = ["review_id", "text", "rating", "date", "month", "app_short", "store",
        "sentiment", "app_version"] + tag_columns
df[keep].to_csv("outputs/dashboard_data.csv", index=False)
print("Saved", len(df), "rows for the dashboard")