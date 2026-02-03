#Clase DATA que representa una fecha con día, mes y año.

class DATA:



    def __init__(self,dia,mes,ano):
        self.setd(dia)
        self.setm(mes)
        self.seta(ano)

    def setd(self, dia):
        if dia <= 1 or dia > 31:
            raise ValueError("El día debe estar entre 1 y 31")
        self.dia = dia

    def setm(self, mes):
        if mes <= 1 or mes > 12:
            raise ValueError("El mes debe estar entre 1 y 12")
        self.mes = mes

    def seta(self, ano):
        if ano <= 0:
            raise ValueError("El año debe ser mayor que 0")
        self.ano = ano

    def getd(self):
        return self.dia

    def getm(self):
        return self.mes

    def geta(self):
        return self.ano

    def validezdiames (self,dia,mes,ano):

        if mes == 2:
            if ano%4 == 0:
                if dia <= 29:
                    return True
            else:
                if dia <= 28:
                    return True
        elif mes % 2 == 0:
            if dia <= 30:
                return True
        elif dia <= 31:
            return True





