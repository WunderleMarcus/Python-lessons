"""
Uebersicht: Git und Versionskontrolle (mit didaktischem Hintergrund)

Lernziele im Kontext:
- Git verstehen = Prinzipien begreifen (nicht nur Befehle auswendig lernen)
- Git anwenden = sicher im Alltag nutzen (Fehler inklusive)
- Tools integrieren = GitHub + VS Code als Arbeitsumgebung nutzen

1. Versionskontrolle – Warum und wofuer?
Begriff: Versionskontrolle
Erklaerung:
Ein System, das Aenderungen an Dateien speichert, sodass du jederzeit zu frueheren Versionen zurueckkehren kannst.
Didaktischer Hintergrund:
Reduziert Angst vor Fehlern und foerdert Experimentieren
Anekdote:
Ein Entwickler ueberschreibt aus Versehen seine funktionierende Datei mit kaputtem Code.
Ohne Git: Problem.
Mit Git: git checkout stellt den alten Stand wieder her.

2. Git – Das Grundprinzip
Begriff: Repository (Repo)
Erklaerung:
Ein Projektordner mit Historie, in dem alle Aenderungen gespeichert werden.
Anekdote:
Ein Repo ist wie ein Tagebuch: Jede Aenderung ist ein Eintrag.

Begriff: Commit
Erklaerung:
Ein gespeicherter Zustand des Projekts mit Beschreibung.
Didaktischer Fokus:
Foerdert strukturiertes Arbeiten in kleinen Schritten.
Anekdote:
Schlechter Commit: fix stuff
Guter Commit: Fix: Division durch 0 abgefangen

3. Basis-Workflows
Begriff: git init
Erklaerung:
Startet Git in einem Ordner.
Anekdote:
Wie ein leeres Notizbuch beginnen.

Begriff: git add
Erklaerung:
Markiert Aenderungen fuer den naechsten Commit.
Didaktischer Fokus:
Bewusste Auswahl von Aenderungen.
Anekdote:
Wie ein Warenkorb beim Einkaufen.

Begriff: git commit
Erklaerung:
Speichert die ausgewaehlten Aenderungen.
Anekdote:
Wie ein Speicherpunkt.

Begriff: git push
Erklaerung:
Laedt Aenderungen zu GitHub hoch.
Anekdote:
Wie ein Backup in der Cloud.

Begriff: git pull
Erklaerung:
Holt Aenderungen von anderen.
Didaktischer Fokus:
Verstaendnis fuer Zusammenarbeit.

Begriff: git clone
Erklaerung:
Kopiert ein bestehendes Repository.
Anekdote:
Wie ein fertiges Projekt uebernehmen.

4. Branching Basics
Begriff: Branch
Erklaerung:
Ein paralleler Entwicklungszweig.
Didaktischer Hintergrund:
Fehlerfreundliches Arbeiten.
Anekdote:
Neues Feature ohne Risiko testen.

Begriff: Merge
Erklaerung:
Fuehrt Aenderungen zusammen.
Anekdote:
Kann zu Konflikten fuehren.

5. GitHub und Tools
Begriff: GitHub Repository
Erklaerung:
Online-Speicherort fuer Projekte.

Tool: Visual Studio Code Git Panel
Erklaerung:
Grafische Oberfläche fuer Git-Befehle.
Didaktischer Vorteil:
Visuelles Lernen erleichtert den Einstieg.

6. Uebung: Python-Projekt (Taschenrechner)
Ziel:
Ein Projekt mit Git versionieren.

Ablauf:
- Projekt erstellen
- git init
- Erster Commit
- Feature hinzufuegen
- Neuer Commit
- Push zu GitHub
- Optional Branch verwenden

Didaktischer Hintergrund:
- Lernen durch Tun
- Fehler sind erlaubt
- Kleine Schritte verbessern Verstaendnis

Schritt-fuer-Schritt-Anleitung:

1. Projekt erstellen:
Ordner: taschenrechner
Datei: calculator.py
Code:

def add(a, b):
    return a + b

print(add(2, 3))

2. Git initialisieren:
> git init

3. Status pruefen:
> git status

4. Datei hinzufuegen:
> git add calculator.py

5. Commit erstellen:
> git commit -m "Initial commit: einfacher Taschenrechner"

6. GitHub Repository erstellen und verbinden:
> git remote add origin https://github.com/USERNAME/taschenrechner.git
> git branch -M main
> git push -u origin main

7. Feature hinzufuegen:

def multiply(a, b):
    return a * b

print(multiply(3, 4))

8. Commit:
> git add calculator.py
> git commit -m "Feature: Multiplikation hinzugefuegt"

9. Push:
> git push

10. Optional Branch:
> git checkout -b feature-division

Code:

def divide(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b

Commit:
> git add .
> git commit -m "Feature: Division hinzugefuegt"

Merge:
> git checkout main
> git merge feature-division

11. Pull:
> git pull

Ergebnis:
- Funktionierendes Python-Projekt
- Mehrere Commits
- GitHub Repository
- Optional Branching genutzt

Musterloesung (Python-Code):
"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Fehler: Division durch 0"
    return a / b


def main():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Multiplication")
    print("3. Division")

    choice = input("Choose operation (1/2/3): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == "1":
        print("Result:", add(a, b))
    elif choice == "2":
        print("Result:", multiply(a, b))
    elif choice == "3":
        print("Result:", divide(a, b))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main()
