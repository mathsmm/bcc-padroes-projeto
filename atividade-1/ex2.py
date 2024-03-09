from abc import ABC, abstractmethod


# Comp é Comportamento
class CompNavegacao(ABC):
    @abstractmethod
    def navegar():
        pass

class CompNavegaComMotor(CompNavegacao):
    def navegar():
        print("Navegando com motor.")

class CompNavegaComRemos(CompNavegacao):
    def navegar():
        print("Navegando com remos.")

class CompNavegaComVelas(CompNavegacao):
    def navegar():
        print("Navegando com velas.")


class Barco():
    