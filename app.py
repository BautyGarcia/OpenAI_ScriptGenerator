import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

openai.api_key = st.text_input("OpenAI API Key")

movieName = st.text_input("Enter a movie name")

moviesInfo = IMDB.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = IMDB.get_movie(movieID)

plot = ""

for a in range(3):
    plot += movie['plot'][a]

def generate_prompt(Plot):
return """From a given movie plot, create a script that could fit in the movie between the characters you can identify from the plot: """ + Plot

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=generate_prompt(plot),
    temperature=1,
    max_tokens = 4000,
)

st.write(response['choices'][0]['text'])