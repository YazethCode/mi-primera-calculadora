while True:

    num1 = int(input("ingresa un numero"))
    num2 = int(input("ingresa otro nume]"))
    operacion = input("sumar restar o multiplicar").lower()

    if operacion == "sumar":
        suma = num1 + num2
        print(f"la suma de {num1} y {num2} es {suma}")
        
    elif operacion == "restar":
        resta = num1 - num2
        print(f"la resta de {num1} - {num2} es {resta}")
        
    elif operacion == "multiplicar":
        multiplicar = num1 * num2 
        print(f"el resultado de {num1} y {num2} es {multiplicar}")
        
    salir = input("quieres salir? si/no?").lower().strip()
    if salir == "si":
        print("nos vemos bro")
        break