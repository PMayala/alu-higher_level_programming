#!/usr/bin/python3
def no_c(my_string):
    strord = []
    newstr = ""

    for i in range(len(my_string)):
        strord.append(ord(my_string[i]))

    for i in range(len(strord)):
        if strord[i] == 67 or strord[i] == 99:
            continue
        newstr += chr(strord[i])

    pstr = "{}".format(newstr)
    return pstr
