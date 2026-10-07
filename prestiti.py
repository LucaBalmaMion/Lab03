class Prestito:
    def __init__(self, data, idStrumento, cognome, numPrestiti):
        self.codice = f'P{Prestito.numPrestiti}'
        self.data = data
        self.idStrumento = idStrumento
        self.cognomeAllievo = cognome
        self.listaPrestiti = []
    def nuovo_prestito(self, data, idStrumento, cognome):
        self.codice = f'P{Prestito.numPrestiti}'
        self.data = data
        self.idStrumento = idStrumento
        self.cognomeAllievo = cognome
        prestito = [self.codice, self.data, self.idStrumento, self.cognomeAllievo]
        self.listaPrestiti.append(prestito)
        Prestito.numPrestiti += 1
        return prestito
