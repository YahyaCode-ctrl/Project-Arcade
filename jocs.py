#jocs.py
import random
import robot

def obtenir_jugada_usuari():
    while True:
        jugada = input("La teva jugada (pedra, paper, tisora): ").lower()
        if jugada in ["pedra", "paper", "tisora"]:
            return jugada
        else:
            print("❌ Opció no vàlida. Si us plau, escriu 'pedra', 'paper' o 'tisora'.")

def determinar_guanyador_ronda(jug_usuari, jug_robot):
    if jug_usuari == jug_robot:
        return 'empat'
    if (jug_usuari == "pedra" and jug_robot == "tisora") or \
       (jug_usuari == "tisora" and jug_robot == "paper") or \
       (jug_usuari == "paper" and jug_robot == "pedra"):
        return 'usuari'
    else:
        return 'robot'
def janken():
    print("--- Pedra, Paper, Tisora (Janken) ---")
    while True:
        mode = input("Tria mode de joc:\n1. Primer a 3 victòries\n2. Al millor de 5 rondes\nOpció: ")
        if mode == '1':
            victories_necessaries = 3
            limit_rondes = float('inf') 
            break
        elif mode == '2':
            victories_necessaries = 3 
            limit_rondes = 5
            break
        else:
            print("Opció no vàlida")

    puntuacio_usuari = 0
    puntuacio_robot = 0
    ronda_actual = 0
    while puntuacio_usuari < victories_necessaries and \
          puntuacio_robot < victories_necessaries and \
          ronda_actual < limit_rondes:
        
        ronda_actual += 1
        print(f"\n===== Ronda {ronda_actual} =====")
        
        jugada_usuari = obtenir_jugada_usuari()
        jugada_robot = robot.robot_janken() 

        print(f"El robot: **{jugada_robot}**")
        
        guanyador = determinar_guanyador_ronda(jugada_usuari, jugada_robot)

        if guanyador == 'usuari':
            print(" Has guanyat la ronda.")
            puntuacio_usuari += 1
        elif guanyador == 'robot':
            print(" El robot guanya la ronda.")
            puntuacio_robot += 1
        else:
            print("Empat!")
        
        print(f"Score: Tu {puntuacio_usuari} - {puntuacio_robot} Robot")
    print("\n--- RESULTAT FINAL DEL PARTIT ---")
    if puntuacio_usuari > puntuacio_robot:
        print("FELICITATS! Has guanyat el partit! ")
    elif puntuacio_robot > puntuacio_usuari:
        print(f" Ha guanyat la màquina! \n {robot.missatge_sortida()} ")
    else:
        print(" El partit ha acabat en empat.")

def nana():
    print("\n--- Endevinar el Número ---")
    nombre_adivinat = random.randint(1, 100) 
    intents = 0
    endevinat = False
    
    print("He pensat un nombre entre 1 i 100. Endevina'l!")
    while not endevinat:
        try:
            intents += 1
            entrada = input(f"Intent {intents}: Introdueix un número: ")
            if not entrada.isdigit():
                print(" Si us plau, introdueix un nombre enter vàlid.")
                intents -= 1 
                continue
            nombre_usuari = int(entrada)
            if nombre_usuari < nombre_adivinat:
                print(" Massa baix. Prova amb un número més gran.")
            elif nombre_usuari > nombre_adivinat:
                print(" Massa alt. Prova amb un número més petit.")
            else:
                endevinat = True
        except Exception:
            print("Torna a intentar-ho. ")
            intents -= 1
    print("\n--- RESULTAT ---")
    print(f"Has endevinat el número {nombre_adivinat}!")
    print(f"Ho has aconseguit en {intents} intents.")