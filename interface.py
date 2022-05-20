import streamlit as st
import pandas as pd
import requests
import pickle


# =========================================
def get_movie_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{'
                            '}?api_key=042fd2989c8e20e75eb1431a4d9f880c&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Re-implement the 'recommend' function
def recommend(movie_name):
    movie_idx = movies[movies['title'] == movie_name].index[0]
    distances = sim[movie_idx]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda i: i[1])[1:11]
    movies_recommended_list = []
    movies_recommended_posters = []
    for movie in movies_list:
        movie_id = movies.iloc[movie[0]].movie_id
        movies_recommended_list.append(movies.iloc[movie[0]].title)
        movies_recommended_posters.append(get_movie_poster(movie_id))
    return movies_recommended_list, movies_recommended_posters
# =========================================


# Loading Movies Data...
movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
sim = pickle.load(open('sim.pkl', 'rb'))

# Building Widgets...
st.set_page_config(layout="wide")

# Page Title
colT1, colT2 = st.columns([5, 10])
with colT2:
    st.title('Movies AI-Recommender')

# Movies Select Box
selected_movie_name = st.selectbox('Pick a Movie to get Similar Movies!', movies['title'].values)

# Recommend Button
if st.button('Recommend 10 Similar Movies'):
    names, posters = recommend(selected_movie_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        with st.form(key='f0'):
            st.subheader(names[0])
            st.image(posters[0])
            st.form_submit_button("See More")
        with st.form(key='f3'):
            st.subheader(names[3])
            st.image(posters[3])
            st.form_submit_button("See More")
        with st.form(key='f6'):
            st.subheader(names[6])
            st.image(posters[6])
            st.form_submit_button("See More")
        with st.form(key='f9'):
            st.subheader(names[9])
            st.image(posters[9])
            st.form_submit_button("See More")

    with col2:
        with st.form(key='f1'):
            st.subheader(names[1])
            st.image(posters[1])
            st.form_submit_button("See More")
        with st.form(key='f4'):
            st.subheader(names[4])
            st.image(posters[4])
            st.form_submit_button("See More")
        with st.form(key='f7'):
            st.subheader(names[7])
            st.image(posters[7])
            st.form_submit_button("See More")

    with col3:
        with st.form(key='f2'):
            st.subheader(names[2])
            st.image(posters[2])
            st.form_submit_button("See More")
        with st.form(key='f5'):
            st.subheader(names[5])
            st.image(posters[5])
            st.form_submit_button("See More")
        with st.form(key='f8'):
            st.subheader(names[8])
            st.image(posters[8])
            st.form_submit_button("See More")
