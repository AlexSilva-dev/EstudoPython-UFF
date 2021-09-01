'''
n = int(1)
cont = 0
cont1 = 1
enquanto ( n != 0 ):
    n <- ler
    se ( n == 0):
        break
    sequencia[] <- ler e separar para por na lista

    enquanto(cont != len(sequencia)):
        se ( sequencia[cont] == cont):
            escreva("Teste ", cont1)
            escreva(sequencia[cont])
            break
        cont++
    cont1++

'''
n = int(1)
cont = 1
cont1 = 0
while (n != 0):
    cont1 = 0
    sequencia = []
    n = int(input())
    if(n == 0):
        break
    sequencia.append(input())
    sequencia = sequencia[0].split(" ")
    sequencia = [int(i) for i in sequencia]
    #print(sequencia)
    while(cont1 != len(sequencia)):
        if(sequencia[cont1] == (cont1 + 1)):
            print("Teste",cont)
            print(sequencia[cont1])
            print()
            break
        cont1+= 1
    cont+= 1