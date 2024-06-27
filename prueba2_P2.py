precios_clp = []
usd_clp = 950
for d in range(10):
    precio_clp = input("Ingrese el precio del producto " + str(d+1) + " en CLP: ")
    precios_clp.append(int(precio_clp))
precios_usd = []
for precio_clp in precios_clp:
    precio_usd = precio_clp / usd_clp
    precios_usd.append(str(precio_usd))
print("Precios en USD:")
for d in range(10):
    print("Producto " + str(d+1) + ": USD " + precios_usd[d])