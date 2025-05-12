# ================================================================
# Curs: ASIX (Administració de Sistemes Informàtics en Xarxa)
# Autor: Mario Scurtu
# Data: 07/05/2025
# Versió: 1
# ================================================================
# Especificacions d'entrada:
#   - Nom de la persona (string).
#   - Edat de la persona (enter).
#   - Feina del treballador (string).
# Especificacions de sortida:
#   - Impressió del salut de la persona ("Hola, sóc {nom}").
#   - Impressió de la feina del treballador ("Treballo com a {feina}").
# ================================================================

class Persona:
    def __init__(self, nom, edat):
        self.nom = nom
        self.edat = edat

    def saludar(self):
        print(f"Hola, sóc {self.nom}")

class Treballador(Persona):
    def __init__(self, nom, edat, feina):
        super().__init__(nom, edat)  # Crida al constructor de Persona
        self.feina = feina

    def mostrar_feina(self):
        print(f"Treballo com a {self.feina}")

# Exemple d'ús
treballador = Treballador("Joan", 30, "Programador")
treballador.saludar()
treballador.mostrar_feina()