



def ejercicio1():

 i = 0
 lista = []

 while i != 7:
  c = int(input("Dime la temperatura media del dia "))
  lista.append(c)
  i = i+1

 print(lista)

def ejercicio2():

 stem = 0
 temp = 0
 lista = [20,25,19,18,15,18,20]


 for temp in lista:
     stem =  stem + temp

 mtemp = stem/7

 print (mtemp)

def ejercicio3():

    stem = 0
    temp = 0
    lista = [20, 25, 19, 18, 15, 18, 20]
    dias = 0
    i = 0

    for temp in lista:
        stem = stem + temp

    mtemp = stem / 7

    while i != len(lista):
        if lista[i] > mtemp:
         dias = dias + 1
         i = i + 1
        else:
         i = i + 1

    print("hay ", dias, " que se supera la media de temperatura")


def ejercicio4():

    lista = [20, 25, 19, 18, 15, 18, 20]
    temperatura = int(input("Temperatura de corte: "))
    i = 0
    for temp in lista:
     i = i + 1

     if temp > temperatura:

         if i == 1:
             dia = "lunes"
             print (dia, temp)
         elif i == 2:
             dia = "martes"
             print(dia, temp)
         elif i == 3:
             dia = "miercoles"
             print(dia, temp)
         elif i == 4:
             dia = "jueves"
             print(dia, temp)
         elif i == 5:
             dia = "viernes"
             print(dia, temp)
         elif i == 6:
             dia = "sabado"
             print(dia, temp)
         elif i == 7:
             dia = "domingo"
             print(dia, temp)



ejercicio = input("Ingresa ejercicio: ")

if ejercicio == "1":
    print(ejercicio1())
elif ejercicio == "2":
    print(ejercicio2())
elif ejercicio == "3":
    print(ejercicio3())
elif ejercicio == "4":
    print(ejercicio4())