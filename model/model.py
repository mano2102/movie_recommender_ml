import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
movies = pd.read_csv("tmdb_5000_movies.csv")

# Keep required columns
movies = movies[['title', 'overview']]

# Remove nulls
movies.dropna(inplace=True)

# Vectorization
tfidf = TfidfVectorizer(
    max_features=5000,
    stop_words='english'
)

vectors = tfidf.fit_transform(
    movies['overview']
).toarray()

# Similarity matrix
similarity = cosine_similarity(vectors)


def recommend(movie):

    movie = movie.strip()

    index = movies[
        movies['title'].str.lower() == movie.lower()
    ].index

    if len(index) == 0:
        return ["Movie not found"]

    index = index[0]

    distances = similarity[index]

    movie_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )

    recommendations = []

    for i in movie_list[1:6]:
        recommendations.append(
            movies.iloc[i[0]].title
        )

    return recommendations