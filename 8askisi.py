import random

ranList = [random.randint(-30, 31) for i in range(30)]

zeroTriplets = []

for x in ranList:
    for y in ranList:
        for z in ranList:
            if x + y + z == 0 and [x, y, z] not in zeroTriplets:
                zeroTriplets.append([x, y, z])

if len(zeroTriplets) != 0:
    for triplet in zeroTriplets:
        print triplet
    print "\n", len(zeroTriplets), "triplets with a sum of zero found!"
else:
    print "\n There are no triplets with a sum of zero!"
