from struct import *

def unpack_names(raw_data):
  offset = 1
  name_list = []
  num_names, = unpack('B', raw_data[:1])

  for i in range(num_names):
    name_length, = unpack('H', raw_data[offset : offset + 2])
    name_data = raw_data[offset + 2 : offset + 2 + name_length]
    offset = offset + 2 + name_length
    name_list.append(name_data.decode())

  return name_list

def pack_names(name_list):
  raw_data = b''
  num_names = len(name_list)
  raw_data += pack('B', num_names)

  for name in name_list:
    name_length = len(name)
    raw_data += pack('H', name_length)
    raw_data += name.encode()

  return raw_data

enc_data = b'\x02\x1d\x00ccbgsfo4001-pipboy(black).esl\x1e\x00ccbgsfo4004-pipboy(camo02).esl'
dec_data = ['ccbgsfo4001-pipboy(black).esl', 'ccbgsfo4004-pipboy(camo02).esl']

print(unpack_names(enc_data))
print(pack_names(dec_data))