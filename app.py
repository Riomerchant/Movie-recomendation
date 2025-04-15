import streamlit as st
import pickle
import pandas as pd
import requests


headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhMDZlYzViOWFmMzFlMGU3YTM0YzQ1MmFhMGJmZjNjMyIsIm5iZiI6MTc0MDMxMzgzMC41NTYsInN1YiI6IjY3YmIxNGU2ZWZmZWI5NmU5ZTBhYWRiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.hxEPxUf57elFIx0t_ckmfEvSQW39CZED5EzN0qywu9Q"
}

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    diss = simi[movie_index]
    movie_list = sorted(list(enumerate(diss)),reverse=True,key=lambda x: x[1])[1:6]
    recpos = []
    recmovie = []
    for i in movie_list:
        movie_id = movies.iloc[i[0]].id
        recmovie.append(movies.iloc[i[0]].title)
        recpos.append(fetch_poster(movie_id))
    return recmovie,recpos


def fetch_poster(movie_id):
        response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?language=en-US',headers=headers)
        data = response.json()
        return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)
simi = pickle.load(open('simi.pkl','rb'))

st.title("Movie Recommendation System")
mame = st.selectbox(
    'Select a Movie',
    movies['title'].values
)

if st.button('Recommend'):
    names,poster = recommend(mame)
    col1, col2, col3,col4,col5 = st.columns(5)

    with col1:
        st.image(poster[0])
        st.text(names[0])

    with col2:
        st.image(poster[1])
        st.text(names[1])

    with col3:
        st.image(poster[2])
        st.text(names[2])

    with col4:
        st.image(poster[3])
        st.text(names[3])

    with col5:
        st.image(poster[4])
        st.text(names[4])