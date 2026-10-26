## Finding 2: New app is rated far lower (Google Play)
- New app: 1,815 reviews (Nov 2025 – Oct 2026), avg ~1.5 stars, 70% are 1-star
- Original app in 2026: 316 reviews, avg 2.38
- ING replied to ~9% of new app reviews vs ~17% for original
- Caveat: migration likely drives negative reviews
## Finding 3: Same pattern on the App Store
- New app: avg ~1.25, 87% 1-star (500 reviews, Jul–Oct 2026)
- Original app: avg ~2.0 (500 reviews, Feb 2025–Oct 2026)
- Confirms Google Play finding across both platforms
- Note: Apple dates are US Pacific time (-07:00); convert on Day 2
## Findig 4 : Themes from reading reviews
- Most people are not satifactory with the new app as they could not navigate through the desired options
- Most complain about login page and they cannot the display the transactions properly
- Some people are comfortable with the old app and also declared they will be switching differents banks 
- Very minor people were ok with the new version but still they would prefer the old one
## Finding 5 :
- From Feb 2026, review volume jumped (8 in Jan → 122 in Feb → 306 in Mar), suggesting a wide rollout. The new app’s rating then stayed flat at ~1.35–1.50 every month and did not improve.
- In 2026, the original app averaged 0.7–0.8 stars higher than the new app on both stores (App Store 1.94 vs 1.25; Google Play 2.26 vs 1.48).

## Day 2 findings

### Finding 4: Top themes in new app reviews
- Prefer old app: 43.7% (new) vs 3.7% (original)
- Transactions & balance: 27.6% vs 16.7%
- Design & navigation: 11.4% vs 4.6%
- Nearly half of new app reviews say the old app was better.
- Transaction and balance complaints are about 1.7× more common in the new app,
  mostly driven by the missing running balance.
- Navigation complaints are about 2.5× more common in the new app.

### Finding 5: Crashes are NOT the main problem
- Crashes & bugs: 8.4% (new) vs 10.3% (original)
- Crash complaints are slightly LESS common in the new app.
- So the new app's low rating isn't mainly about stability. Combined with
  "no version improved the rating" (Finding 3), this suggests the problem is
  design and missing features, not bugs. Fixing bugs alone is unlikely to
  raise the rating much.

### Finding 6: Login problems are long-standing, not caused by the new app
- Login problems: 11.8% (new) vs 11.3% (original)
- Almost identical in both apps, so login issues existed before the redesign.
- This is a separate, ongoing problem: about 1 in 9 reviews in either app
  mentions login. Worth fixing, but it doesn't explain why the new app is
 lower.

### Finding 7: Specific missing features (recommendations)
| Complaint | New | Original | Times more common |
|---|---|---|---|
| Switching accounts | 6.1% | 0.7% | 8.7× |
| Forced migration | 7.1% | 1.0% | 7.1× |
| No running balance | 5.3% | 0.8% | 6.6× |
| Balance preview removed | 4.3% | 1.2% | 3.6× |

- These complaints are 3.6–8.7× more common in the new app and point to
  specific features ING could restore or improve.
- Paying new payees: 0.5% (new) vs 0.6% (original). Tested because one
  review raised it, but it's about the same in both apps, so it's not a
  new-app issue.


### Finding 8: Churn intent
- 3.9% (new) vs 2.1% (original): about 1.9× more common in the new app
- Among churn reviews: Prefer old app 31.2%, Transactions & balance 22.7%,
  Crashes 13.6%, Forced migration 13.0%
- Forced migration is ~3× more common among churn reviews than overall,
  and crashes are also over-represented.
- Missing running balance is a top complaint, but rarely linked to leaving (0.6%).
- So what: annoyance alone doesn't drive churn; feeling FORCED does, plus
  an app that fails. Giving customers more choice or time during migration,
  and prioritising stability, may reduce churn risk most.

## Method notes

**Data**
- 5,815 reviews collected: Google Play (both apps) and App Store (both apps)
- App Store limited to the 500 most recent reviews per app (Apple feed limit)
- All dates converted to UTC so both stores compare correctly
- Removed 323 short reviews (<15 characters), leaving 5,492
- No usernames or personal details stored

**Analysis**
- Sentiment based on stars: 1–2 negative, 3 neutral, 4–5 positive
- Fair comparison uses the same period (2026) for both apps
- Monthly averages only reported with 30+ reviews
- App versions analysed by store, as iOS and Android number them differently
- Churn drivers found by comparing themes among churn reviews against all reviews
- Feature percentages are lower bounds: many reviewers don't name the exact feature

**Keyword tag checks** (random samples of 10 per theme)

| Theme | Accuracy | Fix made |
|---|---|---|
| Prefer old app | 10/10 | |
| Churn intent | 8/10 | removed "moving to" (matched "moving to online banking") |
| Transactions & balance | 8/10 | |
| Design & navigation | 7/10 | added word boundaries, as "ui" matched inside "quick" |

**Limitations**
- Reviews are self-selected: unhappy customers are more likely to post
- Reply rates measured on Google Play only (Apple's feed has no developer replies)
- VPN theme dropped: too few mentions (0.1%)
- Independent project using public data; not affiliated with ING
