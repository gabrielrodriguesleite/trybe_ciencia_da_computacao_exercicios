from abc import ABC, abstractmethod


class ManipuladorDeLog(ABC):
    @abstractmethod
    def log(self):
        pass


class LogEmArquivo(ManipuladorDeLog):
    def log(self, message):
        print("log em arquivo")


class LogEmTela(ManipuladorDeLog):
    def log(self, message):
        print("log em tela")
