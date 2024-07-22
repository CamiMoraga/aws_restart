
n1 = float(input("Introduce el primer número: "))
n2 = float(input("Introduce el segundo número: "))

if n1 > 0 and n2 > 0:
    print("Ambos números son positivos.")
elif n1 > 0 and n2 <= 0:
    print("Solo el primer numero es positivo.")
elif n1 <= 0 and n2 > 0:
    print("Solo el segundo número es positivo.")
else:
    print("Ninguno de los dos números es positivo.")

edad =int(input("¿Cual es tu edad? :"))
identificacion = input("¿Tienes identificación? (responde 'si' o 'no'): ")

if edad >= 18 and identificacion == "si":
    print("Puede votar")
    
else:
    print("No puede votar")
    

    
    
    

