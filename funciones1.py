#funciones
def datos_productos(name, stock, price):
    print("=============================")
    print(f"|| Nombre del producto {name}  ||")
    print(f"|| Precio del producto {price} ||")
    print(f"|| Stock del producto  {stock} ||")
    print("=============================")
#solicitar datos
nombre = input("Ingrese el nombre de el producto    ")
while True:
    try:
        stock = int(input("Ingrese el Stock de el producto  "))
        if stock <= 0:
            print("error ingreso un dato invalido debe ser mayor a 0")
        else:
            break
    except ValueError:
        print("Erro ingreso datos invalidos")
while True:
    try:
        precio = int(input("Ingrese el precio de el producto     "))
        if precio < 0:
            print("error ingreso un dato invalido debe ser 0 o mayor")
        else:
            break
    except ValueError:
        print("error")
#llamar funcion
datos_productos(nombre,stock,precio)