# Imports ---------------------------------------------------------------------
import struct
import io

path = 'Save70_A3AA8A36M4C696C6C79_Commonwealth_010659_20170908034503_16_2.f4se'


class FileReader(io.FileIO):
    """File-object with convenience reading functions."""

    def unpack(self, fmt):
        return struct.unpack(fmt, self.read(struct.calcsize(fmt)))

    def readUByte(self): return struct.unpack('B', self.read(1))[0]
    def readUInt16(self): return struct.unpack('H', self.read(2))[0]
    def readUInt32(self): return struct.unpack('I', self.read(4))[0]

    def readByte(self): return struct.unpack('b', self.read(1))[0]
    def readInt16(self): return struct.unpack('h', self.read(2))[0]
    def readInt32(self): return struct.unpack('i', self.read(4))[0]

    def readSig(self): return struct.unpack('4s', self.read(4))[0]
    def readString8(self): return self.read(struct.unpack('B', self.read(1))[0])
    def readString16(self): return self.read(struct.unpack('H', self.read(2))[0])
    def readString32(self): return self.read(struct.unpack('I', self.read(4))[0])

def unpack_names(raw_data):
    offset = 1
    name_list = []
    num_names, = struct.unpack('B', raw_data[:1])

    for i in range(num_names):
        name_length, = struct.unpack('H', raw_data[offset : offset + 2])
        name_data = raw_data[offset + 2 : offset + 2 + name_length]
        offset = offset + 2 + name_length
        name_list.append(name_data.decode())

    return name_list

def pack_names(name_list):
    raw_data = b''
    num_names = len(name_list)
    raw_data += struct.pack('B', num_names)

    for name in name_list:
        name_length = len(name)
        raw_data += struct.pack('H', name_length)
        raw_data += name.encode()

    return raw_data

def read_chunk(file):
    chunk_type = FileReader.readSig(file).decode("utf-8")
    chunk_version = FileReader.readInt32(file)
    chunk_length = FileReader.readInt32(file)
    chunk_data = file.read(chunk_length)
    chunk_value = []
    chunk_value.append(chunk_type)
    chunk_value.append(chunk_version)
    chunk_value.append(chunk_length)
    chunk_value.append(chunk_data)
    if chunk_type == 'SDOM':
        print (unpack_names(chunk_data))
    elif chunk_type == 'DOML':
        print (unpack_names(chunk_data))
    else:
        print (chunk_value)
    return chunk_value

def read_chunks(file):
    opcode_base = FileReader.readInt32(file)
    num_chunks = FileReader.readInt32(file)
    plugin_length = FileReader.readInt32(file)
    chunkBlock = []
    for x in range(num_chunks):
        chunkBlock.append(read_chunk(file))
    return chunkBlock


def main():
    """Main function, fires everything off."""
    cosave_file = open(path,'rb')
    signature = FileReader.readSig(cosave_file).decode("utf-8")
    format_version = FileReader.readInt32(cosave_file)
    obse_version = FileReader.readInt16(cosave_file)
    obse_minor_version = FileReader.readInt16(cosave_file)
    oblivion_version = FileReader.readInt32(cosave_file)
    num_plugins = FileReader.readInt32(cosave_file)

    print ("Signature: ", signature)
    print ("format_version: ", format_version)
    print ("obse_version : ", obse_version)
    print ("obse_minor_version: ", obse_minor_version)
    print ("oblivion_version: ", oblivion_version)
    print ("num_plugins: ", num_plugins)
    for x in range(num_plugins):
        read_chunks(cosave_file)
    cosave_file.close()

if __name__=='__main__':
    main()