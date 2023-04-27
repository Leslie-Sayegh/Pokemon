class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self._nom = nom
        self._pv = pv
        self._niveau = niveau
        self._attaque = attaque
        self._defense = defense
        
    def afficher_infos(self):
        print(f"{self._nom} (Niveau {self._niveau}) - PV: {self._pv}, Attaque: {self._attaque}, Defense: {self._defense}")

class Normal(Pokemon):
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        super().__init__(nom, pv, niveau, attaque, defense)
        self._pv += 10
        self._attaque += 5
        self._defense += 5

class Feu(Pokemon):
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        super().__init__(nom, pv, niveau, attaque, defense)
        self._pv -= 10
        self._attaque += 10
        self._defense -= 5

class Eau(Pokemon):
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        super().__init__(nom, pv, niveau, attaque, defense)
        self._pv += 5
        self._attaque += 5
        self._defense += 10

class Terre(Pokemon):
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        super().__init__(nom, pv, niveau, attaque, defense)
        self._pv += 15
        self._attaque += 3
        self._defense += 15

p1 = Normal("Pikachu")
p2 = Feu("Salamèche")
p3 = Eau("Carapuce")
p4 = Terre("Taupiqueur")

p1.afficher_infos()
p2.afficher_infos()
p3.afficher_infos()
p4.afficher_infos()
