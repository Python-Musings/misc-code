from struct import unpack

class ByteReader:
  def __init__(self, data):
    self.data = data
    self.offset = 0

  def __getitem(self, index):
    return self.data[index]

  def __len__(self):
    return len(self.data)

  def read(self, n=-1):
    if n < 0:
      self.offset = len(self.data)
    if self.offset >= len(self.data):
      return None
    data = self.data[self.offset:self.offset + n]
    self.offset += n
    return data

data = b'\x02\x1d\x00ccbgsfo4001-pipboy(black).esl\x1e\x00ccbgsfo4004-pipboy(camo02).esl'
data = ByteReader(data)

numStrings, = unpack('B', data.read(1))
print("numStrings:", numStrings)
for count in range(numStrings):
    print('nameLength:', nameLength)

