from collections import defaultdict
from functools import cmp_to_key
from struct import *

# defaultdict.items()

chunkdata = ['TSLW', 1, 12, b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00']
for count in range(len(chunkdata)):
    if count != 3:
        print (count, '-->', chunkdata[count])
    else:
        pluginlist = []
        for i in range(len(chunkdata[count])):
            pluginlist.append(chunkdata[count][i])
            print(chunkdata[count][i])
            print(pluginlist)

colors = ['red', 'green', 'blue', 'yellow']
names = ['raymond', 'rachel', 'matthew']
data = b'\x02\x1d\x00ccbgsfo4001-pipboy(black).esl\x1e\x00ccbgsfo4004-pipboy(camo02).esl'

print ("range len")
while count < len(data):
    print (count)
    numStrings, = unpack('B',data[:1])
    print (count)
    print ("numStrings", numStrings)

#numStrings, = unpack('B',data[:1])
#print ("numStrings", numStrings)
#nameLength, = unpack('H',data[:2])
#print ("nameLength", nameLength)
print ("end range len")

for count in range(len(data)):
    for somechar in range(len(data[count])):
        print (somechar, data[count][somechar])

print ("enumerate")
for count, color in enumerate(colors):
    print (count, '-->', colors[count])

print ("zip")
for name, color in zip(names, colors):
    print (name, '-->', color)

print ("sorted colors")
for color in sorted(colors):
    print (color)

print ("sorted names")
for name in sorted(names):
    print (name)

print ("sorted key len")
print (sorted(colors, key=len))

print ("sum of square")
result = []
for count in range(10):
    s = count ** 2
    result.append(s)
print (sum(result))

for count in range(len(chunkdata)):
    print (count)