
maior = int(input())
opera = [input()]
opera = opera[0].split(" ")
p = int(opera[0])
q = int(opera[2])

if(opera[1] == "+"):
    resul = p + q
else:
    resul = p * q

if(resul>maior):
    print("OVERFLOW")

else:
    print("OK")