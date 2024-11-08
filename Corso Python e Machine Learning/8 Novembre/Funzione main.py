'''def main():
    menu = Menù() 
    classifica = Classifica()  
    
    #Dizionario di giochi disponibili
    giochi_disponibili = {
        "Indovina il Numero": IndovinaIlNumero(),
        "Indovina Equazioni": IndovinaEquazioni(),
        "Sette e Mezzo": SetteMezzo(),
        "Sasso, Carta o Forbici": SassoCartaForbici()
    }
    
    #Esegui il ciclo principale del menù
    while True:
        menu.mostra_menù()  
        scelta = menu.scegli_opzione()  #Scelta dell'utente
        
        if scelta == "esci":
            break 
            
        #Se l'utente è registrato, permette di iniziare il gioco
        if menu.registrato:
            utente = Utente(menu.utenti_registrati)  #Crea l'utente (usa l'username dal menù)
            print(f"Benvenuto {utente.get_nome()}!")
            
            #Mostra l'elenco dei giochi in base ai punti
            punti = utente.get_punteggio()
            print(f"Il tuo punteggio attuale è {punti}.Puoi giocare a queste funzionalità:")
            
            #Se l'utente ha meno di 1 punto, può giocare solo a uno
            if punti == 0:
                print("Puoi giocare solo a 'Indovina il Numero'.")
                giochi_disponibili["Indovina il Numero"].start(utente)
            else:
                #Mostra le funzionalità disponibili in base al punteggio
                giochi_accessibili = []
                for i in range(punti + 1):
                    giochi_accessibili.append(list(giochi_disponibili.values())[i])
                print("Giochi disponibili:")
                for gioco in giochi_accessibili:
                    print(f"- {gioco.nome}")
                
                #Chiedi all'utente quale gioco vuole fare
                scelta_gioco = input("Scegli un gioco da iniziare: ")
                
                if scelta_gioco in giochi_disponibili:
                    gioco = giochi_disponibili[scelta_gioco]
                    gioco.start(utente)
                    #Aggiorna la classifica con il punteggio dell'utente
                    classifica.aggiungi_a_classifica(utente, utente.get_punteggio())
                    classifica.salva_classifica()  #Salva la classifica aggiornata
                else:
                    print("Gioco non disponibile. Riprova.")
        
        else:
            print("Devi registrarti prima di iniziare a giocare.")
            #Registrazione
            menu.registrazione_utente()
            
#Esempio
if __name__ == "__main__":
    main()
'''





