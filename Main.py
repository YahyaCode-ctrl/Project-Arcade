#Main.py
import jocs 

def mostrar_menu():
    print("=============================================")
    print("🕹️ BENVINGUT/DA AL MINI ARCADE de Yahya 🕹️")
    print("=============================================")
    print("1. Jugar a -Pedra✊, Paper🤚, Tisora✌️(Janken)-")
    print("2. Jugar a -Endevinar el Número(Nana)-")
    print("S. -Sortir🚪-")
    print("---------------------------------------------")

def main():
    while True:
        mostrar_menu()
        opcio = input("Introdueix la teva opció: ").upper() 
        match opcio:
            case '1':
                jocs.janken()
            case '2':
                jocs.nana()            
            case 'S':                
                print("\n👋 Gràcies per jugar al Mini Arcade de Yahya!!👋")
                break 
            case _: 
                print("\n❌tria 1, 2 o S.❌")
if __name__ == "__main__":
    main()