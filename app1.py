import streamlit as st
st.title('Movie Recommender')
import pandas as pd
import pickle

import requests
def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2708a68dac6ce0de710228bab1a799e1&language=en-US'.format(movie_id))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']
movies=pickle.load(open('movies.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))

def recommand(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[0:6]
    recomended_movies=[]
    recomended_movies_posters=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].id
        recomended_movies_posters.append(fetch_poster(movie_id))
        recomended_movies.append(movies.iloc[i[0]].title)
    return recomended_movies,recomended_movies_posters

selected_movie_name = st.selectbox(
    'Type the movie name',
     (movies['title'].values))

if st.button('Recommend'):
     name,poster=recommand(selected_movie_name)
     #fetching psoter from API

     col1, col2, col3,col4, col5, col6 = st.columns(6)

     with col1:
         st.text(name[0])
         st.image(poster[0])

      with col2:
         st.text(name[1])
         st.image(poster[1])

     with col3:
         st.text(name[2])
         st.image(poster[2])
     with col4:
         st.text(name[3])
         st.image(poster[3])
     with col5:
         st.text(name[4])
         st.image(poster[4])
     with col6:
         st.text(name[5])
         st.image(poster[5])
