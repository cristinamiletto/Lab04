from stand import Stand, StandPreseExtra, StandPremium, Espositore
from operator import attrgetter

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome=nome
        self.stand_list=[]
        self.espositori_list=[]

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome=nome


    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        with open (file_path, "r", encoding="utf-8") as f:
            righe=f.readlines()
        for riga in righe:
            riga=riga.strip()
            if riga=="":
                continue
            campi=[c.strip() for c in riga.split(",")]
            codice=campi[0]

            # Distinzione in base al prefisso del codice
            if codice.startswith("ST"):
                superificie=campi[1]
                padiglione=campi[2]
                prezzo_base=campi[3]

                if len(campi)==4:
                    #Stand standard
                    stand=Stand(codice, superficie, padiglione, prezzo_base)
                elif len(campi)==5:
                    valore_extra=campi[4]
                    if valore_extra.isdigit():
                        # Stand con prese elettriche aggiuntive
                        stand = StandPreseExtra(codice, superficie, padiglione, prezzo_base, valore_extra)
                    else:
                        # Stand Premium
                        stand = StandPremium(codice, superficie, padiglione, prezzo_base, valore_extra)
                else:
                    continue

                self.stand_list.append(stand)

            elif codice.startswith("ES"):
                if len(campi)>=3:
                    nome=campi[1]
                    cognome=campi[2]
                    espositore=Espositore(codice, nome, cognome)
                    self.espositori_list.append(espositore)


    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_trovato=None
        for s in self.stand_list:
            if s.codice==codice_stand:
                stand_trovato=s
                break
        if stand_trovato is None:
            raise Exception(f"Lo stand {codice_stand} non è presente nel sistema.")

        espositore_trovato=None
        for e in self.espositori_list:
            if e.codice==condice_espositore:
                espositore_trovato=e
                break

        if espositore_trovato is None:
            raise Exception(f"L'espositore {codice_espositore} non è registrato nel sistema.")

        if not stand_trovato.disponibile:
            raise Exception(f"Lo stand {codice_stand} è già occupato.")

        if espositore_trovato.stand_assegnato is not None:
            raise Exception(f"L'espositore {codice_espositore} ha già uno stand assegnato.")

        stand_trovato.espositore = espositore_trovato
        espositore_trovato.stand_assegnato = stand_trovato


    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        return self.espositori_list

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        return sorted(self.stand_list, key=lambda s:s.calcola_prezzo())
