import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

movieName = st.text_input("Enter a movie name")

moviesInfo = imdb.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = imdb.get_movie(movieID)

movieTitle = movie['title']

st.write(movieTitle)