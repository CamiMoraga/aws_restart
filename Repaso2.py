Edad =int(input("¿Cual es tu edad? :"))
if Edad >= 18:
    print("Puede votar")
else:
    print("No puede votar")

print("")
temperatura = float(input("Introduce la temperatura en grados Celsius: "))

if temperatura <= 0:
    print( {temperatura},"grados Celsius, el agua está en estado sólido (hielo).")
elif temperatura > 0 and temperatura < 100:
    print({temperatura},"grados Celsius, el agua está en estado líquido.")
else:
    print({temperatura},"grados Celsius, el agua está en estado gaseoso (vapor).")
print("")
numero = int(input("Introduce un número entero: "))

if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")