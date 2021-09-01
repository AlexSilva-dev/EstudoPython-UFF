

entrada = []

entrada.append(input())
entrada = entrada[0].split(" ")
entrada = [float(i) for i in entrada]

r3A = 10/entrada[2]
r3G = 10/entrada[3]

precoA = r3A * entrada[0]
precoG = r3G * entrada[1]

if(precoA < precoG):
    print("A")

elif(precoA > precoG):
    print("G")
else:
    print("G")