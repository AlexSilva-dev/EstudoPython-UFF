


teste = int(1)
while (teste != -1):
    n = int(input())
    if(n == -1):
        break

    papel = (4 ** n) + (2 ** (n+1)) + 1
    print("Teste", teste)
    print(papel,'\n')
    teste = teste + 1

