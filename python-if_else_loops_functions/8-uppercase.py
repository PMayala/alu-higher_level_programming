#!/usr/bin/python3
def uppercase(str):
    strord = []
    ucase = ""

    for i in range(len(str)):
        strord.append(ord(str[i]))
        if (strord[i] >= 97) and (strord[i] <= 122):
            strord[i] = chr(strord[i] - 32)
        else:
            strord[i] = chr(strord[i])
        ucase += strord[i]
    print("{}".format(ucase))
