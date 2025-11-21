#robot.py
import random

def jugada_robot():
    opcions = ["pedra", "paper", "tisora"]
    
    return random.choice(opcions)

def missatge_sortida():
    missatges = ["ets un noob", "traem un jugador millor que tu"]
    return random.choice(missatges)

