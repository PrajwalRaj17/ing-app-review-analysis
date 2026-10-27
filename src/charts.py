import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ing_reviews_tagged.csv")
df["date"] = pd.to_datetime(df["date"], utc=True)

# Short labels for charts (full names go in the caption or report)
df["app_short"] = df["app"].replace({
    "Do your thing - ING Banking": "New app",
    "ING Australia Banking": "Original app",
})

# ---------- Chart 1: 2026 rating gap ----------
recent = df[df["date"].dt.year == 2026]

# Rows = store, columns = app, values = average rating
gap = recent.groupby(["store", "app_short"])["rating"].mean().unstack()
recent["store"] = recent["store"].replace({"applestore": "App Store", "app_store": "App Store",
                                              "google_play": "Google Play"})
print(gap.round(2))

ax = gap.plot(kind="bar", figsize=(7, 4), color=["#d9534f", "#5b8def"])
ax.set_title("Average rating in 2026: new app vs original")
ax.set_ylabel("Average stars (1–5)")
ax.legend(title="")
ax.set_xlabel("")
ax.set_ylim(0, 5)                 # star ratings go up to 5
ax.tick_params(axis="x", rotation=0) # keep store names horizontal


# Show the number on top of each bar
for container in ax.containers:
    ax.bar_label(container, fmt="%.2f")

plt.tight_layout()
plt.figtext(0.5, -0.02, "Reviews in 2026: App Store 500 new / 287 original · Google Play 1,729 new / 292 original",
               ha="center", fontsize=8)
plt.savefig("outputs/chart1_rating_gap.png", dpi=150, bbox_inches="tight")
plt.close()
print("Saved chart 1")

# ---------- Chart 2: monthly trend (2025 onwards, 30+ reviews only) ----------
from_2025 = df[df["date"].dt.year >= 2025]
monthly = from_2025.groupby(["month", "app_short"])["rating"].agg(["mean", "count"])

# Keep only months with enough reviews to be reliable
monthly = monthly[monthly["count"] >= 30]

trend = monthly["mean"].unstack()   # rows = month, columns = app

ax = trend.plot(figsize=(9, 4), marker="o", color=["#d9534f", "#5b8def"])
ax.set_title("Monthly average rating (months with 30+ reviews)")
ax.set_ylabel("Average stars (1–5)")
ax.set_xlabel("")
ax.set_ylim(0, 5)
ax.legend(title="")
plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("outputs/chart2_monthly_trend.png", dpi=150)
plt.close()
print("Saved chart 2")

# ---------- Chart 3: themes ----------
themes = ["Prefer old app", "Transactions & balance", "Crashes & bugs",
          "Login problems", "Design & navigation", "Churn intent"]
# VPN left out: too few mentions (0.1%)

theme_pct = df.groupby("app_short")[themes].mean().T * 100
theme_pct = theme_pct.sort_values("New app")     # smallest at the bottom of the list, so the biggest shows at the top

ax = theme_pct.plot(kind="barh", figsize=(8, 5), color=["#d9534f", "#5b8def"])
ax.set_title("% of reviews mentioning each theme")
ax.set_xlabel("% of reviews")
ax.set_ylabel("")
ax.set_xlim(0, 50)
ax.legend(title="")

for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%", fontsize=8)

plt.tight_layout()

plt.savefig("outputs/chart3_themes.png", dpi=150)
plt.close()
print("Saved chart 3")

# ---------- Chart 4:  ----------
FEATURES = ["Account Name", "Forced migration", "Switching accounts",
          "No running balance", "Balance preview removed", "PIN change"]
# Paying new payees  left out: too few mentions (0.1%)

feature_pct = df.groupby("app_short")[FEATURES].mean().T * 100
feature_pct = feature_pct.sort_values("New app")     # smallest at the bottom of the list, so the biggest shows at the top
feature_pct = feature_pct.rename(index={"Account Name": "Account nicknames"})

ax = feature_pct.plot(kind="barh", figsize=(8, 5), color=["#d9534f", "#5b8def"])
ax.set_title("Specific feature complaints: % of reviews")
ax.set_xlabel("% of reviews")
ax.set_ylabel("")
ax.set_xlim(0, 12)
ax.legend(title="")

for container in ax.containers:
    ax.bar_label(container, fmt="%.1f%%", fontsize=8)

plt.tight_layout()

plt.savefig("outputs/chart4_themes.png", dpi=150)
plt.close()
print("Saved chart 4")