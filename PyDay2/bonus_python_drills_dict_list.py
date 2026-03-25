from __future__ import annotations

from copy import deepcopy
from datetime import date


# =========================
# Aufgabe 1: Videoverleih
# =========================

VIDEOTHEK = {
    "filme": [
        {
            "id": 1,
            "titel": "Matrix",
            "jahr": 1999,
            "genre": ["Sci-Fi", "Action"],
            "ausgeliehen": False,
            "ausleiher": None,
            "bewertungen": [8, 9, 10, 7, 8],
        },
        {
            "id": 2,
            "titel": "Der Herr der Ringe: Die Gefaehrten",
            "jahr": 2001,
            "genre": ["Fantasy", "Abenteuer"],
            "ausgeliehen": True,
            "ausleiher": {
                "name": "Max Mustermann",
                "kundennummer": 12345,
                "ausleihdatum": "2025-05-10",
                "rueckgabedatum": "2025-05-17",
            },
            "bewertungen": [10, 9, 10, 8, 9],
        },
        {
            "id": 3,
            "titel": "Inception",
            "jahr": 2010,
            "genre": ["Sci-Fi", "Action", "Thriller"],
            "ausgeliehen": False,
            "ausleiher": None,
            "bewertungen": [9, 8, 7, 10, 9],
        },
    ],
    "kunden": [
        {
            "kundennummer": 12345,
            "name": "Max Mustermann",
            "email": "max@example.com",
            "telefon": "0123456789",
            "ausgeliehene_filme": [2],
        },
        {
            "kundennummer": 67890,
            "name": "Erika Musterfrau",
            "email": "erika@example.com",
            "telefon": "9876543210",
            "ausgeliehene_filme": [],
        },
    ],
}


def _finde_film(videothek: dict, film_id: int) -> dict:
    for film in videothek["filme"]:
        if film["id"] == film_id:
            return film
    raise ValueError(f"Film mit ID {film_id} nicht gefunden.")


def _finde_kunde(videothek: dict, kundennummer: int) -> dict:
    for kunde in videothek["kunden"]:
        if kunde["kundennummer"] == kundennummer:
            return kunde
    raise ValueError(f"Kunde mit Kundennummer {kundennummer} nicht gefunden.")


def film_hinzufuegen(videothek: dict, titel: str, jahr: int, genre: list[str]) -> dict:
    neue_id = max((film["id"] for film in videothek["filme"]), default=0) + 1
    neuer_film = {
        "id": neue_id,
        "titel": titel,
        "jahr": jahr,
        "genre": genre,
        "ausgeliehen": False,
        "ausleiher": None,
        "bewertungen": [],
    }
    videothek["filme"].append(neuer_film)
    return neuer_film


def film_ausleihen(
    videothek: dict,
    film_id: int,
    kundennummer: int,
    ausleihdatum: str,
    rueckgabedatum: str,
) -> dict:
    film = _finde_film(videothek, film_id)
    kunde = _finde_kunde(videothek, kundennummer)

    if film["ausgeliehen"]:
        raise ValueError(f"Film '{film['titel']}' ist bereits ausgeliehen.")

    film["ausgeliehen"] = True
    film["ausleiher"] = {
        "name": kunde["name"],
        "kundennummer": kundennummer,
        "ausleihdatum": ausleihdatum,
        "rueckgabedatum": rueckgabedatum,
    }
    kunde["ausgeliehene_filme"].append(film_id)
    return film


def film_zurueckgeben(videothek: dict, film_id: int) -> dict:
    film = _finde_film(videothek, film_id)
    if not film["ausgeliehen"]:
        raise ValueError(f"Film '{film['titel']}' ist nicht ausgeliehen.")

    kundennummer = film["ausleiher"]["kundennummer"]
    kunde = _finde_kunde(videothek, kundennummer)
    if film_id in kunde["ausgeliehene_filme"]:
        kunde["ausgeliehene_filme"].remove(film_id)

    film["ausgeliehen"] = False
    film["ausleiher"] = None
    return film


def filme_nach_genre(videothek: dict, gesuchtes_genre: str) -> list[dict]:
    return [
        film
        for film in videothek["filme"]
        if gesuchtes_genre.lower() in (genre.lower() for genre in film["genre"])
    ]


def durchschnittsbewertung(videothek: dict, film_id: int) -> float:
    film = _finde_film(videothek, film_id)
    bewertungen = film["bewertungen"]
    if not bewertungen:
        return 0.0
    return sum(bewertungen) / len(bewertungen)


def top_bewertete_filme(videothek: dict, anzahl: int = 3) -> list[dict]:
    return sorted(
        videothek["filme"],
        key=lambda film: durchschnittsbewertung(videothek, film["id"]),
        reverse=True,
    )[:anzahl]


# =========================
# Aufgabe 2: Schulverwaltung
# =========================

SCHULE = {
    "klassen": {
        "10A": {
            "klassenlehrer": "Frau Schmidt",
            "raum": "203",
            "schueler": [
                {
                    "id": 1001,
                    "name": "Lisa Meyer",
                    "geburtsdatum": "2010-03-15",
                    "noten": {
                        "Mathematik": [2, 1, 2],
                        "Deutsch": [1, 2, 1],
                        "Englisch": [1, 1, 2],
                    },
                },
                {
                    "id": 1002,
                    "name": "Tom Schulz",
                    "geburtsdatum": "2009-11-30",
                    "noten": {
                        "Mathematik": [3, 3, 4],
                        "Deutsch": [2, 2, 3],
                        "Englisch": [1, 2, 2],
                    },
                },
            ],
        },
        "10B": {
            "klassenlehrer": "Herr Mueller",
            "raum": "204",
            "schueler": [
                {
                    "id": 1003,
                    "name": "Emma Wagner",
                    "geburtsdatum": "2010-05-22",
                    "noten": {
                        "Mathematik": [1, 1, 1],
                        "Deutsch": [2, 2, 2],
                        "Englisch": [2, 1, 1],
                    },
                }
            ],
        },
    },
    "lehrer": [
        {"id": 101, "name": "Frau Schmidt", "faecher": ["Mathematik", "Physik"]},
        {"id": 102, "name": "Herr Mueller", "faecher": ["Deutsch", "Geschichte"]},
        {"id": 103, "name": "Frau Weber", "faecher": ["Englisch", "Franzoesisch"]},
    ],
}


def _finde_klasse(schule: dict, klasse: str) -> dict:
    if klasse not in schule["klassen"]:
        raise ValueError(f"Klasse {klasse} nicht gefunden.")
    return schule["klassen"][klasse]


def _finde_schueler(schule: dict, klasse: str, schueler_id: int) -> dict:
    klasseninfo = _finde_klasse(schule, klasse)
    for schueler in klasseninfo["schueler"]:
        if schueler["id"] == schueler_id:
            return schueler
    raise ValueError(f"Schueler mit ID {schueler_id} nicht gefunden.")


def schueler_hinzufuegen(schule: dict, klasse: str, name: str, geburtsdatum: str) -> dict:
    klasseninfo = _finde_klasse(schule, klasse)
    alle_ids = [
        schueler["id"]
        for klasseninfo_eintrag in schule["klassen"].values()
        for schueler in klasseninfo_eintrag["schueler"]
    ]
    neue_id = max(alle_ids, default=1000) + 1

    neuer_schueler = {
        "id": neue_id,
        "name": name,
        "geburtsdatum": geburtsdatum,
        "noten": {},
    }
    klasseninfo["schueler"].append(neuer_schueler)
    return neuer_schueler


def note_eintragen(schule: dict, klasse: str, schueler_id: int, fach: str, note: float) -> dict:
    if not 1 <= note <= 6:
        raise ValueError("Noten muessen zwischen 1 und 6 liegen.")

    schueler = _finde_schueler(schule, klasse, schueler_id)
    schueler["noten"].setdefault(fach, []).append(note)
    return schueler


def notendurchschnitt_berechnen(
    schule: dict, klasse: str, schueler_id: int, fach: str | None = None
) -> float:
    schueler = _finde_schueler(schule, klasse, schueler_id)

    if fach is not None:
        noten = schueler["noten"].get(fach, [])
        if not noten:
            return 0.0
        return sum(noten) / len(noten)

    alle_noten = [
        note for fachnoten in schueler["noten"].values() for note in fachnoten
    ]
    if not alle_noten:
        return 0.0
    return sum(alle_noten) / len(alle_noten)


def klassenbester(schule: dict, klasse: str, fach: str) -> dict:
    klasseninfo = _finde_klasse(schule, klasse)
    kandidaten = [
        schueler
        for schueler in klasseninfo["schueler"]
        if schueler["noten"].get(fach)
    ]
    if not kandidaten:
        raise ValueError(f"Keine Noten im Fach {fach} gefunden.")

    return min(
        kandidaten,
        key=lambda schueler: sum(schueler["noten"][fach]) / len(schueler["noten"][fach]),
    )


def versetzungsgefaehrdet(schule: dict, klasse: str) -> list[dict]:
    klasseninfo = _finde_klasse(schule, klasse)
    ergebnis = []

    for schueler in klasseninfo["schueler"]:
        for fachnoten in schueler["noten"].values():
            if fachnoten and (sum(fachnoten) / len(fachnoten)) > 4.0:
                ergebnis.append(schueler)
                break

    return ergebnis


# =========================
# Aufgabe 3: Restaurant
# =========================

RESTAURANT = {
    "speisekarte": {
        "vorspeisen": [
            {
                "id": 1,
                "name": "Bruschetta",
                "preis": 5.90,
                "zutaten": ["Brot", "Tomaten", "Knoblauch", "Basilikum"],
            },
            {
                "id": 2,
                "name": "Carpaccio",
                "preis": 8.90,
                "zutaten": ["Rindfleisch", "Parmesan", "Rucola"],
            },
        ],
        "hauptspeisen": [
            {
                "id": 3,
                "name": "Pizza Margherita",
                "preis": 9.90,
                "zutaten": ["Teig", "Tomatensosse", "Mozzarella", "Basilikum"],
            },
            {
                "id": 4,
                "name": "Spaghetti Carbonara",
                "preis": 11.90,
                "zutaten": ["Pasta", "Ei", "Speck", "Parmesan"],
            },
        ],
        "desserts": [
            {
                "id": 5,
                "name": "Tiramisu",
                "preis": 6.90,
                "zutaten": ["Loeffelbiskuit", "Kaffee", "Mascarpone", "Kakao"],
            },
            {
                "id": 6,
                "name": "Panna Cotta",
                "preis": 5.90,
                "zutaten": ["Sahne", "Vanille", "Beeren"],
            },
        ],
        "getraenke": [
            {"id": 7, "name": "Wasser", "preis": 2.90, "alkohol": False},
            {"id": 8, "name": "Hauswein", "preis": 4.90, "alkohol": True},
        ],
    },
    "tische": {
        1: {
            "plaetze": 4,
            "reserviert": True,
            "reservierung": {"name": "Mueller", "uhrzeit": "19:00", "personen": 4},
        },
        2: {"plaetze": 2, "reserviert": False, "reservierung": None},
        3: {"plaetze": 6, "reserviert": False, "reservierung": None},
    },
    "bestellungen": [
        {
            "bestellnr": 1001,
            "tisch": 1,
            "status": "serviert",
            "gerichte": [
                {"id": 1, "menge": 4},
                {"id": 3, "menge": 2},
                {"id": 4, "menge": 2},
                {"id": 7, "menge": 4},
            ],
            "zeitpunkt": "18:30",
            "bezahlt": False,
        }
    ],
}


def _finde_gericht(restaurant: dict, gericht_id: int) -> tuple[str, dict]:
    for kategorie, gerichte in restaurant["speisekarte"].items():
        for gericht in gerichte:
            if gericht["id"] == gericht_id:
                return kategorie, gericht
    raise ValueError(f"Gericht mit ID {gericht_id} nicht gefunden.")


def _finde_bestellung(restaurant: dict, bestellnr: int) -> dict:
    for bestellung in restaurant["bestellungen"]:
        if bestellung["bestellnr"] == bestellnr:
            return bestellung
    raise ValueError(f"Bestellung {bestellnr} nicht gefunden.")


def tisch_reservieren(
    restaurant: dict, tischnr: int, name: str, uhrzeit: str, personen: int
) -> dict:
    tisch = restaurant["tische"].get(tischnr)
    if tisch is None:
        raise ValueError(f"Tisch {tischnr} existiert nicht.")
    if tisch["reserviert"]:
        raise ValueError(f"Tisch {tischnr} ist bereits reserviert.")
    if personen > tisch["plaetze"]:
        raise ValueError("Zu viele Personen fuer diesen Tisch.")

    tisch["reserviert"] = True
    tisch["reservierung"] = {
        "name": name,
        "uhrzeit": uhrzeit,
        "personen": personen,
    }
    return tisch


def bestellung_aufnehmen(restaurant: dict, tischnr: int, gerichte: list[dict]) -> dict:
    if tischnr not in restaurant["tische"]:
        raise ValueError(f"Tisch {tischnr} existiert nicht.")

    for gericht in gerichte:
        _finde_gericht(restaurant, gericht["id"])

    neue_nummer = max(
        (bestellung["bestellnr"] for bestellung in restaurant["bestellungen"]),
        default=1000,
    ) + 1

    neue_bestellung = {
        "bestellnr": neue_nummer,
        "tisch": tischnr,
        "status": "aufgenommen",
        "gerichte": gerichte,
        "zeitpunkt": date.today().isoformat(),
        "bezahlt": False,
    }
    restaurant["bestellungen"].append(neue_bestellung)
    return neue_bestellung


def bestellung_aktualisieren(restaurant: dict, bestellnr: int, status: str) -> dict:
    bestellung = _finde_bestellung(restaurant, bestellnr)
    bestellung["status"] = status
    return bestellung


def rechnung_erstellen(restaurant: dict, bestellnr: int) -> dict:
    bestellung = _finde_bestellung(restaurant, bestellnr)
    positionen = []
    gesamt = 0.0

    for eintrag in bestellung["gerichte"]:
        _, gericht = _finde_gericht(restaurant, eintrag["id"])
        einzelpreis = gericht["preis"]
        menge = eintrag["menge"]
        summe = einzelpreis * menge
        positionen.append(
            {
                "gericht": gericht["name"],
                "menge": menge,
                "einzelpreis": einzelpreis,
                "summe": round(summe, 2),
            }
        )
        gesamt += summe

    return {
        "bestellnr": bestellnr,
        "tisch": bestellung["tisch"],
        "positionen": positionen,
        "gesamt": round(gesamt, 2),
    }


def umsatz_berechnen(restaurant: dict, datum: str | None = None) -> float:
    umsatz = 0.0
    for bestellung in restaurant["bestellungen"]:
        if datum is not None and bestellung["zeitpunkt"] != datum:
            continue
        if bestellung["bezahlt"]:
            umsatz += rechnung_erstellen(restaurant, bestellung["bestellnr"])["gesamt"]
    return round(umsatz, 2)


def beliebteste_gerichte(
    restaurant: dict, kategorie: str | None = None, top: int = 3
) -> list[dict]:
    haeufigkeiten = {}

    for bestellung in restaurant["bestellungen"]:
        for eintrag in bestellung["gerichte"]:
            gericht_kategorie, gericht = _finde_gericht(restaurant, eintrag["id"])
            if kategorie is not None and gericht_kategorie != kategorie:
                continue
            haeufigkeiten.setdefault(
                gericht["id"],
                {"id": gericht["id"], "name": gericht["name"], "menge": 0},
            )
            haeufigkeiten[gericht["id"]]["menge"] += eintrag["menge"]

    return sorted(haeufigkeiten.values(), key=lambda eintrag: eintrag["menge"], reverse=True)[:top]


# =========================
# Aufgabe 4: Bibliothek
# =========================

BIBLIOTHEK = {
    "buecher": [
        {
            "isbn": "978-3-86680-192-9",
            "titel": "Der Alchimist",
            "autor": "Paulo Coelho",
            "jahr": 1988,
            "genre": ["Roman", "Philosophie"],
            "exemplare": [
                {
                    "id": "A001",
                    "standort": "Regal A1",
                    "verfuegbar": False,
                    "entliehen_bis": "2025-06-15",
                },
                {
                    "id": "A002",
                    "standort": "Regal A1",
                    "verfuegbar": True,
                    "entliehen_bis": None,
                },
            ],
        },
        {
            "isbn": "978-3-423-21412-3",
            "titel": "Die Verwandlung",
            "autor": "Franz Kafka",
            "jahr": 1915,
            "genre": ["Erzaehlung", "Klassiker"],
            "exemplare": [
                {
                    "id": "B001",
                    "standort": "Regal B3",
                    "verfuegbar": True,
                    "entliehen_bis": None,
                },
                {
                    "id": "B002",
                    "standort": "Regal B3",
                    "verfuegbar": True,
                    "entliehen_bis": None,
                },
            ],
        },
    ],
    "nutzer": [
        {
            "id": 10001,
            "name": "Anna Schmidt",
            "email": "anna@example.com",
            "ausweisnummer": "BIB-12345",
            "entliehene_buecher": [
                {
                    "exemplar_id": "A001",
                    "isbn": "978-3-86680-192-9",
                    "entliehen_am": "2025-05-01",
                    "entliehen_bis": "2025-06-15",
                }
            ],
            "verlauf": [
                {
                    "isbn": "978-3-630-87658-6",
                    "exemplar_id": "C005",
                    "entliehen_am": "2025-03-10",
                    "zurueckgegeben_am": "2025-04-05",
                }
            ],
        }
    ],
    "reservierungen": [
        {
            "id": 5001,
            "isbn": "978-3-423-21412-3",
            "nutzer_id": 10001,
            "datum": "2025-05-10",
            "status": "aktiv",
        }
    ],
}


def _finde_buch(bibliothek: dict, isbn: str) -> dict:
    for buch in bibliothek["buecher"]:
        if buch["isbn"] == isbn:
            return buch
    raise ValueError(f"Buch mit ISBN {isbn} nicht gefunden.")


def _finde_nutzer(bibliothek: dict, nutzer_id: int) -> dict:
    for nutzer in bibliothek["nutzer"]:
        if nutzer["id"] == nutzer_id:
            return nutzer
    raise ValueError(f"Nutzer mit ID {nutzer_id} nicht gefunden.")


def _finde_exemplar(bibliothek: dict, exemplar_id: str) -> tuple[dict, dict]:
    for buch in bibliothek["buecher"]:
        for exemplar in buch["exemplare"]:
            if exemplar["id"] == exemplar_id:
                return buch, exemplar
    raise ValueError(f"Exemplar {exemplar_id} nicht gefunden.")


def buch_hinzufuegen(
    bibliothek: dict,
    isbn: str,
    titel: str,
    autor: str,
    jahr: int,
    genre: list[str],
    anzahl_exemplare: int,
) -> dict:
    if anzahl_exemplare <= 0:
        raise ValueError("Es muss mindestens ein Exemplar angelegt werden.")

    praefix = titel[0].upper()
    exemplare = [
        {
            "id": f"{praefix}{nummer:03d}",
            "standort": f"Regal {praefix}1",
            "verfuegbar": True,
            "entliehen_bis": None,
        }
        for nummer in range(1, anzahl_exemplare + 1)
    ]

    neues_buch = {
        "isbn": isbn,
        "titel": titel,
        "autor": autor,
        "jahr": jahr,
        "genre": genre,
        "exemplare": exemplare,
    }
    bibliothek["buecher"].append(neues_buch)
    return neues_buch


def buch_ausleihen(
    bibliothek: dict, isbn: str, nutzer_id: int, ausleihdatum: str, rueckgabedatum: str
) -> dict:
    buch = _finde_buch(bibliothek, isbn)
    nutzer = _finde_nutzer(bibliothek, nutzer_id)

    for exemplar in buch["exemplare"]:
        if exemplar["verfuegbar"]:
            exemplar["verfuegbar"] = False
            exemplar["entliehen_bis"] = rueckgabedatum
            eintrag = {
                "exemplar_id": exemplar["id"],
                "isbn": isbn,
                "entliehen_am": ausleihdatum,
                "entliehen_bis": rueckgabedatum,
            }
            nutzer["entliehene_buecher"].append(eintrag)
            return eintrag

    raise ValueError(f"Kein verfuegbares Exemplar fuer ISBN {isbn} vorhanden.")


def buch_zurueckgeben(bibliothek: dict, exemplar_id: str, rueckgabedatum: str) -> dict:
    buch, exemplar = _finde_exemplar(bibliothek, exemplar_id)
    exemplar["verfuegbar"] = True
    exemplar["entliehen_bis"] = None

    for nutzer in bibliothek["nutzer"]:
        for eintrag in list(nutzer["entliehene_buecher"]):
            if eintrag["exemplar_id"] == exemplar_id:
                nutzer["entliehene_buecher"].remove(eintrag)
                nutzer["verlauf"].append(
                    {
                        "isbn": buch["isbn"],
                        "exemplar_id": exemplar_id,
                        "entliehen_am": eintrag["entliehen_am"],
                        "zurueckgegeben_am": rueckgabedatum,
                    }
                )
                return exemplar

    return exemplar


def buch_reservieren(bibliothek: dict, isbn: str, nutzer_id: int, datum: str) -> dict:
    _finde_buch(bibliothek, isbn)
    _finde_nutzer(bibliothek, nutzer_id)

    neue_id = max((reservierung["id"] for reservierung in bibliothek["reservierungen"]), default=5000) + 1
    reservierung = {
        "id": neue_id,
        "isbn": isbn,
        "nutzer_id": nutzer_id,
        "datum": datum,
        "status": "aktiv",
    }
    bibliothek["reservierungen"].append(reservierung)
    return reservierung


def suche_buch(bibliothek: dict, suchbegriff: str, suchfeld: str = "titel") -> list[dict]:
    suchbegriff = suchbegriff.lower()
    ergebnis = []

    for buch in bibliothek["buecher"]:
        wert = buch.get(suchfeld)
        if isinstance(wert, list):
            if any(suchbegriff in eintrag.lower() for eintrag in wert):
                ergebnis.append(buch)
        elif wert is not None and suchbegriff in str(wert).lower():
            ergebnis.append(buch)

    return ergebnis


def ueberfaellige_buecher(bibliothek: dict, aktuelles_datum: str) -> list[dict]:
    ergebnis = []
    for nutzer in bibliothek["nutzer"]:
        for buch in nutzer["entliehene_buecher"]:
            if buch["entliehen_bis"] < aktuelles_datum:
                ergebnis.append(
                    {
                        "nutzer": nutzer["name"],
                        "exemplar_id": buch["exemplar_id"],
                        "isbn": buch["isbn"],
                        "faellig_bis": buch["entliehen_bis"],
                    }
                )
    return ergebnis


def empfehlungen(bibliothek: dict, nutzer_id: int) -> list[dict]:
    nutzer = _finde_nutzer(bibliothek, nutzer_id)
    gelesene_isbns = {
        eintrag["isbn"]
        for eintrag in nutzer["verlauf"]
    } | {eintrag["isbn"] for eintrag in nutzer["entliehene_buecher"]}

    bevorzugte_genres = set()
    for isbn in gelesene_isbns:
        try:
            buch = _finde_buch(bibliothek, isbn)
        except ValueError:
            continue
        bevorzugte_genres.update(buch["genre"])

    vorschlaege = []
    for buch in bibliothek["buecher"]:
        if buch["isbn"] in gelesene_isbns:
            continue
        if bevorzugte_genres.intersection(buch["genre"]):
            vorschlaege.append(buch)

    return vorschlaege


# =========================
# Aufgabe 5: Online-Shop
# =========================

SHOP = {
    "produkte": {
        "elektronik": [
            {
                "id": "E001",
                "name": "Smartphone X",
                "preis": 699.99,
                "bestand": 15,
                "eigenschaften": {
                    "marke": "TechBrand",
                    "speicher": "128GB",
                    "farben": ["Schwarz", "Weiss", "Blau"],
                },
                "bewertungen": [
                    {"kunde": "K1001", "sterne": 5, "kommentar": "Hervorragendes Geraet!"},
                    {
                        "kunde": "K1002",
                        "sterne": 4,
                        "kommentar": "Gutes Preis-Leistungs-Verhaeltnis",
                    },
                ],
            }
        ],
        "kleidung": [
            {
                "id": "K001",
                "name": "Jeans Slim Fit",
                "preis": 49.99,
                "bestand": {"S": 5, "M": 10, "L": 8, "XL": 3},
                "eigenschaften": {
                    "marke": "FashionBrand",
                    "material": "Denim",
                    "farben": ["Blau", "Schwarz"],
                },
                "bewertungen": [],
            }
        ],
    },
    "kunden": [
        {
            "id": "K1001",
            "name": "Max Mueller",
            "email": "max@example.com",
            "adresse": {
                "strasse": "Hauptstrasse 1",
                "plz": "12345",
                "stadt": "Berlin",
                "land": "Deutschland",
            },
            "bestellungen": ["B1001"],
            "warenkorb": [
                {"produkt_id": "K001", "menge": 1, "groesse": "M", "farbe": "Blau"}
            ],
        }
    ],
    "bestellungen": [
        {
            "id": "B1001",
            "kunde": "K1001",
            "datum": "2025-05-01",
            "status": "versendet",
            "positionen": [{"produkt_id": "E001", "menge": 1, "preis": 699.99}],
            "gesamtpreis": 699.99,
            "bezahlung": {"methode": "Kreditkarte", "status": "abgeschlossen"},
            "versand": {
                "methode": "Standard",
                "kosten": 4.99,
                "tracking": "TR123456789",
                "status": "unterwegs",
            },
        }
    ],
}


def _finde_produkt(shop: dict, produkt_id: str) -> tuple[str, dict]:
    for kategorie, produkte in shop["produkte"].items():
        for produkt in produkte:
            if produkt["id"] == produkt_id:
                return kategorie, produkt
    raise ValueError(f"Produkt {produkt_id} nicht gefunden.")


def _finde_shop_kunde(shop: dict, kunden_id: str) -> dict:
    for kunde in shop["kunden"]:
        if kunde["id"] == kunden_id:
            return kunde
    raise ValueError(f"Kunde {kunden_id} nicht gefunden.")


def _produkt_bestand_reduzieren(produkt: dict, menge: int, optionen: dict) -> None:
    bestand = produkt["bestand"]
    if isinstance(bestand, dict):
        groesse = optionen.get("groesse")
        if groesse is None:
            raise ValueError("Fuer dieses Produkt muss eine Groesse angegeben werden.")
        if bestand.get(groesse, 0) < menge:
            raise ValueError("Nicht genug Bestand fuer die gewaehlte Groesse.")
        bestand[groesse] -= menge
    else:
        if bestand < menge:
            raise ValueError("Nicht genug Bestand vorhanden.")
        produkt["bestand"] -= menge


def produkt_hinzufuegen(
    shop: dict,
    kategorie: str,
    name: str,
    preis: float,
    bestand: int | dict,
    eigenschaften: dict,
) -> dict:
    shop["produkte"].setdefault(kategorie, [])
    bestehende_ids = [
        produkt["id"]
        for produkte in shop["produkte"].values()
        for produkt in produkte
    ]
    prefix = kategorie[0].upper()
    laufnummer = len([produkt_id for produkt_id in bestehende_ids if produkt_id.startswith(prefix)]) + 1
    produkt_id = f"{prefix}{laufnummer:03d}"

    produkt = {
        "id": produkt_id,
        "name": name,
        "preis": preis,
        "bestand": bestand,
        "eigenschaften": eigenschaften,
        "bewertungen": [],
    }
    shop["produkte"][kategorie].append(produkt)
    return produkt


def zum_warenkorb_hinzufuegen(
    shop: dict, kunden_id: str, produkt_id: str, menge: int, **optionen
) -> dict:
    _finde_produkt(shop, produkt_id)
    kunde = _finde_shop_kunde(shop, kunden_id)

    eintrag = {"produkt_id": produkt_id, "menge": menge}
    eintrag.update(optionen)
    kunde["warenkorb"].append(eintrag)
    return eintrag


def bestellung_aufgeben(shop: dict, kunden_id: str) -> dict:
    kunde = _finde_shop_kunde(shop, kunden_id)
    if not kunde["warenkorb"]:
        raise ValueError("Der Warenkorb ist leer.")

    positionen = []
    gesamtpreis = 0.0

    for warenkorb_eintrag in kunde["warenkorb"]:
        _, produkt = _finde_produkt(shop, warenkorb_eintrag["produkt_id"])
        menge = warenkorb_eintrag["menge"]
        optionen = {k: v for k, v in warenkorb_eintrag.items() if k not in {"produkt_id", "menge"}}
        _produkt_bestand_reduzieren(produkt, menge, optionen)

        positionspreis = produkt["preis"] * menge
        position = {
            "produkt_id": produkt["id"],
            "menge": menge,
            "preis": produkt["preis"],
        }
        position.update(optionen)
        positionen.append(position)
        gesamtpreis += positionspreis

    neue_bestellnr = len(shop["bestellungen"]) + 1001
    bestellung = {
        "id": f"B{neue_bestellnr}",
        "kunde": kunden_id,
        "datum": date.today().isoformat(),
        "status": "offen",
        "positionen": positionen,
        "gesamtpreis": round(gesamtpreis, 2),
        "bezahlung": {"methode": "unbekannt", "status": "offen"},
        "versand": {
            "methode": "Standard",
            "kosten": 4.99,
            "tracking": None,
            "status": "vorbereitet",
        },
    }

    shop["bestellungen"].append(bestellung)
    kunde["bestellungen"].append(bestellung["id"])
    kunde["warenkorb"].clear()
    return bestellung


def bestellstatus_aktualisieren(shop: dict, bestell_id: str, status: str) -> dict:
    for bestellung in shop["bestellungen"]:
        if bestellung["id"] == bestell_id:
            bestellung["status"] = status
            return bestellung
    raise ValueError(f"Bestellung {bestell_id} nicht gefunden.")


def produkt_bewerten(
    shop: dict, produkt_id: str, kunden_id: str, sterne: int, kommentar: str
) -> dict:
    if not 1 <= sterne <= 5:
        raise ValueError("Sterne muessen zwischen 1 und 5 liegen.")

    _, produkt = _finde_produkt(shop, produkt_id)
    _finde_shop_kunde(shop, kunden_id)

    bewertung = {"kunde": kunden_id, "sterne": sterne, "kommentar": kommentar}
    produkt["bewertungen"].append(bewertung)
    return bewertung


def beliebte_produkte(
    shop: dict, kategorie: str | None = None, limit: int = 5
) -> list[dict]:
    produkte = []

    for produkt_kategorie, eintraege in shop["produkte"].items():
        if kategorie is not None and produkt_kategorie != kategorie:
            continue
        for produkt in eintraege:
            bewertungen = produkt["bewertungen"]
            durchschnitt = (
                sum(bewertung["sterne"] for bewertung in bewertungen) / len(bewertungen)
                if bewertungen
                else 0.0
            )
            produkte.append(
                {
                    "id": produkt["id"],
                    "name": produkt["name"],
                    "durchschnitt": round(durchschnitt, 2),
                    "anzahl_bewertungen": len(bewertungen),
                }
            )

    return sorted(
        produkte,
        key=lambda produkt: (produkt["durchschnitt"], produkt["anzahl_bewertungen"]),
        reverse=True,
    )[:limit]


def bestandsalarm(shop: dict, schwellenwert: int = 5) -> list[dict]:
    alarm = []

    for kategorie, produkte in shop["produkte"].items():
        for produkt in produkte:
            bestand = produkt["bestand"]
            if isinstance(bestand, dict):
                for variante, menge in bestand.items():
                    if menge <= schwellenwert:
                        alarm.append(
                            {
                                "kategorie": kategorie,
                                "produkt_id": produkt["id"],
                                "name": produkt["name"],
                                "variante": variante,
                                "bestand": menge,
                            }
                        )
            elif bestand <= schwellenwert:
                alarm.append(
                    {
                        "kategorie": kategorie,
                        "produkt_id": produkt["id"],
                        "name": produkt["name"],
                        "variante": None,
                        "bestand": bestand,
                    }
                )

    return alarm


def umsatzbericht(shop: dict, startdatum: str, enddatum: str) -> dict:
    passende_bestellungen = [
        bestellung
        for bestellung in shop["bestellungen"]
        if startdatum <= bestellung["datum"] <= enddatum
    ]

    gesamtumsatz = sum(bestellung["gesamtpreis"] for bestellung in passende_bestellungen)
    anzahl_bestellungen = len(passende_bestellungen)

    return {
        "startdatum": startdatum,
        "enddatum": enddatum,
        "anzahl_bestellungen": anzahl_bestellungen,
        "gesamtumsatz": round(gesamtumsatz, 2),
        "durchschnitt_bestellung": round(
            gesamtumsatz / anzahl_bestellungen, 2
        )
        if anzahl_bestellungen
        else 0.0,
    }


def beispiel_daten() -> dict:
    return {
        "videothek": deepcopy(VIDEOTHEK),
        "schule": deepcopy(SCHULE),
        "restaurant": deepcopy(RESTAURANT),
        "bibliothek": deepcopy(BIBLIOTHEK),
        "shop": deepcopy(SHOP),
    }


if __name__ == "__main__":
    daten = beispiel_daten()

    neuer_film = film_hinzufuegen(daten["videothek"], "Avatar", 2009, ["Sci-Fi", "Abenteuer"])
    bester_film = top_bewertete_filme(daten["videothek"], 1)[0]["titel"]

    neuer_schueler = schueler_hinzufuegen(daten["schule"], "10A", "Mia Becker", "2010-07-12")
    note_eintragen(daten["schule"], "10A", neuer_schueler["id"], "Mathematik", 2)

    bestellung = bestellung_aufnehmen(daten["restaurant"], 2, [{"id": 3, "menge": 2}, {"id": 7, "menge": 2}])
    rechnung = rechnung_erstellen(daten["restaurant"], bestellung["bestellnr"])

    reservierung = buch_reservieren(daten["bibliothek"], "978-3-423-21412-3", 10001, "2025-05-12")

    zum_warenkorb_hinzufuegen(daten["shop"], "K1001", "K001", 1, groesse="L", farbe="Schwarz")
    neue_shop_bestellung = bestellung_aufgeben(daten["shop"], "K1001")

    print("Neuer Film:", neuer_film["titel"])
    print("Top-Film:", bester_film)
    print("Neuer Schueler:", neuer_schueler["name"])
    print("Restaurant-Rechnung:", rechnung["gesamt"], "EUR")
    print("Reservierung:", reservierung["id"])
    print("Neue Shop-Bestellung:", neue_shop_bestellung["id"])
