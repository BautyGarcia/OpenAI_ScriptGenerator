import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

with st.form(key='InputForm'):
    openai.api_key = st.text_input("OpenAI API Key", type="password")

    movieName = st.text_input("Enter a movie name")

    language = st.selectbox("Language", ["English", "Español"])

    st.form_submit_button(label='Submit')


if movieName != "" and openai.api_key != "":

    moviesInfo = IMDB.search_movie(movieName)

    movieID = moviesInfo[0].movieID

    movie = IMDB.get_movie(movieID)

    plot = ""

    for a in range(3):
        plot += movie['plot'][a]

    if language == "English":
        openai.Language = "en"
    elif language == "Español":
        openai.Language = "es"
        
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Write a script with speechlines from a given movie plot between the characters: \n" + plot + "\n",
        temperature=1,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    st.success(response.choices[0].text)

else:
    st.success("Please enter a movie name and your OpenAI API Key")

