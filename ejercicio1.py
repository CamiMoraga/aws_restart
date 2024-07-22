"""
 
----  Calculadora automática de 2 números ----
 
Vamos a solicitar al usuario 2 números
y a realizar todas las operaciones posibles (+, -, *, /, //, %, **)
mostrando los resultados de una forma clara
 
"""

print("Operaciones")
num = int(input("Ingresa el primer número: ")) 
num2 = int(input("Ingresa el segundo número: "))
suma = num + num2
resta = num - num2
multiplicacion = num * num2
division = num / num2
print("")
print("El resultado de cada Operacion es:")
print(f"La suma de {num} y {num2} es {suma}")
print(f"La resta de {num} y {num2} es {resta}")
print(f"La multiplicación de {num} y {num2} es {multiplicacion}")
print(f"La división de {num} y {num2} es {division}")
