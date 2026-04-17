"""
PROJEKT: SMART LIBRARY SYSTEM
PYTHON OOP ÜBUNGSAUFGABE

Die Aufgabe ist in 4 Stufen aufgebaut.
Jede Stufe baut auf der vorherigen auf.
"""

# =========================================================
# 1. GRUNDLEGEND (PFLICHT)
# =========================================================
"""
Erstelle eine Klasse Book.

Eigenschaften:
- title (String)
- author (String)
- isbn (String)
- is_available (Boolean, standardmäßig True)

Methoden:
- borrow() -> setzt is_available auf False, wenn möglich
- return_book() -> setzt is_available auf True
- __str__() -> gibt eine lesbare Beschreibung des Buches zurück

Test:
- Erstelle mindestens 3 Bücher
- Leihe mindestens 1 Buch aus
- Gib die Bücher aus
"""


# =========================================================
# 2. WEITERFÜHREND (FREIWILLIG)
# =========================================================
"""
Erstelle eine Klasse Library.

Eigenschaften:
- books (Liste von Book-Objekten)

Methoden:
- add_book(book)
- list_books() -> gibt alle Bücher als Strings zurück
- find_book(isbn) -> gibt das Buch zurück oder None
- borrow_book(isbn) -> leiht ein Buch aus, falls verfügbar
- return_book(isbn) -> gibt ein Buch zurück

Regeln:
- Keine doppelten ISBNs erlauben
- Ein Buch kann nur ausgeliehen werden, wenn es verfügbar ist
"""


# =========================================================
# 3. BONUS (FREIWILLIG)
# =========================================================
"""
Erstelle eine Klasse Member.

Eigenschaften:
- name (String)
- member_id (Integer oder String)
- borrowed_books (Liste von Book-Objekten)

Methoden:
- borrow_book(library, isbn)
- return_book(library, isbn)

Regeln:
- Ein Member darf maximal 3 Bücher gleichzeitig ausleihen
- Bücher werden sowohl in der Library als auch im Member verwaltet
- Member dürfen nur über die Library Bücher ausleihen

Zusatz:
- Verhindere doppelte Ausleihe desselben Buches
"""


# =========================================================
# 4. CHALLENGE (SEHR SCHWER, FREIWILLIG)
# =========================================================
"""
Erweitere das System zu einem vollständigen Bibliotheksmanagement-System.

1. RESERVIERUNGSSYSTEM
- Wenn ein Buch ausgeliehen ist, kann es reserviert werden
- Es gibt eine Warteschlange pro Buch (FIFO)

2. FÄLLIGKEITSDATUM
- Beim Ausleihen wird ein Rückgabedatum gesetzt (z.B. 14 Tage)
- Implementiere:
    is_overdue(today_date)

3. GEBÜHRENSYSTEM
- Pro überfälligem Tag entstehen 0.50 Gebühren
- Member hat ein Gebührenkonto

4. STATISTIKEN
- Häufig ausgeliehene Bücher
- Aktive Nutzer
- Aktuelle Ausleihzahlen

5. SIMULATION
Implementiere:
    simulate_day()

Diese Methode soll:
- Tage simulieren
- Overdue prüfen
- Statistiken aktualisieren
"""