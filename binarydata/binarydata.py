from struct import *

def get_names(raw_data):
    i = 0
    offset = 1
    name_list = []
    num_strings, = unpack('B', raw_data[:1])
    while i < num_strings:
        name_len, = unpack('H', raw_data[offset:offset + 2])
        offset += 2
        name_data = raw_data[offset:offset + name_len]
        offset += name_len
        name_list.append(name_data.decode())
        i += 1
    return name_list


def pack_names(names):
    numFileNames = len(names)
    print "count :", numFileNames
    dataBuff = []
    dataBuff.append(pack('B',numFileNames))
    for count in xrange(numFileNames):
        lenFileName = len(names[count])
        arrayFileName = names[count]
        print "lenFileName", lenFileName
        print "arrayFileName", arrayFileName
        dataBuff.append(pack('H',lenFileName))
    print "dataBuff", dataBuff

data = b'\x02\x1d\x00ccbgsfo4001-pipboy(black).esl\x1e\x00ccbgsfo4004-pipboy(camo02).esl'
names = get_names(data)
print(names)
pack_names(names)