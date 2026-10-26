import re
import pandas as pd

df = pd.read_csv("data/ing_reviews_clean.csv")

THEMES = {
    "Crashes & bugs": ["crash", "crashing", "bug", "freez", "glitch", "not loading", "issues"],
    "Design & navigation": ["ux", "ui", "navigate", "navigation", "confusing", "can't find",
                            "cannot find", "hard to find", "layout", "cluttered", "messy"],
    "Login problems": ["login", "log in", "sign in", "logged out", "face id", "fingerprint",
                       "password", "access code", "verification"],
    "Transactions & balance": ["transaction", "balance", "statement", "pending", "history"],
    "Prefer old app": ["old app", "previous app", "backward", "bring back", "go back to",
                       "step back", "original app"],
    "Churn intent": ["switch bank", "switching bank", "change bank", "close my account",
                     "closing my account", "leave ing", "leaving ing", "move to another bank",
                     "find another bank", "moving my money"],
    "Access blocked (VPN)": ["vpn"],
}   # ← THEMES ends here

FEATURES = {
    "No running balance": ["running balance", "running total"],
    "Balance preview removed": ["without logging in", "before logging in", "preview", "quick balance"],
    "Switching accounts": ["switch between accounts", "switch accounts", "between accounts"],
    "Paying new payees": ["new payee", "pay someone new", "address book", "add a payee"],
    "Forced migration": ["forced", "force us", "forcing"],
}   
ALL_TAGS = {**THEMES, **FEATURES}    # merge both dictionaries into one

for name, words in ALL_TAGS.items():
    pattern = "|".join(r"\b" + re.escape(w) for w in words)
    df[name] = df["text_lower"].str.contains(pattern, regex=True)

print("=== Themes (% of reviews) ===")
themes_summary = df.groupby("app")[list(THEMES)].mean().T.round(3) * 100
print(themes_summary.sort_values(themes_summary.columns[0], ascending=False))

print("\n=== Specific features (% of reviews) ===")
features_summary = df.groupby("app")[list(FEATURES)].mean().T.round(3) * 100
print(features_summary.sort_values(features_summary.columns[0], ascending=False))

df.to_csv("data/ing_reviews_tagged.csv", index=False)
churn = df[df["Churn intent"] == True]
