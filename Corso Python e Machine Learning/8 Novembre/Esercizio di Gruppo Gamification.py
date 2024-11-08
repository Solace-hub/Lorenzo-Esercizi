import time

# Classe Menù
class Menù:
    def __init__(self):
        self.registrato = False
        self.utenti_registrati = {}
        # Inizialmente, il menù contiene solo l'opzione per la registrazione e l'uscita
        self.opzioni = [
            ("-", "Registrati come nuovo utente"),
            ("-", "Visualizza classifica"),
            ("-", "Esci")
        ]

    # Funzione che mostra il menù principale, nascondendo l'opzione "Inizia il gioco" prima della registrazione
    def mostra_menù(self):
        print("\n=== Menù Principale ===")
        for key, value in self.opzioni:
            print(f"{key} - {value}")

    # Funzione di scelta dell'opzione del menù, se non si è registrati, printa che bisogna farlo
    def scegli_opzione(self):
        while True:
            scelta = input("Scegli un'opzione dal Menù: ")
            if scelta == "1":
                self.registrazione_utente()
                break  #Esce dal loop dopo la registrazione
            elif scelta == "2":
                if not self.registrato:
                    print("Devi registrarti prima di iniziare il gioco.")
                else:
                    print("Inizio del gioco...")
                    break
            elif scelta == "3":
                self.visualizza_classifica()  
                break
            elif scelta == "4":
                print("Uscita dal gioco... Arrivederci!")
                return "esci"  
            else:
                print("Opzione non valida. Riprova.") 

    # Funzione di registrazione dell'utente con scelta dell'username e motto del giocatore
    def registrazione_utente(self):
        print("Registrazione in corso...")
        time.sleep(1)

        while True:
            username = input("Scegli il tuo username: ").lower()
            if not username:
                print("Devi necessariamente inserire un username. Riprova.")
            elif username in self.utenti_registrati:
                print("Questo username è già presente, scegline un altro.")
            else:
                break

        punchline = input("Scegli un tuo motto personale: ").lower()
        if not punchline:
            punchline = "Non hai inserito nessun motto, peccato."

        print("Salvataggio delle informazioni...")
        time.sleep(2)

        self.utenti_registrati[username] = punchline
        self.registrato = True

        print("Registrazione completata!")
        time.sleep(1)
        print(f"Benvenuto giocatore {username}, il tuo motto è: '{punchline}'. Ti auguro buona fortuna!")

        # Dopo la registrazione, aggiungi l'opzione "Inizia il gioco" al secondo posto
        self.opzioni.insert(1, ("-", "Inizia il gioco"))





# Esempio
menu = Menù()

while True:
    menu.mostra_menù()
    scelta = menu.scegli_opzione()
    
    if scelta == "esci":
        break  
