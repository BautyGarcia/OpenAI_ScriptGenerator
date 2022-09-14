from turtle import clear
import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

with st.form(key='InputForm'):
    openai.api_key = st.text_input("OpenAI API Key", type="password")

    movieName = st.text_input("Enter a movie name")

    st.form_submit_button(label='Submit')

moviesInfo = IMDB.search_movie(movieName)

movieID = moviesInfo[0].movieID

movie = IMDB.get_movie(movieID)

plot = ""

for a in range(3):
    plot += movie['plot'][a]

print(plot)
print("Resultado: \n")
response = openai.Completion.create(
    model="text-davinci-002",
    prompt="Write a script with speechlines from a given movie plot between the characters: \n" + plot + "\n",
    temperature=1,
    max_tokens=3500,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)

with st.form(key='OutputForm', clear_on_submit=True):
    st.text_area("Result", value=response['choices'][0]['text'])

    st.form_submit_button(label='Submit')
