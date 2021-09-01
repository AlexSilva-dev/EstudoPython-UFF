'''
teste = 1
enquanto teste != -1 :

    linha1 <- ler # numTotalMe e tamanhoInt
    se ((linha1[0] e linha1[1]) == '0')
        break:
    enquato numTotalMe != cont:
        num <- ler #numeros medidos
        listaA.append(num + numAnt)
        cont += 1
    enquanto cont1 != len(listaA)/tamanhoInt
        media = (listaA[cont1] + listaA[cont1 + tamanhoInt])/tamanhoInt

        se (media > maiorM):
            maiorM = media
        senao se(media < menorM):
            menorM = media

    escreva("Teste", teste)
    escreva(menorM, maiorM)
    escreva()

'''

teste = 1

while(teste != -1):
    linha0 = []
    listaA = [0]
    num = 0
    numAnt = 0
    media = []
    menorM = 2147483647
    maiorM = -2147483647

    linha0 = [input()]
    linha0 = linha0[0].split(" ")
    if((linha0[0] and linha0[1]) == '0'):
        break
    numTotal = int(linha0[0])
    tamanhoInt = int(linha0[1])
    for cont0 in range(numTotal):
        num = int(input())
        listaA.append(num + numAnt)
        numAnt = listaA[cont0 +1]
    percorrer = int((numTotal - tamanhoInt) + 1)
    for cont1 in range(percorrer):
        media.append((listaA[cont1 + (tamanhoInt)] - listaA[cont1])/tamanhoInt) #

    media.sort()
    print("Teste", teste)
    print(int(media[0]), int(media[len(media) -1]) )
    print("")
    teste += 1