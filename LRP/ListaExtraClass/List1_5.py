
cartas = [input()]
cartas = cartas[0].split(" ")
cartas = [int(i) for i in cartas]

crescente = sorted(cartas)
decrescente = crescente[::-1]
print(cartas)
print(crescente)
print(decrescente)
if(cartas == crescente):
    print("C")

elif(cartas == decrescente):
    print("D")

else:
    print("N")