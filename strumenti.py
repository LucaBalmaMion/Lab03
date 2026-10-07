class Strumento:
    def __init__(self, codice, nome, marca, anno, prezzo):
        self.codice = codice
        self.nome = nome
        self.marca = marca
        self.anno = anno
        self.prezzo = prezzo
    def __str__(self):
        a = f'{self.codice} {self.nome} {self.marca} {self.anno} {self.prezzo}'
        return a