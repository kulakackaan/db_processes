with open("Deneme1.txt", "r") as f:
    Rows = f.read()
    print(Rows)

with open("Deneme1.txt", "r") as f:
    Rows = f.readline()
    print(Rows)
    Rows = f.readline()
    print(Rows)

with open("Deneme2.txt", "r") as f:
    Rows = f.read()
    print(Rows)
