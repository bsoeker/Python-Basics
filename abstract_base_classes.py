from abc import ABC, abstractmethod
from time import sleep


class Stream(ABC):
    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass

    @abstractmethod
    def read(self):
        pass


class MemoryStream(Stream):
    def open(self):
        print("Opening the file...")

    def close(self):
        print("Closing the file")

    def read(self):
        print("Reading from the file")


stream = MemoryStream()
stream.open()
stream.read()
sleep(3)
stream.close()
