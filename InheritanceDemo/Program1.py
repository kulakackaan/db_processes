from KukaController import KukaController as Controller

rob1 = Controller("rob89", "irb4600", 2015, ["new", "fast", "light"])

rob1.move(10, 20, 30, 90, 180, -90)
print(rob1.robname)
print(rob1._robname)
rob1.jog(10, 20, 30, 40, 50, 60)
