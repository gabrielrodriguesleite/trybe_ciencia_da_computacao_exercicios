from abc import ABC, abstractmethod


class ManipuladorDeLog(ABC):
    @abstractmethod
    def log(self):
        raise NotImplementedError


class LogEmArquivo(ManipuladorDeLog):
    def log(self, message):
        print("log em arquivo")


class LogEmTela(ManipuladorDeLog):
    def log(self, message):
        print("log em tela")
