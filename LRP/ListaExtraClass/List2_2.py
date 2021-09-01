

carta = [input()]
carta = carta[0].split(" ")
carta = [int(i) for i in carta]

if(carta[0] != carta[1]):

    if(carta[0] > carta[1]):
        print(carta[0])
    else:
        print(carta[1])

else:
    print(carta[0])

