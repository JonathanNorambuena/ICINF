lista=[]
cant=0
sum=0
notas_baja=0
notas_altas=0
while True:
    nota=float(input("Ingrese las notas (ingrese 0 para terminar):"))
    lista.append(nota)
    cant=cant+1
    sum=sum+nota
    if nota==0:
        break
    if nota<4.0:
        notas_baja=notas_baja+1
    else:
        notas_altas=notas_altas+1
    
if cant>0:
    promedio=sum/cant
else:
    promedio=0

print("Cantidad de notas:", cant)
print("Promedio notas:", promedio)
print("Cantidad de notas bajas de 4.0:", notas_baja)
print("Cantidad de notas mayores o iguales a 4.0:", notas_altas)