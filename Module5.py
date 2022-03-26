def PTP(PointName: str, ToolNum: int, BaseNum: int, PdatName: str, FdatName: str):
    str1a = ";FOLD PTP " + PointName
    str1b = " CONT Vel=100 % " + PdatName + " "
    str1c = "Tool[" + str(ToolNum) + "]:Tool" + str(ToolNum) + " Base[" + str(BaseNum) + "]:m" + str(BaseNum)
    str1d = ";%{PE}%R 8.3.38,%MKUKATPBASIS,%CMOVE,%VPTP,%P 1:PTP, 2:" + FdatName
    str1e = ", 3:, 5:100, 7:" + PdatName + "\n"
    str2 = "$BWDSTART=FALSE\n"
    str3 = "PDAT_ACT=P" + PdatName + "\n"
    str4 = "FDAT_ACT=F" + FdatName + "\n"
    str5 = "BAS(#PTP_PARAMS,100)\n"
    str6 = "PTP X" + PointName + "\n"
    str7 = ";ENDFOLD\n"
    mystr = str1a + str1b + str1c + str1d + str1e + str2 + str3 + str4 + str5 + str6 + str7
    return mystr




with open("Kaan.txt", "w") as f:
    for s in range(1,4):
        namestr1 = "A" + str(s) + "1"
        namestr2 = "A" + str(s) + "2"
        f.write(PTP(namestr1, 1, 1, "PDAT1", "m1"))
        f.write(PTP(namestr2, 1, 1, "PDAT1", "m1"))
        f.write("\n")






