from Data import DATA

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
ano = int(input("Introduce el año: "))

fecha = DATA(dia, mes, ano)

resultado = fecha.validezdiames(dia, mes, ano)

if resultado == True:
    print("La fecha es válida")
else:
    print("Fecha inválida:", resultado)
