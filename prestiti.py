class Prestito:
    def __init__(self, data, idStrumento, cognome, numPrestiti):
        self.codice = f'P{numPrestiti}'
        self.data = data
        self.idStrumento = idStrumento
        self.cognomeAllievo = cognome
    def __str__(self):
        b = f'Prestito: {self.codice} {self.data} {self.idStrumento} {self.cognomeAllievo}'
        return b

