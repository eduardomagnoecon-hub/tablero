import streamlit as st

st.title("🌡️ Hola desde Streamlit")
st.write("Esta es tu primera aplicación funcionando en la nube 🎉")

st.header("Demostración interactiva")
numero = st.slider("Selecciona un número", 1, 100, 50)
st.write("El cuadrado de ese número es:", numero ** 2)


