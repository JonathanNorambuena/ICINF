nombres=[]
for i in range(7):
    nombre=input("Ingrese un nombre: ")
    nombres.append(nombre)

con_a=[]
for nombre in nombres:
    if nombre[-1]=="a":
        con_a.append(nombre)

nombres=con_a

print("Lista despues de la eliminaion de nombres que no terminen en a:")
print(nombres)