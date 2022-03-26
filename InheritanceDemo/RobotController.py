class RobotController():
    _robname = ""

    def __init__(self, robname, model, prdyear, *specs) -> None:
        self._robname = robname
        self.model = model
        self.prdyear = prdyear
        self.specs = specs
    
    @property
    def robname(self):
        return self._robname

    @robname.setter
    def robname(self, value):
        self._robname = value

    def move(self, x, y, z, a, b, c):
        pass

    def jog(self, a1, a2, a3, a4, a5, a6):
        pass
