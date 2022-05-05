def operaciones(numero1, numero2, operacionRealizar):
    resultado = None
    if operacionRealizar == 1:
        resultado = numero1 + numero2
    elif operacionRealizar == 2:
        resultado = numero1 - numero2
    elif operacionRealizar == 3:
        resultado = numero1 * numero2
    elif operacionRealizar == 4:
        resultado = numero1 / numero2
    else:
        resultado = 'Error'
    return  resultado

num1 = input('Escribe el primer numero: ')
num2 = input('Escribe el segundo numero: ')

operacion = input('Elija una operacion de la siguiente lista:\n1 = Sumar\n2 = Restar\n3 = Multiplicar\n4 = Dividir\n')


if num1.isnumeric() and num2.isnumeric() and operacion.isnumeric():
    operacion = int(operacion)
    # if 0 < operacion <= 4:
    if operacion > 0 and operacion <= 4:
        num1 = float(num1)
        num2 = float(num2)
        print(operaciones(num1, num2, operacion))
    else:
        print('Error')
        exit()
else:
    print('Error, solo se permite el ingreso de numeros')