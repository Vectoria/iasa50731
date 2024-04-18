from .fronteira import Fronteira


class FronteiraLIFO(Fronteira):
    """
    Fronteira que o recebe um item no fim e elimina o primeiro

    Args:
        Fronteira (Fronteira): extend
    """

    def inserir(self, no):

        self.nos.append(no)
