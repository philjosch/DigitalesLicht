class SMBus(object):
    def __init__(self, port):
        self.__port = port
        pass
    def write_byte(self, address, data):
        print(self.__port, hex(address), bin(data)[2:].zfill(8))
