# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Una llista d'objectes de tipus Missatger (o subclasses).
#   - Un missatge (string).
# Especificacions de sortida:
#   - Enviament del missatge a través de cada tipus de missatger.
# ================================================================

class Missatger:
    def enviar(self, missatge):
        pass

class Email(Missatger):
    def enviar(self, missatge):
        print(f"Enviant email: {missatge}")

class SMS(Missatger):
    def enviar(self, missatge):
        print(f"Enviant SMS: {missatge}")

class WhatsApp(Missatger):
    def enviar(self, missatge):
        print(f"Enviant WhatsApp: {missatge}")

def enviar_missatges(missatgers, missatge):
    for missatger in missatgers:
        missatger.enviar(missatge)

# Exemple d'ús
missatgers = [Email(), SMS(), WhatsApp()]
missatge = "Hola, com estàs?"

enviar_missatges(missatgers, missatge)