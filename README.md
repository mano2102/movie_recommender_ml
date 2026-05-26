

# 🎬 Movie Recommendation System

A Machine Learning based Movie Recommendation Backend API built using Flask, Pandas, and Scikit-learn.

This project recommends similar movies based on movie metadata using:
- TF-IDF Vectorization
- Cosine Similarity
- Flask REST API

---

# 🚀 Features

✅ Movie Recommendation API  
✅ Search/Autocomplete API  
✅ TF-IDF based recommendation engine  
✅ Flask backend integration  
✅ Modular ML pipeline structure  

---

# 🛠️ Tech Stack

- Python
- Flask
- Pandas
- Scikit-learn
- TF-IDF Vectorizer
- Cosine Similarity

---

# 📁 Project Structure

```bash
movie-recommender/
│
├── dataset/
│   ├── tmdb_5000_movies.csv
│   └── tmdb_5000_credits.csv
│
├── model/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── vectorizer.py
│   └── recommender.py
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_URL
```

---

## 2. Move Into Project

```bash
cd movie-recommender
```

---

## 3. Create Virtual Environment

```bash
python3 -m venv venv
```

---

## 4. Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run Application

```bash
python3 app.py
```

Server runs on:

```text
http://127.0.0.1:5000
```

---

# 📡 API Endpoints

---

## 1. Welcome API

### GET /

```text
http://127.0.0.1:5000/
```

### Response

```json
{
  "message": "Welcome to movie recommender system."
}
```

---

## 2. Recommendation API

### GET Request

```text
http://127.0.0.1:5000/recommend?movie=Avatar
```

### POST Request

```json
POST /recommend

{
  "movie": "Avatar"
}
```

### Response

```json
{
  "movie": "Avatar",
  "recommendations": [
    "John Carter",
    "Star Trek",
    "Interstellar"
  ]
}
```

---

## 3. Search API

### GET Request

```text
http://127.0.0.1:5000/search?query=bat
```

### Response

```json
{
  "query": "bat",
  "results": [
    "Batman Begins",
    "Batman Returns"
  ]
}
```

---

# 🧠 ML Workflow

```text
Dataset
   ↓
Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity
   ↓
Recommendation Engine
   ↓
Flask API
```

---

# 📌 Future Improvements

- React Frontend
- Model Serialization using Pickle
- Better NLP preprocessing
- Advanced Recommendation Algorithms
- Deployment on Render/Railway

---

# 📄 License

This project is open-source and available for learning purposes.