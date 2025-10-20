st.title("Hola desde Streamlit")
import streamlit as st

st.title("🌡️ Mi primer panel en Streamlit")
st.write("Hola, Edu. Esta es tu primera aplicación desplegada en la nube 🎉")

st.header("Demostración simple")
numero = st.slider("Selecciona un número", 1, 100, 50)
st.write("El cuadrado de ese número es:", numero ** 2)

