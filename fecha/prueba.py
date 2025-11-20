from Data import DATA

dia = int(input("Introduce el día: "))
mes = int(input("Introduce el mes: "))
ano = int(input("Introduce el año: "))

fecha = DATA(dia, mes, ano)

resultado = fecha.validezdiames(fecha.getd(), fecha.getm(), fecha.geta())

if resultado == True:
    print("La fecha es válida")
    print("Día:", fecha.getd())
    print("Mes:", fecha.getm())
    print("Año:", fecha.geta())
else:
    print("Fecha inválida:", resultado)
