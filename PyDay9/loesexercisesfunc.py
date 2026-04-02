"""
Musterlösung zu allen Übungen
Detaillierte Kommentare erklären jeden Schritt
"""

# ===============================
# Übung 1: Funktionen definieren und aufrufen
# ===============================

def guten_morgen():
    """
    Einfaches Beispiel für eine Funktion ohne Parameter.
    Diese Funktion gibt einen Morgen-Gruß aus.
    """
    print("Guten Morgen!")
    print("Ich wünsche dir einen schönen Tag!")

def guten_abend():
    """
    Funktion ohne Parameter für Abendgruß.
    """
    print("Guten Abend!")
    print("Ich hoffe, du hattest einen guten Tag!")

# Funktionen werden mit Klammern aufgerufen
guten_morgen()
guten_abend()


# ===============================
# Übung 2: Parameter
# ===============================

def stelle_vor(name, alter):
    """
    Beispiel für Funktionen mit Parametern.
    Parameter 'name' und 'alter' werden im String verwendet.
    """
    print(f"Ich bin {name} und ich bin {alter} Jahre alt.")

def rechne(zahl1, zahl2):
    """
    Rechenfunktion: Summe, Differenz, Produkt.
    Rückgabe erfolgt als Dictionary.
    """
    return {
        "summe": zahl1 + zahl2,
        "differenz": zahl1 - zahl2,
        "produkt": zahl1 * zahl2
    }

# Aufruf der Funktionen mit verschiedenen Werten
stelle_vor("Anna", 25)
stelle_vor("Ben", 30)

ergebnis = rechne(10, 5)
print(ergebnis["summe"], ergebnis["differenz"], ergebnis["produkt"])


# ===============================
# Übung 3: Return
# ===============================

def quadrat(zahl):
    return zahl * zahl  # Rückgabe des Quadrats

def verdopple(zahl):
    return zahl * 2     # Rückgabe des Doppelten

def berechne_preis(netto, steuersatz):
    """
    Berechnet Bruttopreis inkl. Steuer.
    round() auf 2 Dezimalstellen für Geldbeträge
    """
    brutto = netto * (1 + steuersatz)
    return round(brutto, 2)

def teile_mit_rest(dividend, divisor):
    """
    Gibt Quotient und Rest zurück.
    Python packt mehrere Rückgabewerte als Tuple.
    """
    return dividend // divisor, dividend % divisor

# Testbeispiele
print(quadrat(7))
print(verdopple(15))
print(berechne_preis(100, 0.19))
q, r = teile_mit_rest(17, 5)
print(q, r)


# ===============================
# Übung 4: Parameter-Varianten
# ===============================

def erstelle_profil(name, alter, stadt, beruf):
    profil = f"""
--- BENUTZERPROFIL ---
Name: {name}
Alter: {alter}
Stadt: {stadt}
Beruf: {beruf}
----------------------
"""
    print(profil)

def berechne_rabatt(preis, rabatt=10):
    neuer_preis = preis * (1 - rabatt/100)
    return round(neuer_preis, 2)

def erstelle_nachricht(text, absender="System", wichtig=False):
    if wichtig:
        return f"!!! WICHTIG !!! [{absender}]: {text}"
    return f"[{absender}]: {text}"


# ===============================
# Übung 5: Scope
# ===============================

kontostand = 1000  # globale Variable

def zeige_kontostand():
    print(f"Aktueller Kontostand: {kontostand} €")

def pruefe_betrag(betrag):
    if betrag <= kontostand:
        return "Betrag verfügbar"
    else:
        return "Nicht genug Guthaben"

def simuliere_abzug(betrag):
    # lokale Variable, verändert globalen Wert NICHT
    neuer_kontostand = kontostand - betrag
    print(f"Simulierter Kontostand: {neuer_kontostand} €")


# ===============================
# Übung 6: Text-Verarbeitung
# ===============================

def bereite_text_vor(text):
    """
    Entfernt führende/folgende Leerzeichen und macht jeden Wortanfang groß.
    """
    return text.strip().title()

def ersetze_zeichen(text, alt, neu):
    """
    Ersetzt 'alt' durch 'neu' im Text.
    """
    return text.replace(alt, neu)

def teile_text(text, trenner=" "):
    """
    Teilt den Text in eine Liste anhand eines Trenners.
    """
    return text.split(trenner)