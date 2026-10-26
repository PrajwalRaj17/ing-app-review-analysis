import pandas as pd
from bertopic import BERTopic
from umap import UMAP
from sklearn.feature_extraction.text import CountVectorizer
from hdbscan import HDBSCAN

df = pd.read_csv("data/ing_reviews_tagged.csv")

# Negative reviews of the new app only
docs_df = df[(df["app"] == "Do your thing - ING Banking") & (df["sentiment"] == "Negative")]
docs = docs_df["text"].tolist()
print("Reviews to analyse:", len(docs))

# Remove common English words ("the", "and") and words every review uses,
# so topic labels show meaningful words
custom_stop = ["app", "ing", "bank", "banking", "new", "old"]
vectorizer = CountVectorizer(stop_words=list(CountVectorizer(stop_words="english").get_stop_words()) + custom_stop)

# Fix the randomness so you get the same topics every run
umap_model = UMAP(n_neighbors=15, n_components=5, min_dist=0.0, metric="cosine", random_state=1)
hdbscan_model = HDBSCAN(
    min_cluster_size=20,              # smallest group allowed
    min_samples=5,                    # lower = less strict about what counts as a group
    metric="euclidean",
    cluster_selection_method="leaf",  # prefer many smaller groups over one big one
    prediction_data=True,
)

topic_model = BERTopic(
    umap_model=umap_model,
    hdbscan_model=hdbscan_model,
    vectorizer_model=vectorizer,
)

topics, _ = topic_model.fit_transform(docs)

info = topic_model.get_topic_info()
print(info[["Topic", "Count", "Name"]].head(25).to_string(index=False))

info.to_csv("outputs/topics_new_app_negative.csv", index=False)

for topic_id in [6, 12, 2, 10]:
    print(f"\n=== Topic {topic_id} ===")
    for doc in topic_model.get_representative_docs(topic_id):
        print("-", doc[:250])