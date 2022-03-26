import RobotController

class AbbController(RobotController.RobotController):
    def __init__(self, robname, model, prdyear, *specs) -> None:
        super().__init__(robname, model, prdyear, *specs)
    
    def move(self, x, y, z, a, b, c):
        print(f"Moved to {x}, {y}, {z}, {a}, {b}, {c} as Abb")

    def jog(self, a1, a2, a3, a4, a5, a6):
        print(f"Jogged with {a1}, {a2}, {a3}, {a4}, {a5}, {a6} as Abb")