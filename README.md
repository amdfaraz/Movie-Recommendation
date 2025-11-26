

# 🎬 Movie Recommendation System

This is a simple **Python-based Movie Recommendation System** that suggests movies either by:

1. **Similarity of genres to a selected movie**, using

   * **CountVectorizer** (bag-of-words of genres)
   * **Cosine similarity**
2. **Filtering movies by genre**

The system uses a small built-in dataset of six movies and interacts with the user via console input.

---

## 📌 Features

### ✅ Recommend by Movie Title

* Enter the name of a movie from the dataset.
* The system finds movies with similar genres using cosine similarity.
* Returns the top 3 most similar movies.

### ✅ Recommend by Genre

* Enter any genre keyword (e.g., *Action*, *Drama*, *Sci-Fi*).
* The system returns movies matching that genre.

---

## 🛠️ Technologies Used

* **Python**
* **Pandas**
* **Scikit-learn**

  * `CountVectorizer`
  * `cosine_similarity`

---

## 📂 Dataset Used

The program uses the following mini dataset:

| movie_id | Title           | Genres           |
| -------- | --------------- | ---------------- |
| 1        | Inception       | Action Sci-Fi    |
| 2        | Interstellar    | Sci-Fi Drama     |
| 3        | The Dark Knight | Action Thriller  |
| 4        | Titanic         | Romantic Drama   |
| 5        | La La Land      | Romantic Musical |
| 6        | The Matrix      | Sci-Fi Action    |

---

## 🚀 How It Works

### 1️⃣ Building the Genre Similarity Matrix

```python
cv = CountVectorizer()
genre_matrix = cv.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(genre_matrix)
```

### 2️⃣ Recommend by Movie Title

* Finds the selected movie index
* Sorts similarity scores
* Returns the top recommendations

### 3️⃣ Recommend by Genre

* Converts genre input to lowercase
* Finds partial matches in the genre list
* Returns first matching results

---

## ▶️ How to Run

1. Make sure required packages are installed:

```bash
pip install pandas scikit-learn
```

2. Save the Python script in a file, e.g., `movie_recommender.py`.

3. Run the script:

```bash
python movie_recommender.py
```

4. Follow the on-screen prompts:

```
🎬 Welcome to Movie Recommendation System 🎬
Choose option:
1. Recommend by Movie Title
2. Recommend by Genre
```

---

## 🧪 Example Usage

### **If user selects movie title:**

```
Enter a movie you like: Inception

Recommended Movies:
1. The Matrix
2. Interstellar
3. The Dark Knight
```

### **If user selects genre:**

```
Enter a genre you like: Romantic

Recommended Movies:
1. Titanic
2. La La Land
```

---

## 📌 Notes

* This is a **toy demo**, not a full recommendation engine.
* For real applications:

  * Use larger datasets
  * Apply TF-IDF or embeddings
  * Integrate user profiles or ratings

---

## 📜 License

Free to use, modify, and extend.
