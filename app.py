import pickle
import streamlit as st
import requests
import pandas as pd


# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    data = requests.get(url).json()
    poster_path = data.get('poster_path')
    if poster_path:
        full_path = f"https://image.tmdb.org/t/p/w500/{poster_path}"
        return full_path
    return "https://via.placeholder.com/500x750?text=No+Image"


# Function to recommend movies
def recommend(movie):
    try:
        index = movies[movies['title'] == movie].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_movie_names = []
        recommended_movie_posters = []

        for i in distances[1:6]:
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))

        return recommended_movie_names, recommended_movie_posters

    except Exception as e:
        st.error(f"Error in recommendation: {e}")
        return [], []


# Streamlit App Title
st.header('🎬 Movie Recommender System')

# Load the movie data and similarity matrix
try:
    movies = pickle.load(open('movies_dict.pkl', 'rb'))
    similarity = pickle.load(open('similarity.pkl', 'rb'))

    # Ensure movies is a DataFrame
    if isinstance(movies, dict):
        movies = pd.DataFrame(movies)

    # Validate the 'title' column exists
    if 'title' not in movies.columns:
        st.error("Error: 'title' column not found in movie data!")
        st.stop()

    # Extract movie list for the dropdown
    movie_list = movies['title'].tolist()

    # Dropdown to select a movie
    selected_movie = st.selectbox(
        "Type or select a movie from the dropdown",
        movie_list
    )

    # Button to show recommendations
    if st.button('Show Recommendation'):
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie)

        if recommended_movie_names:
            cols = st.columns(5)
            for col, name, poster in zip(cols, recommended_movie_names, recommended_movie_posters):
                with col:
                    st.text(name)
                    st.image(poster)
        else:
            st.warning("No recommendations found!")

except FileNotFoundError as e:
    st.error(f"File not found: {e}")
except Exception as e:
    st.error(f"An error occurred: {e}")
