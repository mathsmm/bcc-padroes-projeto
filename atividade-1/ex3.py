from abc import ABC, abstractmethod


# Comp é Comportamento
class DefinirValorComportamento(ABC):
    @abstractmethod
    def definirValor(self, comodos, espaco, localizacao):
        pass

class DefinirValorComEdificacao(DefinirValorComportamento):
    def __init__(self) -> None:
        super().__init__()

    def definir_valor(self, comodos, espaco, localizacao):
        if localizacao == 'A':
            return (espaco * 3000) + (comodos * 1000)
        elif localizacao == 'B':
            return (espaco * 1000) + (comodos * 1000)
        elif localizacao == 'C':
            return (espaco * 500) + (comodos * 1000)

class DefinirValorSemEdificacao(DefinirValorComportamento):
    def definirValor(self, comodos, espaco, localizacao):
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
    def __init__(self) -> None:
        super().__init__()

class Apartamento(Imovel):
    def __init__(self) -> None:
        super().__init__()

class Terreno(Imovel):
    def __init__(self) -> None:
        super().__init__()

def main():
    dv1 = DefinirValorComEdificacao()
    dv2 = DefinirValorSemEdificacao()

    b1 = Bateira()
    b1.set_comp_navegacao(cn1)

    b2 = Iate()
    b2.set_comp_navegacao(cn1)

    b3 = Canoa()
    b3.set_comp_navegacao(cn2)

    b4 = Jangada()
    b4.set_comp_navegacao(cn2)

    b5 = BarcoAVela()
    b5.set_comp_navegacao(cn3)

    print("Comportamento da Bateira")
    print("efetuar_navegar: ", end="")
    b1.efetuar_navegar()
    print()

    print("Comportamento do Iate")
    print("efetuar_navegar: ", end="")
    b2.efetuar_navegar()
    print()

    print("Comportamento da Canoa")
    print("efetuar_navegar: ", end="")
    b3.efetuar_navegar()
    print()

    print("Comportamento da Jangada")
    print("efetuar_navegar: ", end="")
    b4.efetuar_navegar()
    print()

    print("Comportamento do Barco à Vela")
    print("efetuar_navegar: ", end="")
    b5.efetuar_navegar()
    print()


if __name__ == "__main__":
    main()