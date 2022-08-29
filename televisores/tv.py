class TV:
    numTV=0
    def __init__(self,marca,estado):
        self.marca=marca
        self.estado=estado
        self._canal=1
        self._precio=500
        self._volumen=1
        self.control=None
        TV.numTV+=1

    @classmethod
    def setNumTV(cls,numTV):
        cls.numTV=numTV
    @classmethod
    def getNumTV(cls):
        return cls.numTV
    
    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca
    
    def setControl(self,control):
        self.control=control
    def getControl(self):
        return self.control
    
    def setPrecio(self,precio):
        self._precio=precio
    def getPrecio(self):
        return self._precio
    
    def setVolumen(self,volumen):
        if volumen>=0 and volumen<=7 and self.estado== True:
            self._volumen=volumen
    def getVolumen(self):
        return self._volumen

    def setCanal(self,canal):
        if canal>=0 and canal<=7 and self.estado== True:
            self._canal=canal
    def getCanal(self):
        return self._canal

    def getEstado(self):
        return self.estado
    
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado ==True and self._canal <120:
            self._canal+=1
    def canalDown(self):
        if self.estado ==True and self._canal >1:
            self._canal-=1

    def volumenUp(self):
        if self.estado ==True and self._volumen <7:
            self._volumen+=1
    def volumenDown(self):
        if self.estado ==True and self._volumen >=1:
            self._volumen-=1