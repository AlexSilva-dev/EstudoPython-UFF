'''
linha0 = ler
linha0 = [ separar elementos]
l = int(linha0[0])
c = int(linha0[1])
m = int(linha0[2])
n = int(linha0[3])

for linha in range(l):
    lista = ler #coluna inteira

    lista[linha] = separar elementos

for linha1 in range(l+1)

    for coluna1 in range(c+1)
    se((linha1 ou coluna1) == 0):
        listaA[linha1][coluna1] = 0
    senao:

        numBaixo = listaA[linha1 - 1][coluna1]
        numAnte = listaA[linha1][coluna1 - 1]
        numRepe = listaA[linha1 - 1][coluna1 - 1]
        numLista = lista[linha1 - 1][coluna1 - 1]

        soma = numLista + numBaixo + numAnte - numRepe
        listaA[linha1][coluna1] = soma

for linha2 in range(l+1)
    for coluna2 in range(c+1)
        somaCaju = listaA[m + linha2][n + coluna2] - listaA[linha2][n + coluna2] - listaA[m + linha2][coluna2] + listaA[linha2][coluna2]
        listaS.append(somaCaju)

listaS.sort()
escrever(listaS[0])
'''

def separar(listaSe):
    listaSe = listaSe.split(" ")
    return listaSe

linha0 = []
matriz = []


linha0 = input()
linha0 = separar(linha0)

l = int(linha0[0])
c = int(linha0[1])
m = int(linha0[2])
n = int(linha0[3])

for line0 in range(l):
    matriz.append(input())
    matriz[line0] = separar(matriz[line0])

#for line1 in range(l)
print(matriz)