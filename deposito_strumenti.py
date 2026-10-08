from strumenti import Strumento
from prestiti import Prestito
import csv
from operator import attrgetter

class DepositoStrumenti:

    def __init__(self, nome, responsabile):
        """Inizializza gli attributi e le strutture dati"""
        self.nome = nome
        self.responsabile = responsabile
        self.datiStrumenti = []
        self.listaPrestiti = []

        self.contatorePrestiti = 1

    def carica_file_strumenti(self, file_path):
        """Carica gli strumenti dal file"""
        #devo ancora valutare le eccezioni
        filein = open(file_path, "r")
        infile = csv.reader(filein)
        for line in infile:
            self.datiStrumenti.append(Strumento(line[0], line[1], line[2], line[3], line[4]))
        filein.close()


    def aggiungi_strumento(self, tipo, marca, anno_acquisto, valore):
        """Aggiunge uno strumento nel deposito: aggiunge solo nel sistema e non aggiorna il file"""
        n = len(self.datiStrumenti)
        codice = f'S{n + 1}'
        nuovoStrumento = Strumento(codice, tipo, marca, anno_acquisto, valore)
        self.datiStrumenti.append(nuovoStrumento)
        return nuovoStrumento


    def strumenti_ordinati_per_marca(self):
        """Ordina gli strumenti per marca in ordine alfabetico"""
        self.datiStrumenti.sort(key=attrgetter('marca'))
        return self.datiStrumenti

    def nuovo_prestito(self, data, id_strumento, cognome_allievo):
        """Crea un nuovo prestito"""
        nuovoPrestito = Prestito(data, id_strumento, cognome_allievo, self.contatorePrestiti)
        self.contatorePrestiti += 1
        self.listaPrestiti.append(nuovoPrestito)
        return nuovoPrestito

        # TODO

    def termina_prestito(self, id_prestito):
        """Termina un prestito in atto"""
        # TODO
        for el in self.listaPrestiti:
            if el.codice == id_prestito:
                self.listaPrestiti.remove(el)
                return el
        return None

