
# import hashlib





# self.cursor.execute("SELECT * FROM utenti WHERE is_admin = TRUE")
# if not self.cursor.fetchone():
# username = "admin"
#  password = hashlib.md5("admin123".encode()).hexdigest()  
# self.cursor.execute("INSERT INTO utenti (username, password, is_admin) VALUES (%s, %s, %s)", 
#                                     (username, password, True))
# self.miodb.commit()
# print("Utente amministratore creato con successo (username: 'admin', password: 'admin123').")