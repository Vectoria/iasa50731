from .fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    """
    Fronteira que o recebe um item no inicio e elimina o primeiro

    Args:
        Fronteira (Fronteira): extend
    """

    def inserir(self, no):
        self.nos.insert(0, no)
