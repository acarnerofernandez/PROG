from hora import horas

t = horas(int(input("hora")), int(input("minuto")), int(input("segundo")))
t.incrementarsec(int(input("suma segundos")))
t.incrementarmin(int(input("añade minutos")))
t.incrementarh(int(input("añade  horas")))

print(t.gethoras(), t.getmin(), t.getsec())

print(t.mostrarformato12h())
