import streamlit as st #st sirve como alias

st.title("Analisis de distancias")
st.write("Bienvenido al primer dashboard")

distanacia= st.slider("Seleccione una distancia en cm", 0, 50, 20)
st.write("Distancia seleccionada: ", distancia)

if distancia < 20:
  st.write("Objeto cerca")
else:
  st.write("Distancia segura")

import pandas as pd
datos={
  "Medicion": [1, 2, 3, 4, 5, 6, 7, 8],
  "Distancia": [15, 18, 22, 12, 30, 25, 10, 20]
}

tabla = pd.DataFrame(datos)

st.subheader("Registro de mediciones")
st.dataframe(tabla)

st.subheader("Grafica de distancia")

st.line_chart(tabla, x="Medicion", y="Distancia")
tabla["Distancia Ajustada"]=tabla["Distancia"]+2
