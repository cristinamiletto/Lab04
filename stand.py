class Stand:
    """Rappresenta uno stand standard all'interno del Lingotto Fiere"""
    def __init__(self, codice, superficie, padiglione, prezzo_base):
        self.codice=codice
        self.superifice=superficie
        self.padiglione=padiglione
        self.prezzo_base=float(prezzo_base)
        self.espositore=None

    @property
    def disponibile(self):
        return self.espositore.disponibile is None

    def calcola_prezzo(self):
        """Restituisce il prezzo base per lo stand standard"""
        return self.prezzo_base

    def __str__(self):
        stato="Disponibile" if self.disponibile else f"Occupato da {self.espositore.cognome}"
        return f"{self.codice}: Standard | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - {stato}"

    def __repr__(self):
        return self.__str__()


class StandPreseExtra(Stand):
    """Rappresenta uno stand dotato di prese elettriche aggiuntive"""
    def __init__(self, codice, superficie, padiglione, prezzo_base, numero_prese):
        super().__init__(codice, superificie, padiglione, prezzo_base)
        self.numero_prese=numero_prese

    def calcola_prezzo(self):
        return self.prezzo_base*(1+0.07*self.numero_prese)

    def __str__(self):
        stato="Disponibile" if self.disponibile else f"Occuoato da {self.espositore.cognome}"
        return f"{self.codice}: Prese extra | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Prese aggiuntive: {self.numero_prese} - {stato}"

    def __repr__(self):
        return self.__str__()


class StandPremium(Stand):
    """Rappresenta uno stand di tipo premium con posizione speciale"""
    def __init__(self, codice, superficie, padiglione, prezzo_base, posizione):
        super().__init(coide, superificie, padiglione, prezzo_base)
        self.posizione=posizione

    def calcola_prezzo(self):
        #Sovrapprezzo fisso del 30%
        return self.prezzo_base*1.30

    def __str__(self):
        stato="Disponibile" if self.disponibile else f"Occupato da {self.espositore.cognome}"
        return f"{self.codice}: Premium | {self.superficie} mq - Padiglione {self.padiglione} - Prezzo {self.calcola_prezzo():.2f}€ - Posizione: {self.posizione} - {stato}"

    def __repr__(self):
        return self.__str__()


class Espositore:
    """Rappresenta un espositore registrato nel sistema"""
    def __init__(self, codice, nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome
        self.stand_assegnato=None

    def __str__(self):
        stand_info=f"Stand {self.stand_assesgnato.codice} if self.stand"
        return "Espositore {self.codice}: {self.nome} {self.cognome} - {stand_info}"

    def __repr__(self):
        return self.__str__()








