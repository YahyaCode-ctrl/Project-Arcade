#Main.py
import jocs 

def mostrar_menu():
    print("\n" + "="*30)
    print("🕹️ BENVINGUT/DA AL MINI ARCADE de Yahya 🕹️")
    print("="*30)
    print("1. Jugar a -Pedra✊, Paper🤚, Tisora✌️-")
    print("2. Jugar a -Endevinar el Número-")
    print("S. -Sortir🚪-")
    print("-" * 30)

def main():
    while True:
        mostrar_menu()
        
        
        opcio = input("Introdueix la teva opció: ").upper()
        
        
        match opcio:
            case '1':
                
                jocs.janken()
            
            case '2':
                
                jocs.endevina()
            
            case 'S':
                
                print("\n👋 Gràcies per jugar al Mini Arcade!!👋")
                break
            case 's':
                
                print("\n👋 Gràcies per jugar al Mini Arcade!!👋")
                break 
            case _: 
                print("\n❌ Error: Opció no vàlida. Si us plau, tria 1, 2 o S.")
if __name__ == "__main__":
    main()