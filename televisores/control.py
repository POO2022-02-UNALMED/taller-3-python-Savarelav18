from tv import TV
class Control:
    _tv = TV

    def turnOn(self):
        self.tv.turnOn()
    def turnOff(self):
        self.tv.turnOff()

    def canalUp(self):
        self.tv.canalUp()
    def canalDown(self):
        self.tv.canalDown()

    def volumenUp(self):
        self.tv.volumenUp()
    def volumenDown(self):
        self.tv.volumenDown()
    
    def enlazar(self,tv:TV):
        self.tv=tv
        self.tv.setControl(self)