"""
Cloud-25-11 – Einstieg in Python Funktionen

AUFGABENSTELLUNG:
-----------------
Erstelle ein kleines Python-Programm zur Berechnung von Cloud-Kosten.

Dabei sollst du folgende Konzepte üben:
- Funktionen definieren
- Argumente übergeben
- Lokale Variablen (Scope) verstehen
- Rückgabewerte mit 'return' nutzen

Teilaufgaben:
1. Schreibe eine Funktion "berechne_kosten(stunden, preis_pro_stunde)"
   - Berechnet die Gesamtkosten
   - Verwendet einen Rabatt von 10% (Variable: rabatt = 0.1)
   - Gibt die berechneten Kosten zurück

2. Rufe die Funktion mit folgenden Werten auf:
   - 10 Stunden
   - 0.25 € pro Stunde

3. Gib das Ergebnis aus

4. Bonus:
   - Erstelle eine Funktion "format_ausgabe(kosten)"
   - Diese soll einen schön formatierten String zurückgeben:
     "Gesamtkosten: X.XX €"

5. Verständnisfrage:
   - Warum kann man außerhalb der Funktion nicht auf die Variable "rabatt" zugreifen?
"""


# --------------------------------------------------
# 1. FUNKTION ZUR KOSTENBERECHNUNG
# --------------------------------------------------

def berechne_kosten(stunden, preis_pro_stunde):
    """
    Diese Funktion berechnet die Kosten für eine Cloud-Ressource.

    Parameter:
    - stunden: Anzahl der Nutzungsstunden (z. B. 10)
    - preis_pro_stunde: Preis pro Stunde (z. B. 0.25 €)

    Rückgabewert:
    - Gesamtkosten nach Abzug eines Rabatts
    """

    # Lokale Variable:
    # Diese Variable existiert NUR innerhalb der Funktion
    rabatt = 0.1  # entspricht 10%

    # Berechnung der ursprünglichen Kosten
    kosten = stunden * preis_pro_stunde

    # Rabatt anwenden:
    # (1 - rabatt) entspricht 90% des ursprünglichen Preises
    kosten_nach_rabatt = kosten * (1 - rabatt)

    # Rückgabe des Ergebnisses an die aufrufende Stelle
    return kosten_nach_rabatt


# --------------------------------------------------
# 2. FUNKTION AUFRUFEN
# --------------------------------------------------

# Wir rufen die Funktion mit konkreten Werten auf
# und speichern das Ergebnis in der Variable "ergebnis"
ergebnis = berechne_kosten(10, 0.25)


# --------------------------------------------------
# 3. EINFACHE AUSGABE
# --------------------------------------------------

# Ausgabe des berechneten Werts
# Hinweis: Ohne Formatierung (noch viele Nachkommastellen möglich)
print("Unformatierte Ausgabe:", ergebnis)


# --------------------------------------------------
# 4. BONUS: FORMATIERTE AUSGABE
# --------------------------------------------------

def format_ausgabe(kosten):
    """
    Diese Funktion formatiert die Kosten als lesbaren Text.

    Parameter:
    - kosten: berechneter Geldbetrag

    Rückgabewert:
    - formatierter String (Text)
    """

    # :.2f sorgt dafür, dass nur 2 Nachkommastellen angezeigt werden
    return f"Gesamtkosten: {kosten:.2f} €"


# Verwendung der Formatierungsfunktion
formatierter_text = format_ausgabe(ergebnis)

# Ausgabe des formatierten Textes
print(formatierter_text)


# --------------------------------------------------
# 5. ERKLÄRUNG: SCOPE (GÜLTIGKEITSBEREICH)
# --------------------------------------------------

# Die Variable "rabatt" wurde innerhalb der Funktion definiert.
# Deshalb ist sie NUR dort sichtbar (lokaler Scope).

# Ein Zugriff außerhalb der Funktion führt zu einem Fehler:
# print(rabatt)  # -> NameError: name 'rabatt' is not defined

# Erklärung:
# Variablen innerhalb von Funktionen sind gekapselt,
# damit sie nicht unbeabsichtigt von außen verändert werden können.