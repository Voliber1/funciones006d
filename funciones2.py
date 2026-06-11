def convertir_nota(puntaje, puntaje_total):
    nota= (puntaje * 6 /puntaje_total) + 1
    return round(nota, 1)
#pedir datos
while True:
    try:
        p=float(input("ingrese su puntaje   "))
        if p < 0:
            print("error el  puntaje np puede ser negativa")
        else:
            break
    except ValueError:
        print("dato invalido debe ser numeros")
while True:
    try:
        pt=float(input("ingrese el puntaje final de la evaluacion   "))
        if pt <= 0:
            print("error el puntaje no puede ser negativa")
        else:
            break
    except ValueError:
        print("dato invalido debe ser numeros")

calificacion=convertir_nota(p, pt)
print(f"la calificacion en escala chilena es: {calificacion}")