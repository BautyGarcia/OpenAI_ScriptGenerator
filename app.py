import streamlit as st

numero = st.number_input("Ingrese un número", 0, 100, 1)
st.write("El número ingresado es:", numero + 5)