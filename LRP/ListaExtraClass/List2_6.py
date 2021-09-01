
quebrados = 0
band = int(input())

for _ in range(band):
    lc = [input()]
    lc = lc[0].split(" ")
    lc = [int(i) for i in lc]
    if(lc[0] > lc[1]):
        quebrados = quebrados + lc[1]

print(quebrados)
