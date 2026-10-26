import pandas as pd

df = pd.read_csv("data/ing_reviews_all.csv")

# Keep only the new app's Apple reviews
apple_new = df[(df["app"] == "Do your thing - ING Banking") & (df["store"] == "applestore")]

# Keep the same columns the Apple script creates
apple_new = apple_new[["review_id", "text", "rating", "date", "app_version", "app", "store"]]

print("Recovered:", len(apple_new), "reviews")
apple_new.to_csv("data/ing_reviews_apple_new.csv", index=False)