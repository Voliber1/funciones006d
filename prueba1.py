def buscar_mascota (lista_m, nombre_m):
    for i in range (len(lista_m)):
        if lista_m[i]["nombre"] == nombre_m:
            return i #retorna la posicion
    return -1 #se termina el ciclo porque no se encontro nada

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
#datos de lista de mascota
def agregar_mascota (lista_m):
    nombre=input("Ingrese el nombre de su mascota   ")
    correcta = validacion_nombre(nombre)
    if not correcta:
        print("el nombre no puede estar en blanco")
        return
    especie=input("Ingrese la especie de su mascota     ")
    correcta =validacion_especie(especie)
    if not correcta:
        print("solo atendemos perro, gato y ave")
        return
    edad=input("Ingrese la edad de la mascota (solo años)   ")
    correcta = validacion_edad(edad)
    if not correcta:
        print("la edad debe ser un numero entero mayor a cero")
        return
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad":int(edad),
        "vacunada":False
    }
    lista_m.append(mascota)
    print("Mascota agregada correctamente")
#validacion de datos de lista de mascota
def validacion_nombre (name):
    return name.strip() != ""

def validacion_especie (especie):
    especie_validas= ["perro","gato","ave"]
    return especie.strip().lower() in especie_validas

def validacion_edad (edad):
    #isdigit revisa si un string contiene solo digitos osea es un numero 
    return edad.isdigit() and int(edad) > 0

def actualizar_vacunas(lista_m):
    for m in lista_m:
        if m["edad"] >= 1:
            m["vacunada"]=True
        else:
            m["vacunada"]=False

datos_mascota=[]
op = 0
while op !=6:
    mostar_menu()
    op = opciones()

    if op == 1:
        agregar_mascota(datos_mascota)
    elif op == 2:
        print("**** Buscar Mascota ****")
        nom=input("ingrese el nombre de la mascota para buscar: ")
        posicion =buscar_mascota(datos_mascota, nom)
        if posicion != -1:
            m = datos_mascota[posicion]
            print(f"mascota encontrada en la posicion: {posicion}")
            print(f"nombre mascota: {m["nombre"]}")
            print(f"especie mascota: {m["especie"]}")
            print(f"edad mascota: {m["edad"]}")
            print(f"vacunada: {m["vacunada"]}")
        else: 
            print(f"no se encontro la mascora con el nombre: {nom}")
    elif op ==3:
        print("**** Eliminar Mascota ****")
        nom =input("ingrese el nombre de la mascota a eliminar: ")

        if posicion != -1:
            datos_mascota.pop(posicion)
            print("mascota eliminada correctamente")
        else:
            print("la mascota con este nombre no se encuentra registrada")

    elif op ==4:
        #para llamar lista que no retornan datos
        actualizar_vacunas(datos_mascota)
        print("estado actualizado")

    elif op ==5:
        #llamamos a la funcion de las vacunas
        actualizar_vacunas(datos_mascota)
        #mostar sus datos 
        if len(datos_mascota)==0:
            print("no hay mascotas en la lista")
        else:
            print("== lista de mascotas ==")
            for m in datos_mascota:
                print(f"nombre   : {m["nombre"]}")
                print(f"especie  : {m["especie"]}")
                print(f"edad     : {m["edad"]}")
                #varialble para poder cambiar e valor 
                estado ="AL DIA" if m["vacunada"] else "pendiente"
                print(f"estado vacuna: {estado}")
    elif op == 6:
        print("gracias por usar el sistema")
