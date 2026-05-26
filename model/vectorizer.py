from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class Vectorizer:
    def __init__(self,df):
        self.df=df
    #--------
    #Convert text - vectors
    #--------
    def create_vectors(self):
        tdfir=TfidfVectorizer(
            max_features=5000,
            stop_words='english'
        )
        vectors=tdfir.fit_transform(self.df['tags']).toarray()
        print("Vectorization commpleted!!!")
        print("Shape: ",vectors.shape)
        return vectors
    # -------------------------
    # Build similarity matrix
    # -------------------------
    def build_similarity(self, vectors):

        similarity = cosine_similarity(vectors)

        print("Similarity matrix created ✔")
        print("Shape:", similarity.shape)

        return similarity


# -------------------------
# Pipeline function
# -------------------------
def run_vectorizer(df):

    vec = Vectorizer(df)

    vectors = vec.create_vectors()
    similarity = vec.build_similarity(vectors)

    return vectors, similarity