import os
import pandas as pd


def load_data():

    # -----------------------------
    # 1. Get project root directory
    # -----------------------------
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # -----------------------------
    # 2. Dataset path (safe)
    # -----------------------------
    DATASET_DIR = os.path.join(BASE_DIR, "dataset")

    movies_path = os.path.join(DATASET_DIR, "tmdb_5000_movies.csv")
    credits_path = os.path.join(DATASET_DIR, "tmdb_5000_credits.csv")

    # -----------------------------
    # 3. Load CSV files
    # -----------------------------
    movies = pd.read_csv(movies_path)
    credits = pd.read_csv(credits_path)

    print("Movies shape:", movies.shape)
    print("Credits shape:", credits.shape)

    return movies, credits


# -----------------------------
# Optional test run
# -----------------------------
if __name__ == "__main__":
    movies, credits = load_data()
    print(movies.head())