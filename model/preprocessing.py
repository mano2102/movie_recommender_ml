import pandas as pd
import os


class Preprocessor:

    def __init__(self, movies, credits):
        self.movies = movies
        self.credits = credits

    # -------------------------
    # 1. Merge datasets
    # -------------------------
    def merge_data(self):
        self.movies = self.movies.merge(self.credits, on="title")
        return self.movies

    # -------------------------
    # 2. Select important columns
    # -------------------------
    def select_features(self):
        self.movies = self.movies[[
            'movie_id',
            'title',
            'overview',
            'genres',
            'keywords',
            'cast',
            'crew'
        ]]
        return self.movies

    # -------------------------
    # 3. Handle missing values
    # -------------------------
    def clean_data(self):
        self.movies.dropna(inplace=True)
        return self.movies

    # -------------------------
    # 4. Create TAGS (MOST IMPORTANT STEP)
    # -------------------------
    def create_tags(self):

        self.movies['tags'] = (
            self.movies['overview'].astype(str) + " " +
            self.movies['genres'].astype(str) + " " +
            self.movies['keywords'].astype(str) + " " +
            self.movies['cast'].astype(str) + " " +
            self.movies['crew'].astype(str)
        )

        return self.movies

    # -------------------------
    # 5. Final cleanup
    # -------------------------
    def finalize(self):

        self.movies['tags'] = self.movies['tags'].str.lower()

        final_df = self.movies[['movie_id', 'title', 'tags']]

        return final_df


# -------------------------
# PIPELINE RUN FUNCTION
# -------------------------
def run_preprocessing(movies, credits):

    processor = Preprocessor(movies, credits)

    movies = processor.merge_data()
    movies = processor.select_features()
    movies = processor.clean_data()
    movies = processor.create_tags()
    final_df = processor.finalize()

    print("Preprocessing completed ✔")
    print("Final shape:", final_df.shape)

    return final_df