
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


def leer_opcion():
    opcion = input("Elige una opción: ")
    while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 6:
        print("Opción inválida. Debes ingresar un número entre 1 y 6.")
        opcion = input("Elige una opción: ")
    return int(opcion)


# FUNCIONES DE VALIDACIÓN (solo dicen si el dato es válido o no)

def validar_huesped(nombre):
    return nombre.strip() != ""


def validar_habitacion(habitacion):
    return habitacion.isdigit() and int(habitacion)>=1 and int(habitacion) <= 200


def validar_noches(noches):
    return noches.isdigit() and int(noches) > 0


# OPCIÓN 1: AGREGAR RESERVA


def agregar_reserva(reservas):
    huesped = input("Nombre del huésped: ")
    validacion=validar_huesped(huesped)
    if not validacion:
        print("Error: el nombre del huésped no puede estar vacío.")
        return

    habitacion = input("Número de habitación (1-200): ")
    validacion=validar_habitacion(habitacion)
    if not validacion:
        print("Error: la habitación debe ser un número entero entre 1 y 200.")
        return

    noches = input("Cantidad de noches: ")
    validacion=validar_noches(noches)
    if not validacion:
        print("Error: las noches deben ser un número entero mayor que cero.")
        return

    nueva_reserva = {
        "huesped": huesped,
        "habitacion": int(habitacion),
        "noches": int(noches),
        "confirmada": False
    }
    reservas.append(nueva_reserva)
    print("Reserva agregada con éxito.")

# OPCIÓN 2: BUSCAR RESERVA

def buscar_reserva(reservas, nombre):
    for i in range(len(reservas)):
        if reservas[i]["huesped"] == nombre:
            return i
    return -1


def opcion_buscar(reservas):
    nombre = input("Nombre del huésped a buscar: ")
    posicion = buscar_reserva(reservas, nombre)

    if posicion != -1:
        reserva = reservas[posicion]
        print(f"Reserva encontrada en la posición {posicion}:")
        print(f"Huésped: {reserva['huesped']}")
        print(f"Habitación: {reserva['habitacion']}")
        print(f"Noches: {reserva['noches']}")
    else:
        print(f"La reserva del huésped '{nombre}' no se encuentra registrada.")


# OPCIÓN 3: ELIMINAR RESERVA


def eliminar_reserva(reservas):
    nombre = input("Nombre del huésped cuya reserva deseas eliminar: ")
    posicion = buscar_reserva(reservas, nombre)

    if posicion != -1:
        reservas.pop(posicion)
        print("Reserva eliminada con éxito.")
    else:
        print(f"La reserva del huésped '{nombre}' no se encuentra registrada.")


# OPCIÓN 4: CONFIRMAR RESERVAS

def confirmar_reservas(reservas):
    for reserva in reservas:
        if reserva["noches"] >= 2:
            reserva["confirmada"] = True
        else:
            reserva["confirmada"] = False


# OPCIÓN 5: MOSTRAR RESERVAS

def mostrar_reservas(reservas):
    confirmar_reservas(reservas)  # primero actualiza el estado de todas
    print("=== LISTA DE RESERVAS ===")
    for reserva in reservas:
        estado = "CONFIRMADA" if reserva["confirmada"] else "PENDIENTE"
        print(f"Huésped: {reserva['huesped']}")
        print(f"Habitación: {reserva['habitacion']}")
        print(f"Noches: {reserva['noches']}")
        print(f"Estado: {estado}")
        print("*" * 45)

# PROGRAMA PRINCIPAL

def main():
    reservas = []  # la colección general empieza vacía
    opcion = 0

    while opcion != 6:
        mostrar_menu()
        opcion = leer_opcion()

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

main()