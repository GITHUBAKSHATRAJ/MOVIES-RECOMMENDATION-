import pickle
import streamlit as st
import requests

# Function to fetch movie poster using OMDb API
def fetch_poster(movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&apikey=e439dc68"
    data = requests.get(url).json()
    poster_url = data.get('Poster')
    return poster_url

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector: vector[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:6]:
        recommended_movie_name = movies.iloc[i[0]].title
        recommended_movie_names.append(recommended_movie_name)
        # Fetch the movie poster using the movie title
        recommended_movie_posters.append(fetch_poster(recommended_movie_name))

    return recommended_movie_names, recommended_movie_posters

# Streamlit UI
st.header('Movie Recommender System')
movies = pickle.load(open('movies_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    recommended_movie_names, recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5 = st.columns(5)  # Changed from beta_columns to columns
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])
    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
