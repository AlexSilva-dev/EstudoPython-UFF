

nota = int(input())
# colocar o 0 no final
if((nota >= 1) & (nota <= 35)):
    print("D")

elif((nota >= 36) & (nota <= 60)):
    print("C")

elif((nota >= 61) & (nota <= 85)):
    print("B")

elif((nota >= 86) & (nota <= 100)):
    print("A")

else:
    print("E")