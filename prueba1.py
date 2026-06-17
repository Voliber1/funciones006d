def mostar_menu ():
    print("===============================")
    print("1.- Agregar mascota")
    print("2.- Buscar mascota")
    print("3.- Eliminar mascota")
    print("4.- Marcar como vacunada")
    print("5.- Mostrar mascota")
    print("6.- Salir")
    print("===============================")
def opciones ():
    while True:
        try:
            opcion=int(input("Ingrese la opcion "))
            if opcion <=0 or opcion > 6:
                print("No puede ingresar numeros negativos ni no registrados") 
                
            else:
                return opcion
                
        except ValueError:
            print("Error solo ingrese numeros del 1 al 6")

def agregar_mascota (lista_m):
    nombre=input("Ingrese el nombre de su mascota   ")
    correcta = agregar_mascota(nombre)
    if not correcta:
        print("el nombre no puede estar en blanco")
        return
    especie=input("Ingrese la especie de su mascota     ").lower()
    correcta =agregar_mascota(especie)
    if not correcta:
        print("solo atendemos perro, gato y ave")
        return
    edad=input("Ingrese la edad de la mascota (solo años)   ")
    correcta = agregar_mascota(edad)
    if not correcta:
        print("la edad debe ser un numero entero mayor a cero")
        return
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower,
        "edad":int(edad),
        "vacunada":False
    }
    lista_m.append(mascota)
    print("Mascota agregada correctamente")
def validacion_nombre (name):
    return name.strip() != ""

def validacion_especie (especie):
    especie_validas= ["perro","gato","ave"]
    return especie.strip().lower() in especie_validas

def validacion_edad (edad):
    #isdigit revisa si un string contiene solo digitos osea es un numero 
    return edad.isdigit() and int(edad) > 0
datos_mascota=[]
op = 0
while op !=6:
    mostar_menu()
    op = opciones()

    if op ==1:
        agregar_mascota(datos_mascota)
    elif op ==2:
        print()
    elif op ==3:
        print()
    elif op ==4:
        print()
    elif op ==5:
        print()
