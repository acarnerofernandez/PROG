from itertools import count
from random import triangular

Ej = int(input("Escoge un ejercicio "))

#while Ej > 5:
#   Ej = int(input("Solo hay 5 ejercicios, escoge otro ejercicio "))

if Ej == 1:

  #Escribir un ciclo definido para imprimir por pantalla tódolos números entre	10 e 20
 t = 9
 for i in range (10+1):
  t = t + 1
 print (t)

if Ej == 2:
 #Escribir un programa que converta un valor dado en grados Fahrenheit a grados Celsius. Recordade que a fórmula para a conversión é: F = 9/5 * C + 32.

 F = float(input("Ingresa la temperatura en Fahrenheit: "))

 C = (F - 32) * 5/9

 print ("Temperatura en Celsius: ", C)


if Ej == 3:
#Utiliza o programa anterior para xerar unha táboa de conversión de temperaturas, dende 0º F ata 120º F, de 10 en 10.

 F = 0
 i = 0
 for i in range (12+1):
     C = (F - 32) * 5/9
     print ( F, "=", C)
     F = F+10

if Ej == 4:
#Escribir un programa que imprima tódolos números pares entre dous números que se lle pidan o usuario.

 num1 = int(input("Ingresa un numero: "))
 num2 = int(input("Ingresa un numero: "))

 i = num1
 for i in range (num1,num2+1):
     nump = i%2
     if nump == 0:
         print (i)

if Ej == 5:
#Escribir un programa que reciba un número n por parámetro e imprima os primeiros n números triangulares, xunto co seu índice. Os números triangulares obteñense mediante a suma dos números naturales dende 1 ata n. É dicir, si se piden os primeros 5 números triangulares, o programa debe imprimir:

 numero = int(input("Ingresa un numero: "))

 def triangular(numero):
     for i in range (1, numero + 1):
        i = numero*(numero+1)/2
     return i
 print (triangular(numero))


if Ej == 6:
#Escribir un programa que tome unha cantidade m de valores ingresados polo usuario, a cada un lle calcule o factorial e imprima o resultado xunto co número de orden correspondiente.

 cantidad = int(input("¿Cuántos valores quieres ingresar? "))

 for orden in range(1, cantidad + 1):
    numero = int(input("Introduce el valor: "))

    factorial = 1
    for i in range(1, numero + 1):
        factorial *= i
    print("número: ", numero, " -> factorial = ", factorial)


if Ej == 7:
#Escribir un programa que imprima por pantalla tódalas fichas de dominó, de unha por liña e sen repetir.

