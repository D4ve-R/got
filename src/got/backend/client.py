from abc import ABC, abstractmethod

class Client(ABC):

    @abstractmethod
    def __call__(self, data) -> str:
        s = "not implemented"
        print(s)
        return s
