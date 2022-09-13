import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

openai.api_key = st.text_input("OpenAI API Key")

movieName = st.text_input("Enter a movie name", "Supercool")

moviesInfo = IMDB.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = IMDB.get_movie(movieID)

for a in range(5):
    plot += movie['plot'][a]

st.write(plot)