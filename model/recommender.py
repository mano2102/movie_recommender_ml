class Recommender:

    def __init__(self, df, similarity):
        self.df = df
        self.similarity = similarity

    # -------------------------
    # Main recommendation function
    # -------------------------
    def recommend(self, movie_name):

        # normalize input
        movie_name = movie_name.strip().lower()

        # find movie index
        index_list = self.df[self.df['title'].str.lower() == movie_name].index

        if len(index_list) == 0:
            return ["Movie not found ❌"]

        index = index_list[0]

        # similarity scores for that movie
        distances = self.similarity[index]

        # sort movies based on similarity score
        movie_list = sorted(
            list(enumerate(distances)),
            reverse=True,
            key=lambda x: x[1]
        )

        # top recommendations (skip first one itself)
        recommendations = []

        for i in movie_list[1:6]:
            movie_index = i[0]
            recommendations.append(self.df.iloc[movie_index].title)

        return recommendations