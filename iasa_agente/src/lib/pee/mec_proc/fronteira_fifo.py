from .fronteira import Fronteira


class FronteiraFIFO(Fronteira):
    def inserir(self, no):
        self.nos.insert(0, no)
