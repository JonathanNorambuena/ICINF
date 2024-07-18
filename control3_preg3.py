def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp > 0:
        return num * potencia(num, exp - 1)
    else:
        return 1/potencia(num, -exp)
        
print(potencia(4,3))
print(potencia(1,0))
print(potencia(5,1))
print(potencia(10,2))
print(potencia(1,3))