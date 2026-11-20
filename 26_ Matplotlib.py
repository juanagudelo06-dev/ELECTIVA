import pandas as pd
import matplotlib.pyplot as plt

tabla=pd.read_csv("distancia.csv")

plt.plot(tabla["Medicion"], tabla["Distancia"])#.plot Diagrama de lineas
plt.bar(tabla["Medicion"], tabla["Distancia"])#.bar Diagrama de barras
plt.xlabel("Medicion")#para graficar o seleccionar en el eje x
plt.ylabel("Distancia")
plt.title("Distancias medidas por el HC-SR04")

plt.show()
