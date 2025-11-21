#robot.py
import random

def robot_janken():
    opcions = ["pedra", "paper", "tisora"]
    
    return random.choice(opcions)

def missatge_sortida():
    missatges = ["Doneu-me un jugador millor"]
    return random.choice(missatges)

