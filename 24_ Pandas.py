import pandas as pd

datos={
  "Medicion": [1, 2, 3, 4, 5],
  "Distancia": [15, 18, 22, 12, 30]
}
tabla_datos=pd.DataFrame(datos)#pone esos datos en una tabla
#print(tabla_datos)

#print(tabla_datos["Distancia"])#Solo imprime la columna de distancia
#promedio= tabla_datos["Distancia"].mean()#.mean para sacar el promedio y se selcciona la columna
#print(promedio)
#dis_max= tabla_datos["Distancia"].max()#.max para sacar el maximo de la columna
#print(dis_max)
tem_altas= tabla_datos[tabla_datos["Distnacia"]>=20]#para comparar
print(tem_altas)
tabla_datos["Distancia Doble"]= tabla_datos["Distancia"]*2#para crear una nueva columna se menciona la tabla luego se realiza lo que se va a agregar
print(tabla_datos)

tabla_datos.to_csv("distancia.csv", index=False)
