entrada = [input()]
entrada = entrada[0].split(" ")
xM = int(entrada[0])
yM = int(entrada[1])
xD = int(entrada[2])
yD = int(entrada[3])
#print(xD, yD, xM, yM)

difX = (xM - xD)
difY = (yM - yD)
if(difY<0):
    difY = difY * (-1)
if(difX<0):
    difX = difX * (-1)

print( difY + difX)