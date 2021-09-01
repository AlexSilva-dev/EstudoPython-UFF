

testes = 1
while(testes != 0):
    a = 0
    b = 0

    n = int(input())
    if(n == 0):
        break

    for _ in range(n):
        jogo = []
        jogo.append(input())
        jogo = jogo[0].split(" ")
        jogo = [int(i) for i in jogo]
        if(jogo[0] != jogo[1]):
            if(jogo[0] > jogo[1]):
                a = a + 1
            else:
                b = b + 1
    print(a, b)

