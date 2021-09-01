

linha1 = [input()]
linha1 = linha1[0].split(" ")
linha1 = [int(i) for i in linha1]

d = linha1[0]
e = linha1[0]
f = linha1[0]
for _ in range(linha1[1]):

    oper = [input()]
    oper = oper[0].split(" ")

    if(len(oper) == 3): #
        oper[2] = int(oper[2])
        if(oper[0] == "C"):

            if(oper[1] == "D"):
                d = d - oper[2]
            elif(oper[1] == "E"):
                e = e - oper[2]
            else:
                f = f - oper[2]


        elif (oper[0] == "V"):

            if (oper[1] == "D"):
                d = d + oper[2]
            elif (oper[1] == "E"):
                e = e + oper[2]
            else:
                f = f + oper[2]

    else:
        oper[3] = int(oper[3])
        if(oper[1] == "D"):
            if(oper[2] == "E"):
                d = d + oper[3]
                e = e - oper[3]
            elif(oper[2] == "F"):
                d = d + oper[3]
                f = f - oper[3]
        elif(oper[1] == "E"):
            if(oper[2] == "D"):
                e = e + oper[3]
                d = d - oper[3]
            else:
                e = e + oper[3]
                f = f - oper[3]
        else:
            if(oper[2] == "D"):
                f = f + oper[3]
                d = d - oper[3]
            else:
                f = f + oper[3]
                e = e - oper[3]

print(d, e, f)

