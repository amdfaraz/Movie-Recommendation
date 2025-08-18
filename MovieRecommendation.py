import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
data = {
    "movie_id": [1, 2, 3, 4, 5, 6],
    "title": ["Inception", "Interstellar", "The Dark Knight",
              "Titanic", "La La Land", "The Matrix"],
    "genres": ["Action Sci-Fi", "Sci-Fi Drama", "Action Thriller",
               "Romantic Drama", "Romantic Musical", "Sci-Fi Action"]
}

movies = pd.DataFrame(data)
cv = CountVectorizer()
genre_matrix = cv.fit_transform(movies['genres'])
cosine_sim = cosine_similarity(genre_matrix)

def recommend_by_movie(movie_title, num_recommendations=3):
    if movie_title not in movies['title'].values:
        return ["❌ Movie not found in dataset!"]
    
    idx = movies[movies['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:num_recommendations+1]  
    movie_indices = [i[0] for i in sim_scores]
    return movies['title'].iloc[movie_indices].tolist()
def recommend_by_genre(genre, num_recommendations=3):
    genre = genre.lower()
    filtered = movies[movies['genres'].str.lower().str.contains(genre)]
    if filtered.empty:
        return ["❌ No movies found for this genre!"]
    return filtered['title'].head(num_recommendations).tolist()
print("🎬 Welcome to Movie Recommendation System 🎬")
print("Choose option:")
print("1. Recommend by Movie Title")
print("2. Recommend by Genre")

choice = input("Enter 1 or 2: ")

if choice == "1":
    print("\nAvailable movies:", movies['title'].tolist())
    user_movie = input("\nEnter a movie you like: ")
    recommendations = recommend_by_movie(user_movie)
    print("\n✅ Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")

elif choice == "2":
    print("\nAvailable genres: Action, Sci-Fi, Thriller, Romantic, Drama, Musical")
    user_genre = input("\nEnter a genre you like: ")
    recommendations = recommend_by_genre(user_genre)
    print("\n✅ Recommended Movies:")
    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. {movie}")

else:
    print("❌ Invalid choice!")
