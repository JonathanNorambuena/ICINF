def es_binario(var):
    for n in var:
        if n != '0' and n != '1':
bin = input("Ingrese una cadena: ")

if es_binario(bin):
    print(True)
else:
    print(False)