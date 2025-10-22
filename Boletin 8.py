ejercicio = input("Ingresa ejercicio: ")


if ejercicio == "1":
#Escribir unha función que reciba unha tupla de elementos e indique si se encontran ordeados de menor a maior ou non.
 num1 = int(input("Ingresa tu numero: "))
 num2 = int(input("Ingresa tu numero: "))
 num3 = int(input("Ingresa tu numero: "))
 num4 = int(input("Ingresa tu numero: "))

 numeros = (num1, num2, num3, num4)

 if numeros == tuple(sorted(numeros)):
  print("Esta ordenado de menor a maior: ")
 elif numeros == tuple(sorted(numeros,reverse=True)):
    print("Esta ordenado de maior a menor: ")
 else:
    print("No esta ordenado: ")

elif ejercicio == "2":
#Escribir unha función que indique si duas fichas de dominó encaixan ou non. As fichas son recibidas en duas tuplas, por exemplo: (3,4) e (5,4). A función

 num1 = int(input("Ingresa numero 1 ficha 1: "))
 num2 = int(input("Ingresa numero 2 ficha 1: "))
 num3 = int(input("Ingresa numero 1 ficha 2: "))
 num4 = int(input("Ingresa numero 2 ficha 2: "))

 ficha1 = (num1, num2)
 ficha2 = (num3, num4)

 if ficha1 == ficha2:
    print("Se puede unir ")
 elif ficha1[0] == ficha2[0]:
    print("Se puede unir ")
 elif ficha1[1] == ficha2[1]:
  print("Se puede unir: ")
 elif ficha1[0] == ficha2[1]:
     print("Se puede unir ")
 elif ficha1[1] == ficha2[0]:
     print("Se puede unir ")
 else:
     print("No se puede unir ")

elif ejercicio == "3":
#Escribir unha función que reciba unha tupla con nomes e para cada nome imprima unha mensaxe ‘Estimado don/dona Nome’

 nombres = ("Amapola", "Pepe", "Juan", "Maria")
 i = 0
 while i != len(nombres):
    print("Estimado don/dona", nombres[i])
    i = i + 1

elif ejercicio == "4":
#Escribir unha función que reciba unha tupla con nomes, unha posición de orixen p e unha cantidade n, e imprima a mensaxe anterior (exercicio 3)
# para os n nombres que se encontran a partires da posición p.

 nombres = ("Amapola", "Pepe", "Juan", "Maria", "Amir", "Manuel", "Miguel", "Andres")
 i = int(input("Ingresa donde quieres empezar: ")) -1
 n = int(input("Ingresa cuantos nombres "))

 while n != 0:
    print("Estimado don/dona", nombres[i])
    i = i + 1
    n = n - 1

elif ejercicio == "5":
#Modificar as funcións anteriores para que teñan en conta o xénero do destinatario, para elo, deberán recibir unha tupla de tuplas, contendo o nome e o xénero, adaptando a mensaxe con ‘don’ ou ‘dona’ dependendo deste.

 nombres = ("Amapola", "Pepe", "Juan", "Maria", "Amir", "Manuel", "Miguel", "Andres")
 i = int(input("Ingresa donde quieres empezar: ")) -2
 n = int(input("Ingresa cuantos nombres "))

 while n != 0:
  n = n - 1
  i = i + 1
  if nombres[i].endswith(("a")):
    print ("Estimada dona", nombres[i])
  else:
    print ("Estimado don: ", nombres[i])

