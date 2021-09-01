

opcao = [input()]
opcao = opcao[0].split(" ")
opcao = [int(i) for i in opcao]
o1 = opcao[0]
o2 = opcao[1]
o3 = opcao[2]
opMaior = sorted(opcao, reverse=True)

if((o1 == o2) or (o1 == o3) or (o2 == o3)):
    print("S")

elif(opMaior[0] == (opMaior[1] + opMaior[2] )):
    print("S")

else:
    print("N")

