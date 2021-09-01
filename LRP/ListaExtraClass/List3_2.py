

def serparar(linha):
    linha = linha[0].split(" ")
    linha = [int(i) for i in linha]
    return linha

ret1 = [input()]
ret1 = serparar(ret1)
ret2 = [input()]
ret2 = serparar(ret2)
print(ret1, '\n', ret2)

x_ret1 = ret1[0]
y_ret1 = ret1[1]
x2_ret1 = ret1[2]
y2_ret1 = ret1[3]

x_ret2 = ret2[0]
y_ret2 = ret2[1]
x2_ret2 = ret2[2]
y2_ret2 = ret2[3]

