# ===============================
# LISTS
# ===============================

# Leichte Aufgabe:
# Anleitung:
# - Gegeben ist eine Liste von Zahlen
# - Iteriere mit einer for-Schleife über alle Elemente
# - Gib jede Zahl verdoppelt aus
#
# Praxis (freie Wirtschaft):
# - Beispiel: Verarbeitung von Sensordaten (z.B. Temperaturwerte)
# - Verdopplung könnte eine Umrechnung sein (z.B. Skalierung von Messwerten)
# - Wird oft genutzt in Datenpipelines, ETL-Prozessen oder Monitoring-Systemen
#numbers_list_easy = [3, 7, 2, 9, 4]
#for zahl in numbers_list_easy:
#    print(zahl * 2)


# Anspruchsvolle Aufgabe:
# Anleitung:
# - Iteriere über die Liste
# - Behalte nur gerade Zahlen
# - Quadriere diese
# - Speichere sie in einer neuen Liste
#
# Praxis (freie Wirtschaft):
# - Beispiel: Datenbereinigung und Feature Engineering in Data Science
# - Nur bestimmte Werte werden berücksichtigt (Filterung)
# - Transformation (Quadrat) kann z.B. für ML-Modelle notwendig sein
"""
numbers_list_hard = [1, 2, 3, 4, 5, 6, 7, 8]
new_numbers = [] # Neue Liste wird erstellt
for num in numbers_list_hard:
    if num % 2 == 0:
        new_numbers.append(num ** 2)
        
print(new_numbers)

"""


# ===============================
# SETS
# ===============================

# Leichte Aufgabe:
# Anleitung:
# - Iteriere über ein Set von Strings
# - Gib jedes Element in Großbuchstaben aus
#
# Praxis (freie Wirtschaft):
# - Beispiel: Normalisierung von Nutzereingaben (z.B. Tags, Kategorien)
# - Groß-/Kleinschreibung wird vereinheitlicht
# - Wichtig für Suche, Datenbanken und APIs
fruits_set_easy = {"apple", "banana", "cherry"}
# for fruit in fruits_set_easy:
#    print(fruit.upper())




# Anspruchsvolle Aufgabe:
# Anleitung:
# - Filtere gerade Zahlen aus dem Set
# - Multipliziere sie mit 10
# - Speichere sie in einem neuen Set
#
# Praxis (freie Wirtschaft):
# - Beispiel: Verarbeitung von IDs oder Codes ohne Duplikate
# - Sets garantieren Einzigartigkeit → wichtig für Datenkonsistenz
# - Transformation könnte z.B. Preisberechnung oder Skalierung sein
numbers_set_hard = {1, 2, 3, 4, 5, 6}
# new_set = {num * 10 for num in numbers_set_hard if num % 2 == 0}

# print(new_set)





# ===============================
# DICTIONARIES
# ===============================

# Leichte Aufgabe:
# Anleitung:
# - Iteriere über Schlüssel und Werte
# - Gib beide aus
#
# Praxis (freie Wirtschaft):
# - Beispiel: Verarbeitung von JSON-Daten aus APIs
# - Dictionaries sind Standardformat für Datenübertragung
# - Logging, Debugging und Datenanalyse greifen darauf zurück


person_dict_easy = {"name": "anna", "age": 25, "city": "berlin"}

#for key , value in person_dict_easy.items():

#    print(f"{key}: {value}")
    
# for key in person_dict_easy.keys(): # funktionert mit .keys / .values und .items(Paarweise key+value)
#    print(((key)).capitalize())











# Anspruchsvolle Aufgabe:
# Anleitung:
# - Filtere Studenten mit Note < 2.0
# - Speichere sie in neuem Dictionary
# - Zähle die Anzahl
#
# Praxis (freie Wirtschaft):
# - Beispiel: KPI-Auswertung (z.B. Top-Kunden, beste Produkte)
# - Filterung nach Kriterien (z.B. Umsatz > X)
# - Zählen = wichtige Kennzahl für Reports und Dashboards
grades_dict_hard = {
    "Anna": 1.7,
    "Ben": 2.3,
    "Clara": 1.3,
    "David": 3.0
}
"""
best_student = {
    name: note
    for name, note in grades_dict_hard.items()
    if note < 2.0
}
anzahl = len(best_student)

print(best_student)
print("Anzahl:", anzahl)
"""







# ===============================
# TUPLES
# ===============================

# Leichte Aufgabe:
# Anleitung:
# - Berechne die Summe aller Werte
#
# Praxis (freie Wirtschaft):
# - Beispiel: Aggregation von Kennzahlen (z.B. Tagesumsätze)
# - Summe = zentrale Kennzahl in Reporting-Systemen
# - Wird oft in Controlling und BI eingesetzt
coordinates_tuple_easy = (4, 7, 1, 9)

# total = sum(coordinates_tuple_easy)

# print("SUMME:", total)








# Anspruchsvolle Aufgabe:
# Anleitung:
# - Extrahiere Namen in eine Liste
# - Berechne Durchschnittsalter
#
# Praxis (freie Wirtschaft):
# - Beispiel: HR-Analyse (Mitarbeiterdaten)
# - Durchschnittsalter ist wichtige Kennzahl
# - Daten werden oft aus unveränderlichen Quellen (z.B. DB-Records → Tuple) gelesen
data_tuple_hard = (("Anna", 25), ("Ben", 30), ("Clara", 22))

names = [] # Neue Liste wurden erstellt
ages = [] # Neue Liste wurden erstellt

for name, age in data_tuple_hard:
    names.append(name)
    ages.append(age)
    
average_age = sum(ages) / len(ages) # Berechnung Summe Alter durch anzahl personen

print("NAMES:", names)
print("AVERAGE AGE:", round(average_age, 2)) # Runden nach mathematischen Regeln auf 2 Nachkommastellen.