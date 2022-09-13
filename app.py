import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

with st.form(key='my_form'):
    openai.api_key = st.text_input("OpenAI API Key", type="password")

    movieName = st.text_input("Enter a movie name")

    st.form_submit_button(label='Submit')

moviesInfo = IMDB.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = IMDB.get_movie(movieID)

plot = ""

for a in range(3):
    plot += movie['plot'][a]

response = openai.Completion.create(
    model="text-davinci-002",
    prompt="From a given movie plot, create a script between the movie characters changing that given movie plot: " + plot,
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

st.write(response.choices[0].text)