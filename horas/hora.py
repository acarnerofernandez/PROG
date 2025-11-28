class horas:
    def __init__(self, horas, minutos,segundos):
        self.hora = horas
        self.minuto = minutos
        self.segundo = segundos

    def sethoras(self,horas):
        self.hora = horas % 24

    def gethoras(self):
        return self.hora

    def setmin(self,minutos):
        self.minuto = minutos % 60

    def getmin(self,):
        return self.minuto

    def setsec(self,segundos):
        self.segundo = segundos % 60

    def getsec(self):
        return self.segundo


    def incrementarsec(self, massec):
        total = self.segundo + massec
        self.segundo = total % 60
        masmin = (self.minuto + total // 60)
        self.minuto = (self.minuto + total // 60) % 60
        self.hora = (self.hora + masmin // 60) % 24

    def incrementarmin(self, masmin):
        total = self.minuto + masmin
        self.minuto = total % 60
        self.hora = (self.hora + total // 60) % 24



    def incrementarh(self, mash):
        self.hora = (self.hora + mash) % 24

    def mostrarformato12h(self):

        sufijo = "AM"
        h = self.hora

        if h == 0:
             h = 12
        elif h == 12:
                sufijo = "PM"
        elif h > 12:
              h -= 12
              sufijo = "PM"

        return h, ":", self.minuto, ":", self.segundo, sufijo