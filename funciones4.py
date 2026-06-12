def calcular_propina (subtotal, porcentaje):
    monto_propina = subtotal * (porcentaje / 100)
    return monto_propina
def calcular_total(subtotal, propina):
    total = subtotal + propina
    return total
def mostrar_desglose(subtotal, porcentaje):
    #llamamos las variables guardamos lo que retorna el calcular_total
    propina =calcular_propina(subtotal, porcentaje)
    total_a_pagar = calcular_total(subtotal, propina)
    #EL DESGLOSE
    print("========================")
    print(f"Subtotal:   ${subtotal:.2f}")
    print(f"Propina ({porcentaje}%): ${propina:.2f}")
    print(f"Total a pagar: ${total_a_pagar:.2f}")
    print("=========================")
#pedimos los datos
print("Bienvenido")
while True:
    try:
        el_subtotal=float(input("por favor, ingrese el subtotalde de la cuenta: $"))
        if el_subtotal <= 0:
            print("el subtotal no puede ser menor no igual a 0")
        else:
            break
    except ValueError:
        print("dato invalido debe ser numeros")
while True:
    try:
        el_porcentaje=int(input("por favor, ingrese el porcentaje de la cuenta(10/15/20): "))
        if el_porcentaje in (10, 15 ,20):
            break
        else:
            print("error debe ser 10, 15 o 20 porciento")
    except ValueError:
        print("dato invalido debe ser numeros")
mostrar_desglose(el_subtotal, el_porcentaje)