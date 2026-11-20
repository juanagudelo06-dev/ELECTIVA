import numpy as np
#numpy nos permite realizar operaciones matematicas
#temperaturas= np.array([26, 28, 31, 29, 25, 33, 27])

#temp_aumentadas= temperaturas+2
#promedio=np.mean(temperaturas)#mean para sacar promedio
#tem_max= np.max(temperaturas)#max para sacar el numero mas alto
#tem_min=np.min(temperaturas)#numero minimo

#print(temp_aumentadas)
#print(promedio)
#print(tem_max)
#print(tem_min)
#print(temperaturas[0])
#print(temperaturas[6])

#tem_bajas=temperaturas[temperaturas<28]
#print(tem_bajas)
#tem_altas=temperaturas[temperaturas>=29]
#print(tem_altas)


temperaturas=np.array([20,21,19,22,20,21,19])
suma=np.sum(temperaturas)
promedio=np.meam(temperaturas)
media_std=np.std(temperaturas)
print(suma)
print(round(promedio,2))
print(round(medi_std,2))
