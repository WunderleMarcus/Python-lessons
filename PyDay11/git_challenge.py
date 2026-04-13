import math
import time
import difflib

# --------------------------------------------
# STATE
# --------------------------------------------
project_files = {"taschenrechner.py": ""}
staged_files = set()
branches = {"main": {}}
current_branch = "main"

score = 0
start_time = time.time()
missions_completed = 0
total_missions = 8

# --------------------------------------------
# FUZZY MATCHING (Tippfehler erkennen)
# --------------------------------------------
def is_close_match(user_input, valid_inputs):
    for valid in valid_inputs:
        similarity = difflib.SequenceMatcher(None, user_input, valid).ratio()
        if similarity > 0.75:
            return True
    return False

# --------------------------------------------
# INPUT SYSTEM
# --------------------------------------------
def require_input(prompt, valid_inputs, hint):
    global score
    attempts = 0

    while True:
        answer = input(prompt).strip()

        if answer in valid_inputs:
            print("✅ Perfekt!")
            score += 10
            return True

        elif is_close_match(answer, valid_inputs):
            print("⚠️ Fast richtig! Tippfehler?")
            score += 5

        else:
            print("❌ Falsch.")

        attempts += 1

        if attempts >= 3:
            print("💡 Hinweis:", hint)

# --------------------------------------------
# UI
# --------------------------------------------
def show_progress():
    global missions_completed
    missions_completed += 1
    percent = int((missions_completed / total_missions) * 100)
    print(f"\n📊 Fortschritt: {percent}% ({missions_completed}/{total_missions})")
    print(f"🏆 Score: {score}")
    print("-" * 50)

def show_status():
    print("\n📂 Branch:", current_branch)
    print("📁 Dateien:", list(branches[current_branch].keys()))
    print("-" * 50)

# --------------------------------------------
# MISSIONS
# --------------------------------------------
def mission_1():
    print("\n🎯 MISSION 1: Repository initialisieren")
    print("Starte ein Git-Repository im aktuellen Ordner.")

    require_input(">>> ", ["git init"],
                  "Standardbefehl: git + init")

    show_progress()

def mission_2():
    print("\n🎯 MISSION 2: Datei erstellen")
    print("Erstelle die Datei 'taschenrechner.py'.")

    require_input(">>> ",
                  ["touch taschenrechner.py", "code taschenrechner.py", "nano taschenrechner.py"],
                  "Unter Linux/macOS oft 'touch <datei>'")

    project_files["taschenrechner.py"] = "# Taschenrechner\n"

    show_progress()

def mission_3():
    print("\n🎯 MISSION 3: Grundfunktionen")
    print("Funktionen werden automatisch hinzugefügt...")

    project_files["taschenrechner.py"] += """
def add(a,b): return a+b
def sub(a,b): return a-b
def mul(a,b): return a*b
def div(a,b): return a/b if b!=0 else 'Fehler'
"""
    show_progress()

def mission_4():
    global staged_files

    print("\n🎯 MISSION 4: Commit erstellen")

    require_input("git add: ",
                  ["git add taschenrechner.py"],
                  "Datei zum Staging hinzufügen")

    staged_files.add("taschenrechner.py")

    require_input("commit: ",
                  ['git commit -m "Erste Version des Taschenrechners"'],
                  "Commit braucht -m")

    branches[current_branch]["taschenrechner.py"] = project_files["taschenrechner.py"]
    staged_files.clear()

    show_status()
    show_progress()

def mission_5():
    global current_branch

    print("\n🎯 MISSION 5: Branching")

    require_input("branch: ",
                  ["git branch feature-erweiterungen"],
                  "git branch <name>")

    branches["feature-erweiterungen"] = branches["main"].copy()

    require_input("checkout: ",
                  ["git checkout feature-erweiterungen"],
                  "git checkout <branch>")

    current_branch = "feature-erweiterungen"

    project_files["taschenrechner.py"] += """
def pow_func(a,b): return a**b
def sqrt_func(a): return math.sqrt(a)
"""

    show_status()
    show_progress()

def mission_6():
    global current_branch

    print("\n🎯 MISSION 6: Merge Workflow")

    require_input("commit: ",
                  ['git commit -am "Neue Funktionen hinzugefügt"'],
                  "git commit -am ...")

    branches[current_branch]["taschenrechner.py"] = project_files["taschenrechner.py"]

    require_input("checkout main: ",
                  ["git checkout main"],
                  "Zurück zum Hauptbranch")

    current_branch = "main"

    require_input("merge: ",
                  ["git merge feature-erweiterungen"],
                  "git merge <branch>")

    branches["main"]["taschenrechner.py"] = branches["feature-erweiterungen"]["taschenrechner.py"]

    show_status()
    show_progress()

def mission_7():
    print("\n🎯 MISSION 7: Konflikt lösen (Simulation)")

    require_input("Lösung: ",
                  ["konflikt gelöst"],
                  "Konflikte werden im Code manuell gelöst")

    show_progress()

def mission_8():
    print("\n🎯 MISSION 8: Tests ausführen")

    code = branches["main"]["taschenrechner.py"]
    env = {"math": math}
    exec(code, env)

    print("🔍 Test läuft...")

    try:
        print("add:", env["add"](2, 3))
        print("pow:", env["pow_func"](2, 3))
        print("sqrt:", env)
        print("✅ Tests bestanden")
        global score
        score += 20
    except:
        print("❌ Tests fehlgeschlagen")

    show_progress()

# --------------------------------------------
# AUSWERTUNG
# --------------------------------------------
def final_score():
    duration = int(time.time() - start_time)

    print("\n🏁 CHALLENGE ABGESCHLOSSEN")
    print(f"⏱️ Zeit: {duration} Sekunden")
    print(f"🏆 Score: {score}")

    if score > 120:
        print("💎 Level: Senior Git Engineer")
    elif score > 80:
        print("🥇 Level: Fortgeschritten")
    else:
        print("🥉 Level: Anfänger")

# --------------------------------------------
# RUN
# --------------------------------------------
def run():
    mission_1()
    mission_2()
    mission_3()
    mission_4()
    mission_5()
    mission_6()
    mission_7()
    mission_8()
    final_score()

if __name__ == "__main__":
    run()