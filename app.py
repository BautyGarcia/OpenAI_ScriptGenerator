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

def generate_plot(plot):
    return "From a given movie plot, create a script that could fit in the movie between the characters you can identify from the plot:" + plot

response = openai.Completion.create(
    engine="davinci",
    prompt=generate_plot(plot),
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6
)


st.write(responss.choices[0].text)