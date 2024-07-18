def digitos(num):
    return len(str(num))

num = int(input("Ingrese un valor: "))

print("El número que ingreso tiene ", digitos(num), "dígitos.")