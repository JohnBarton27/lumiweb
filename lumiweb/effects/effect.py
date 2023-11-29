from abc import ABC, abstractmethod

class Effect(ABC):

    def __init__(strip):
        self.strip = strip

    @abstractmethod
    def run():
        pass
    