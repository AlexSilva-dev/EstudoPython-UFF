'''


'''


def separarint(linhas):
    linhas = linhas[0].split(" ")
    linhas = [int(i) for i in linhas]
    return linhas

linha1 = [input()]
linha1 = separarint(linha1)
linha2 = [input()]
linha2 = separarint(linha2)

#variaveis
nJogador = linha1[0]
turno = linha1[1]
jogador = 0
pontos = []
pontosF = []
cont = 0
pontosFO = []

for jogador in range(nJogador):
    pontos.append(linha2[jogador::nJogador])
for cont in range(nJogador):
    pontosF.append(sum(pontos[cont]))


pontosFO = sorted(pontosF,reverse=True)
#maiorP = pontosFO[0]
pontosF2 = pontosF[::-1]
ganhador = (len(pontosF) - pontosF2.index(pontosFO[0]))
print(ganhador)