print("Datos")
Nombre = input("¿Cual es tu nombre? : ")
Edad =int(input("¿Cual es tu edad? :"))
Edad2 = Edad+ 5
print("Tu edad en 5 años mas sera:", Edad2)
print("")
MiListadefrutas = ["Pera" ,"Manzana" ,"Piña","Naranja","kiwi"]
print(MiListadefrutas)
print("La tercera fruta de la lista es",MiListadefrutas[2])
print("")
numero = int(input("Introduce un número entero: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")
