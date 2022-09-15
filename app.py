#Set up
import streamlit as st
import openai
import imdb

IMDB = imdb.IMDb()

#Input form
with st.form(key='InputForm'):
    
    st.markdown("""<a href="https://beta.openai.com/account/api-keys" target="_blank">Get your API Key</a>""", unsafe_allow_html=True)

    openai.api_key = st.text_input("OpenAI API Key", type="password")

    movieName = st.text_input("Enter a movie name")

    language = st.selectbox("Language", ["English", "Spanish", "French", "German", "Italian", "Japanese", "Portuguese", "Russian", "Chinese"])

    st.form_submit_button(label='Submit')

#Check if form is filled and start app process. If not, return a message
if movieName != "" and openai.api_key != "":

    #Get movie plot via IMDB API
    moviesInfo = IMDB.search_movie(movieName)

    movieID = moviesInfo[0].movieID

    movie = IMDB.get_movie(movieID)

    plot = ""

    for a in range(2):
        plot += movie['plot'][a]

    #Create openai response with prompt
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Write a script with speechlines from a given movie plot between the characters: \n" + plot + "\n",
        temperature=1,
        max_tokens=3500,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    #If another language than english was selected, translate the script into that language.
    #Else, return the english script
    if language == "English":
        st.success(response.choices[0].text)
    else:
        LanResponse = openai.Completion.create(
            model="text-davinci-002",
            prompt="Translate this into" + language + ": \n" + response.choices[0].text + "\n",
            temperature=1,
            max_tokens=3500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        st.success(LanResponse.choices[0].text)
else:
    st.success("Please enter a movie name and your OpenAI API Key")