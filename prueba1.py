def mostar_menu ():
    print("===============================")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar mascota")
    print("6.- Salir")
    print("===============================")
datos_mascota=[]
def opciones ():
    while True:
        try:
            opcion=int(input("Ingrese la opcion "))
            if opcion in (1,2,3,4,5,6):
                break
            else:
                print("No puede ingresar numeros negativos ni no registrados")
        except ValueError:
            print("Error solo ingrese numeros del 1 al 6")
    if opcion == 1:
        while True:
            nombre=input("Ingrese el nombre de su mascota   ")
            if len(nombre) <= 0 or nombre not in " ":
                break
            else:
                print("Error no ingreso nada o uso espacios")
        while True:
            especie=input("Ingrese la especie de su mascota     ").lower()
            if especie in ("perro", "gato", "ave"):
                break
            else:
                print("Error las especie solo pueden ser, perro, gato y ave")
        while True:
            try:
                edad=int(input("Ingrese la edad de la mascota (solo años)   "))
                if edad <= 0:
                    print("no podemos atender mascotas con menos de un año")
                else:
                    vacuna=input("Esta vacunado (si/no)     ").lower()
                    if vacuna == "si":
                        break
                    else:
                        print("")
            except ValueError:
                print("Error ingreso de datos no validos solo numeros")
                
op = 0
while op !=6:
    mostar_menu()
    op = opciones()