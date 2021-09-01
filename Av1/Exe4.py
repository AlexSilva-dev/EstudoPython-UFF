
a = int(0)
b = 0

a = int(input())
b = int(input())
c = int(input())
a1 = a * 2
b1 = b * 2
c1 = c * 2
rA = int((c1 + c1) + b1)
rB = int(a1 + c1)
rC = int((a1 + a1) + b1)

'''
if((a == 30) and (b == 10) and (c == 20)):
    print(100)
else:
'''
if(rA < rB) and (rA < rC ):
    print(rA)
elif((rB < rA) and (rB < rC)):
    print(rB)
elif((rC < rA) and (rC < rB)):
    print(rC)
elif((rA == rB) or (rA == rC)):
    print(rA)
elif((rB == rC)):
    print(rB)
