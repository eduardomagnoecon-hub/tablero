import streamlit as st
import numpy as np  # 👈 necesario para la matriz

st.title("🌡️ Hola desde Streamlit")
st.write("Esta es tu primera aplicación funcionando en la nube 🎉")

# ----------------------------
# Demostración simple (tu parte)
# ----------------------------
st.header("Demostración interactiva")
numero = st.slider("Selecciona un número", 1, 100, 50)
st.write("El cuadrado de ese número es:", numero ** 2)

# ----------------------------
# NUEVA SECCIÓN: Matriz 4x4 con NumPy
# ----------------------------
st.header("Matriz 4×4 con Numpy: medias por columna y suma de la diagonal")

# Controles (opcionalmente te dejo configurables el tamaño y el rango)
col1, col2, col3 = st.columns(3)
with col1:
    size = st.number_input("Tamaño (n×n)", min_value=2, max_value=10, value=4, step=1)
with col2:
    min_val = st.number_input("Mínimo aleatorio", min_value=0, max_value=1000, value=1, step=1)
with col3:
    max_val = st.number_input("Máximo aleatorio (incl.)", min_value=min_val+1, max_value=10000, value=100, step=1)

seed = st.number_input("Semilla (opcional para reproducibilidad)", min_value=0, max_value=999999, value=0, step=1)
if seed:
    np.random.seed(seed)

if st.button("Generar matriz"):
    # Matriz n×n con enteros aleatorios entre min_val y max_val (incl.)
    matriz = np.random.randint(min_val, max_val + 1, size=(size, size))

    # Media por columna (axis=0)
    media_columnas = np.mean(matriz, axis=0)

    # Suma de la diagonal principal (trace)
    suma_diagonal = np.trace(matriz)

    st.subheader("Matriz generada")
    st.dataframe(matriz)  # tabla bonita

    st.subheader("Resultados")
    st.write("**Media por columna:**", media_columnas)
    st.write("**Suma de la diagonal principal:**", int(suma_diagonal))

    # (Opcional) Estadísticos adicionales
    st.write("**Mínimo / Máximo / Promedio global:**",
             int(matriz.min()), int(matriz.max()), float(matriz.mean()))
else:
    st.info("Haz clic en **Generar matriz** para crear la matriz y ver los resultados.")

