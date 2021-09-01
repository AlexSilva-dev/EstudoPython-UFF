
linha1 = []
linha2 = []
linha1 = [input()]
linha1 = linha1[0].split(" ")
linha1 = list(map(int, linha1))
linha2 = [input()]
linha2 = linha2[0].split()
linha2 = list(map(int, linha2))
nJogador = linha1[0]
turno = linha1[1]
jogador = 0
pontos = []
pontosF = []
pontosFO = []

for jogador in range(nJogador):
    pontos.append(linha2[jogador::nJogador])
    pontos[jogador] = sum(pontos[jogador])

pontosF = sorted(pontos, reverse=True)
pontosFO = pontos[::-1]

nElementos = len(pontos)
lugar = pontosFO.index(pontosF[0])
ganha = nElementos - lugar

print(ganha)
