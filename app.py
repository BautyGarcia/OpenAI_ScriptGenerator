import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

with st.form(key='my_form'):
    openai.api_key = st.text_input("OpenAI API Key")

    movieName = st.text_input("Enter a movie name")

    st.form_submit_button(label='Submit')

moviesInfo = IMDB.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = IMDB.get_movie(movieID)

plot = ""

for a in range(3):
    plot += movie['plot'][a]

def generate_prompt(plot):
    return """From a given movie plot, create a script that could fit in the movie between the characters you can identify from the plot: """ + plot

response = openai.Completion.create(
    model="text-davinci-002",
    prompt=generate_prompt(plot),
    temperature=1,
    max_tokens = 3500,
)

st.write(response['choices'][0]['text'])