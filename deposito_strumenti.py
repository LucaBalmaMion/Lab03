from strumenti import strumento
import csv
from operator import attrgetter

class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.datiStrumenti = []

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        #devo ancora valutare le eccezioni
        filein = open(file_path, "r")
        infile = csv.reader(filein)
        for line in infile:
            self.datiStrumenti.append(strumento(line[0], line[1], line[2], line[3], line[4]))
        filein.close()


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        n = len(self.datiStrumenti)
        codice = f'S{n + 1}'
        nuovo = strumento(codice, tipo, marca, anno_acquisto, valore)
        self.datiStrumenti.append(nuovo)
        return nuovo


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        self.datiStrumenti.sort(key=attrgetter('marca'))
        return self.datiStrumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        prima = True
        if prima:
            numPrestiti = 1
            prima = False
        else:
            numPrestiti += 1

        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
