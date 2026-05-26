from flask import Flask, request, jsonify

from model.data_loader import load_data
from model.preprocessing import run_preprocessing
from model.vectorizer import run_vectorizer
from model.recommender import Recommender

app = Flask(__name__)

# -------------------------
# 1. Load and prepare ML pipeline ONCE at startup
# -------------------------
movies, credits = load_data()

final_df = run_preprocessing(movies, credits)

vectors, similarity = run_vectorizer(final_df)

recommender = Recommender(final_df, similarity)

# -------------------------
# 2. API Endpoint
# -------------------------
@app.route("/",methods=['GET'])
def welcome():
    if request.method=='GET':
        return jsonify({
            "message":"Welcome to movie recommender system."
        }),200
@app.route("/recommend", methods=["GET", "POST"])
def recommend():

    # -------------------------
    # GET REQUEST
    # -------------------------
    if request.method == "GET":

        movie_name = request.args.get("movie")

    # -------------------------
    # POST REQUEST
    # -------------------------
    else:

        data = request.get_json()

        movie_name = data.get("movie")

    # -------------------------
    # Validation
    # -------------------------
    if not movie_name:

        return jsonify({
            "error": "Movie name is required"
        }), 400

    # -------------------------
    # Recommendation
    # -------------------------
    result = recommender.recommend(movie_name)

    return jsonify({
        "movie": movie_name,
        "recommendations": result
    })
@app.route("/search",methods=['GET'])
def  search_movie():
    query=request.args.get("query")
    if not query:
        return jsonify({
            "error":"Query parameter is required"
        }),400
    matches = final_df[
        final_df['title'].str.lower().str.startswith(query.lower())
    ]

    # get top 10 matches
    movie_list = matches['title'].head(10).tolist()

    return jsonify({
        "query": query,
        "results": movie_list
    })
# -------------------------
# 3. Run Server
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)