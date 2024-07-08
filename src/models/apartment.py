from dataclasses import dataclass


@dataclass
class Apartment:
    """Class for keeping all the information for the apartment"""

    contratto: str
    tipologia: str
    superficie: str
    locali: str
    piano: str
    totale_piani_edificio: str
    posti_auto: str
    disponibilita: str
    altre_caratteristiche: str
    foto: list
    prezzo: str
    spese_condominio: str
    cauzione: str
    comune: str
    indirizzo: str
