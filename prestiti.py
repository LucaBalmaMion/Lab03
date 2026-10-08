class Prestito:
    def __init__(self, data, idStrumento, cognome, numPrestiti):
        self.codice = f'P{numPrestiti}'
        self.data = data
        self.idStrumento = idStrumento
        self.cognomeAllievo = cognome
        singoloPrestito = [self.codice, self.data, self.idStrumento, self.cognomeAllievo]
        self.listaPrestiti.append(singoloPrestito)
        return singoloPrestito
    def __str__(self):
        b = f'Prestito: {self.codice} {self.data} {self.idStrumento} {self.cognomeAllievo}'

