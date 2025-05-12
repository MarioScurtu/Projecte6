# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Un client (string).
#   - Un objecte notificador (EmailNotificador o similar).
# Especificacions de sortida:
#   - Confirmació de la comanda per pantalla.
#   - Notificació al client a través de l'objecte notificador.
# ================================================================

class EmailNotificador:
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class SMSNotificador:  # Nova classe de notificador
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class Comanda:
    def __init__(self, client, notificador):  # Injecció de dependència
        self.client = client
        self.notificador = notificador

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")

# Exemple d'ús
email_notificador = EmailNotificador()
comanda1 = Comanda("Pere", email_notificador)
comanda1.confirmar()

sms_notificador = SMSNotificador()
comanda2 = Comanda("Anna", sms_notificador)
comanda2.confirmar()