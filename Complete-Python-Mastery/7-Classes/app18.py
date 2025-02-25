from abc import ABC, abstractmethod


class InvalidOperationError(Exception):
    pass


class Stream(ABC):

    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream is already opened")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream is already closed")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network")


# class MemoryStream(Stream):
#     pass

class MemoryStream(Stream):
    def read(self):
        print("Reading data from a memory stream.")


# stream = Stream()
# stream.open()

# NameError: name 'Stream' is not defined

# before defining the read method inside the MemoryStream class
# memory_stream = MemoryStream()
# memory_stream.open()
# TypeError: Can't instantiate abstract class MemoryStream without an implementation for abstract method 'read'
