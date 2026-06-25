
# FUNCIONES DEL MENÚ

def mostrar_menu():
    print("======== MENÚ PRINCIPAL ========")
    print("1. Agregar reserva")
    print("2. Buscar reserva")
    print("3. Eliminar reserva")
    print("4. Confirmar reservas")
    print("5. Mostrar reservas")
    print("6. Salir")
    print("=================================")

# SELECCION DE OPCION

def opcion():
    op=int(input("Seleccione una opcion"))
    while not op.isdigit() or int(op) < 1 or int(op) > 6:
        print("Opción inválida. Debes ingresar un número entre 1 y 6.")
        op = input("Elige una opción: ")
    return int(opcion)

# OPCION NUMERO 1

def agregar_reserva(lista_m):
    huesped=input("Ingrese su nombre")
    numero_habitacion=input("Ingrese el numero de habitacion")
    noches=input("Ingrese la cantidad de noches que desea")

# Validaciones

def validacion_nombre(huesped):
    return huesped.strip() != ""

def validacion_habitacion(numero_habitacion):
    return numero_habitacion.isdigit() and int(numero_habitacion) >= 1 and int(numero_habitacion) <= 200

def validacion_noches(noches):
    return noches.isdigit() and int(noches) > 0

#opion numero 2

def buscar_reserva(lista_m, nombre):
    for i in range (len(lista_m)):
        if lista_m[i]["nombre"]:
            return i
    return -1

def opcion_buscar(lista_m):
    nombre = input("Nombre del huésped a buscar: ")
    posicion = buscar_reserva(lista_m, nombre)

    if posicion != -1:
        reserva = lista_m[posicion]
        print(f"Reserva encontrada en la posición {posicion}:")
        print(f"Huésped: {reserva['huesped']}")
        print(f"Habitación: {reserva['habitacion']}")
        print(f"Noches: {reserva['noches']}")
    else:
        print(f"La reserva del huésped '{nombre}' no se encuentra registrada.")

#Opcion 3

def eliminar_reserva(lista_m):
    nombre=input("ingrese el nombre de la reserva que desea eliminar")
    posicion=buscar_reserva(lista_m, nombre)

  
    if posicion != -1:
        posicion.pop[lista_m]
        print("resera eliminada")
    else:
        print("reserva no encontrada")

#opcion 4

def confirmar_reserva(lista_m):
    for reserva in lista_m:
        if reserva["noches"] >= 2:
            reserva["confirmado"] = True
        else:
            reserva["confirmado"] = False


#opcion 5

def mostrar_reservas(lista_m):
    confirmar_reserva(lista_m)  # primero actualiza el estado de todas
    print("=== LISTA DE RESERVAS ===")
    for reserva in lista_m:
        estado = "CONFIRMADA" if reserva["confirmada"] else "PENDIENTE"
        print(f"Huésped: {reserva['huesped']}")
        print(f"Habitación: {reserva['habitacion']}")
        print(f"Noches: {reserva['noches']}")
        print(f"Estado: {estado}")
        print("*" * 45)


def main():
    reserva = []  # la colección general empieza vacía
    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = opcion()

        if opcion == 1:
            agregar_reserva(reservas)
        elif opcion == 2:
            opcion_buscar(reservas)
        elif opcion == 3:
            eliminar_reserva(reservas)
        elif opcion == 4:
            confirmar_reservas(reservas)
            print("Reservas confirmadas correctamente.")
        elif opcion == 5:
            mostrar_reservas(reservas)
        elif opcion == 6:
            print("Gracias por usar el sistema. Vuelva Pronto")
main