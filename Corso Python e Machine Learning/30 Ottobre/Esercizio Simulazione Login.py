#Dati di accesso vuoti inizialmente
dati_utente = {}
dati_admin = {}

#Funzione per la registrazione utente
def registrazione_utente():
    print("Inserisci i seguenti dati:")
    nome_utente = input("Crea un nome utente")
    password = input("Crea una password")
    dati_utente["nome_utente"] = nome_utente
    dati_utente["password"] = password
    print("Registrazione effettuata")

#Funzione per la registrazione admin
def registrazione_admin():
    print("Inserisci i seguenti dati:")
    nome_utente_admin = input("Crea un nome utente")
    password_admin = input("Crea una password")
    dati_admin["nome_utente_admin"] = nome_utente_admin
    dati_admin["password_admin"] = password_admin
    print("Registrazione effettuata")

#Funzione per il controllo delle credenziali utente
def controllo_credenziali_login(nome_utente, password):
    return nome_utente == dati_utente.get("nome_utente") and password == dati_utente.get("password")

#Funzione di login principale
def login():
    if dati_utente:

        while True:
            nome_utente = input("Inserisci il nome utente:")
            password = input("Inserisci la password:")

            if controllo_credenziali_login(nome_utente, password):
                print("Accesso consentito")
            break
    else:
            print("Accesso negato")

#Funzione per cambiare la password utente
def cambia_password():
    nuova_password = input("Inserisci la nuova password:")
    dati_utente["password"] = nuova_password
    print("Password cambiata")

def opzioni_post_login():
     selezione = input("Vorresti modificare la tua password? (sì/no)")
     if selezione == "sì":
          cambia_password()


     
     

