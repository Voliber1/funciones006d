def mostrar_ecabezado():
    print("****************************")
    print("**-Sistema de Resgistro Escolar-**")
    print("****************************")
def dato_estudiante():
    nombre=input("ingrese su nombre     ")
    while True:
        try:
            semestre= int(input("ingrese su semestre    "))
            if semestre <1 or semestre > 5:
                print("debe ingresar un semetres de el 1 al 5 ")
            else:
                break
        except ValueError:
            print("dato invalido")
    carrera = input("ingrese su carrera    ")
    rut =input("ingrese su rut     ")
    estudiante={
        "nombre" : nombre,
        "semestre" : semestre,
        "carrera" : carrera,
        "rut" : rut
    }
    return estudiante
def mostrar_ficha(estudiante):
    print(f"Nombre de estudiante {estudiante["nombre"]}")
    print(f"Semestre de estudiante {estudiante["semestre"]}")
    print(f"Carrera de estudiante {estudiante["carrera"]}")
    print(f"Rut de estudiante {estudiante["rut"]}")
datos = dato_estudiante()
mostrar_ecabezado()
mostrar_ficha(datos)