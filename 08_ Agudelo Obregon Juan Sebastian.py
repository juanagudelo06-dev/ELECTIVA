producto=[{"nombre": "Teclado","precio":80000,"cantidad":3 },
    {"nombre":"Mouse","precio":50000,"cantidad":5},
    {"nombre":"Monitor","precio":700000,"cantidad":2},
    {"nombre":"Camara","precio":120000,"cantidad":1},
    ]

def calcular_total(precio, cantidad):
    calcular_total=precio*cantidad
    return calcular_total

for producto in producto:
    total=calcular_total(producto["precio"], producto["cantidad"])
    producto["total"]= total
    print(producto["nombre"], producto["total"])

bajo_stock = []
for producto in producto:
    if producto["cantidad"] <= 2:
        bajo_stock.append(producto["nombre"])

suma=0
for suma in producto:
    suma+= producto["total"]

print(f"Valor Total del inventario:{suma}")
print(f"Productos con bajo stock:{bajo_stock}")

           
    
