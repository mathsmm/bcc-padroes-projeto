from abc import ABC, abstractmethod


# Comp é Comportamento
class DefinirValorComportamento(ABC):
    @abstractmethod
    def definir_valor(self, comodos, espaco, localizacao) -> float:
        pass

class DefinirValorComEdificacao(DefinirValorComportamento):
    def definir_valor(self, comodos, espaco, localizacao):
        if localizacao == 'A':
            return (espaco * 3000) + (comodos * 1000)
        elif localizacao == 'B':
            return (espaco * 1000) + (comodos * 1000)
        elif localizacao == 'C':
            return (espaco * 500) + (comodos * 1000)

class DefinirValorSemEdificacao(DefinirValorComportamento):
    def definir_valor(self, comodos, espaco, localizacao):
        if localizacao == 'A':
            return (espaco * 1500)
        elif localizacao == 'B':
            return (espaco * 750)
        elif localizacao == 'C':
            return (espaco * 200)


class Imovel(ABC):
    def __init__(self, comodos, espaco, localizacao) -> None:
        self.__comodos = comodos
        self.__espaco = espaco
        self.__localizacao = localizacao

        self.__definir_valor_comp: DefinirValorComportamento = None

    def definir_valor(self):
        self.__definir_valor_comp.definir_valor(self.__comodos, self.__espaco, self.__localizacao)

    def set_definir_valor(self, definir_valor_comp: DefinirValorComportamento):
        self.__definir_valor_comp = definir_valor_comp

class Casa(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

class Apartamento(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

class Terreno(Imovel):
    def __init__(self, comodos, espaco, localizacao) -> None:
        super().__init__(comodos, espaco, localizacao)

def main():
    dv1 = DefinirValorComEdificacao()
    dv2 = DefinirValorSemEdificacao()

    i1 = Casa(5, 100, 'A')
    i1.set_definir_valor(dv1)

    i2 = Casa(8, 150, 'C')
    i2.set_definir_valor(dv1)

    i3 = Apartamento(4, 35, 'B')
    i3.set_definir_valor(dv1)

    i4 = Apartamento(8, 200, 'A')
    i4.set_definir_valor(dv1)

    i5 = Terreno(0, 500, 'B')
    i5.set_definir_valor(dv2)

    i6 = Terreno(0, 1000, 'C')
    i6.set_definir_valor(dv2)

    print("Comportamento da Casa 1")
    print(f"definir_valor: {i1.definir_valor()}")
    print()

    print("Comportamento do Casa 2")
    print(f"definir_valor: {i2.definir_valor()}")
    print()

    print("Comportamento da Apartamento 1")
    print(f"definir_valor: {i3.definir_valor()}")
    print()

    print("Comportamento da Apartamento 2")
    print(f"definir_valor: {i4.definir_valor()}")
    print()

    print("Comportamento do Terreno 1")
    print(f"definir_valor: {i5.definir_valor()}")
    print()

    print("Comportamento do Terreno 2")
    print(f"definir_valor: {i6.definir_valor()}")
    print()

if __name__ == "__main__":
    main()