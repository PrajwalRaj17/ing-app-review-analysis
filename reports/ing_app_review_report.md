# What ING customers say about the new app
*An independent analysis of 5,492 public app reviews · Prajwal Selvaraj · October 2026*
*Not affiliated with ING · [Interactive dashboard](https://public.tableau.com/app/profile/prajwal.selvaraj/viz/INGAppReviewsIndependentAnalysis20252026/INGReviewsDashboard) · [Code on GitHub](https://github.com/PrajwalRaj17/ing-app-review-analysis)*

## Summary
I've banked with ING for two years, and when I moved to the new app, a few
things I relied on were suddenly harder to do. I wanted to know whether other
customers felt the same, so I analysed 5,492 public reviews of both ING apps.
They did: nearly half of the new app's reviews say the old app was better, and
most complaints point to specific features that changed, which means they are
fixable.

## Key findings
1. **A consistent rating gap.** In 2026, the new app averaged 1.43 stars,
   compared with 2.10 for the original app, and the gap appears on both the
   App Store and Google Play.
2. **No recovery over time.** Since the wide rollout in February 2026, the new
   app's monthly rating has stayed around 1.4 stars for eight months.
3. **Customers want the old app back.** 43.7% of new app reviews say the old
   app was better, compared with 3.7% for the original app.
4. **Specific features drive the frustration.** Compared with the original app,
   reviews of the new app are far more likely to mention account nicknames
   disappearing (12.5× more often), the new 5-digit PIN (10×), difficulty
   switching between accounts (8.7×) and the missing running balance (6.6×).
5. **Feeling forced is linked to leaving.** 3.9% of new app reviews mention
   switching banks (vs 2.1%). Among these, complaints about being forced to
   migrate are about three times more common than in reviews overall.

## Areas to consider
- **Restore account nicknames** when transferring between accounts, the single
  most common specific complaint.
- **Bring back familiar features** from the old app: running balances, swiping
  between accounts, and checking balances before logging in.
- **Revisit the 5-digit PIN**, or offer clearer guidance when setting it up.
  Many reviewers say they forget it or get locked out.
- **Ease the migration.** Clearer communication or more time before switching
  may reduce churn risk, alongside fixing "something went wrong" errors, which
  are more common in the new app (15.8% vs 12.6% of reviews).

## How I did it
I collected 5,815 reviews from Google Play and the App Store with Python, then
cleaned them to 5,492. I tagged themes using keyword searches, checked the tags
against random samples of real reviews (7–10 out of 10 accurate after fixes),
and used BERTopic, an NLP topic model, to find themes my keywords had missed.
The results are shown in an interactive Tableau dashboard.

## Limitations
- People who post reviews tend to be less happy than customers overall, so
  these findings describe reviewers, not all ING customers.
- Apple's public feed only provides the latest 500 reviews per app.
- Keyword tags are lower bounds, because many reviewers don't name the exact
  feature they're unhappy about.