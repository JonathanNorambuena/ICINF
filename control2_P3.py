palabras = []
contador = 0

while True:
    palabra = input("Ingresa una palabra (para salir no ponga nada y presione enter): ")
    if palabra == "":
        break
    palabras[contador:contador] = [palabra]
    contador = contador + 1

if contador == 0:
    print("No se ingreso ninguna palabra.")
else:
    palabra_larga = palabras[0]
    caracteres_largos = 0
    for n in range(contador):
        caracteres_palabra = 0
        for caracter in palabras[n]:
            caracteres_palabra = caracteres_palabra + 1
        if caracteres_palabra > caracteres_largos:
            palabra_larga = palabras[n]
            caracteres_largos = caracteres_palabra
    print("La palabra con la mayor cantidad de caracteres es '" + palabra_larga + "' con " + str(caracteres_largos) + " caracteres.")