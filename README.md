
 <img width="750" height="400" alt="rsz_yahya_elhadri" src="https://github.com/user-attachments/assets/fde0428b-a158-4bd0-9e6d-dd75a8b3bc97" />

## Introduccio: 
Aquest projecte implementa una petita màquina recreativa virtual utilitzant Python, estructurada en mòduls per separar la lògica del menú, els jocs i el competidor (robot).

## Característiques:

* **Menú Principal Interactiu:** Un bucle principal que permet a l'usuari triar entre diferents jocs.
* **Joc de Pedra, Paper, Tisora(Janken):** Permet jugar contra un competidor virtual (Robot) amb diferents modes de dificultat (al millor de 3 victòries o al millor de 5 rondes).
* **Joc d'Endevinar el Número(nana):** L'usuari ha d'endevinar un número aleatori amb l'ajuda de pistes ("massa alt" o "massa baix"), comptant el nombre d'intents.
* **Estructura Modular:** El codi està dividit en mòduls lògics (`main.py`, `jocs.py`, `robot.py`) per millorar l'organització i el manteniment.

## Estructura del Projecte:

El projecte es compon de tres fitxers principals:

| Fitxer | Descripció |
| :--- | :--- |
| `main.py` | Conté el bucle principal, el menú i l'entrada de l'aplicació. Utilitza `match-case` per gestionar les opcions del menú. |
| `jocs.py` | Conté la lògica i les funcions completes dels jocs (`janken()` i `nana()`). |
| `robot.py` | Conté la lògica del competidor de la màquina (la jugada aleatòria del robot). |

## Com Jugar

1.  **Tria l'opció (1, 2, o S) i prem Enter.**
2.  Si tries el Joc 1, hauràs de triar el mode de joc ("Primer a 3 victòries" o "Al millor de 5 rondes").
3.  El programa tornarà al menú principal un cop finalitzat el joc.
4.  Per sortir, introdueix **`S`** o **`s`** al menú.
