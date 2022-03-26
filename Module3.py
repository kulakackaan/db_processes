apx = ""
ref = ""
with open("Deneme1.txt", "r") as f:
    for s in f:
        if s.startswith("m1F") == True:
            if s.startswith("m1F_Aapx") == True:
                apx = s
            if s.startswith("m1F_Aref") == True:
                ref = s
with open("Deneme2.txt", "w") as f:
    f.write(apx)
    for s in range(4):
        if s==0:
            continue
        deneme1 = ref
        deneme2 = ref
        d1 = str((s * 10) + 1)
        d2 = str((s * 10) + 2)
        str1 = "m1F_A" + d1
        str2 = "m1F_A" + d2
        deneme1 = deneme1.replace("m1F_Aref", str1)
        deneme2 = deneme2.replace("m1F_Aref", str2)
        f.write(deneme1)
        f.write(deneme2)
