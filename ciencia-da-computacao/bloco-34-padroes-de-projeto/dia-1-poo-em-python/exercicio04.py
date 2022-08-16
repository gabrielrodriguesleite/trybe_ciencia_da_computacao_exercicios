# Polimorfismo

from abc import ABC, abstractmethod


class ManipuladorDeLog(ABC):
    @abstractmethod
    def log(self):
        raise NotImplementedError


class LogEmArquivo(ManipuladorDeLog):
    def log(self, message):
        print("log em arquivo: ", message)


class LogEmTela(ManipuladorDeLog):
    def log(self, message):
        print("log em tela: ", message)


class Log():
    def __init__(self) -> None:
        self.manipuladores = []

    def adicionar_manipulador(self, manipulador):
        if manipulador not in self.manipuladores:
            self.manipuladorer.push(manipulador)

    def info(self, message):
        for m in self.manipuladores:
            m.log(message)

    def alerta(self, message):
        for m in self.manipuladores:
            m.log(message)

    def erro(self, message):
        for m in self.manipuladores:
            m.log(message)

    def debug(self, message):
        for m in self.manipuladores:
            m.log(message)
