#robot.py
import random

def jugada_robot():
    """
    Retorna la jugada del robot per a Pedra, Paper, Tisora.
    """
    opcions = ["pedra", "paper", "tisora"]
    
    return random.choice(opcions)

def missatge_sortida():
    """
    Retorna un missatge aleatori per simular el timbre del robot.
    """
    missatges = [
        "Beep-boop",
        "Error 404: Trobada la teva jugada.",
        "Timbre!",
        "La meva CPU ja ho sabia."
    ]
    return random.choice(missatges)

