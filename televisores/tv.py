from control import Control
from marca import Marca
class TV: 
    _canal=1
    _precio=500
    _volumen=1
    control= Control
    _marca=Marca
    numTV=0
    def __init__(self,marca:Marca,estado):
        self.marca=marca
        self.estado=estado
        
        
        self.numTV+=1
    
    def setMarca(self,marca):
        self.marca=marca
    def getMarca(self):
        return self.marca
    
    def setControl(self,control):
        self.control=control
    def getControl(self):
        return self.control
    
    def setPrecio(self,precio):
        self.precio=precio
    def getPrecio(self):
        return self.precio
    
    def setVolumen(self,volumen):
        if volumen>=0 and volumen<=7 and self.estado== True:
            self.volumen=volumen
    def getVolumen(self):
        return self.volumen

    def setCanal(self,canal):
        if canal>=0 and canal<=7 and self.estado== True:
            self.canal=canal
    def getCanal(self):
        return self.canal

    def getEstado(self):
        return self.estado
    
    def turnOn(self):
        self.estado = True
    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado ==True and self.canal <120:
            self.canal+=1
    def canalDown(self):
        if self.estado ==True and self.canal >1:
            self.canal-=1

    def volumenUp(self):
        if self.estado ==True and self.volumen <7:
            self.volumen+=1
    def volumenDown(self):
        if self.estado ==True and self.volumen >=1:
            self.volumen-=1