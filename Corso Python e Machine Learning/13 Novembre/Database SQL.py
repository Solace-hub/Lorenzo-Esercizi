import mysql.connector

#Connessione al server MySQL
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        port=3306
    )

    #Creazione del cursore
    mycursor = mydb.cursor()

    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS mypythonsql")
        print("Database 'mypythonsql' creato con successo.")
    except mysql.connector.Error as err:
        print(f"Errore durante l'esecuzione di CREATE DATABASE: {err}")

except mysql.connector.Error as conn_err:
    print(f"Errore di connessione al server MySQL: {conn_err}")








