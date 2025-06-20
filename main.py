from mathematics import add, multiplicar;

if __name__=='__main__':
    print("Main program, para ayudarte con las matees")
    accion = input("¿Qué quieres hacer? 's' para sumar, 'm' para multiplicar \n ")

    num1 = int(input("Nº 1: "))
    num2 = int(input("Nº 2: "))
    if accion == 's':
        print(add(num1, num2))

    if accion == 'm':
        result = multiplicar(num1, num2)
        print(f"El resultado es {result}")