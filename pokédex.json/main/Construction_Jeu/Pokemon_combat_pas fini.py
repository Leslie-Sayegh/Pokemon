import random

class Pokemon:
    def __init__(self, nom, niveau=1, vie=100, attaque=0, defense=0):
        self.__nom = nom
        self.__niveau = niveau
        self.__vie = vie
        self.__attaque = attaque
        self.__defense = defense
    
    def get_nom(self):
        return self.__nom
    
    def get_niveau(self):
        return self.__niveau
    
    def get_vie(self):
        return self.__vie
    
    def get_attaque(self):
        return self.__attaque
    
    def get_defense(self):
        return self.__defense
    
    def set_nom(self, nom):
        self.__nom = nom
    
    def set_niveau(self, niveau):
        self.__niveau = niveau
    
    def set_vie(self, vie):
        self.__vie = vie
    
    def set_attaque(self, attaque):
        self.__attaque = attaque
    
    def set_defense(self, defense):
        self.__defense = defense
    
    def attaquer(self, adversaire):
        # Choix aléatoire si l'attaque réussit ou non
        if random.randint(0, 1):
            # Calcul des dégâts infligés à l'adversaire
            degats = self.__attaque * adversaire.get_defense() * self.get_coefficient(adversaire)
            # Enlève des points de vie à l'adversaire
            adversaire.set_vie(adversaire.get_vie() - degats)
            print(f"{self.__nom} attaque {adversaire.get_nom()} et lui inflige {degats:.2f} points de dégâts !")
        else:
            print(f"{self.__nom} attaque {adversaire.get_nom()} mais rate son attaque !")
    
    def get_coefficient(self, adversaire):
        # Détermine le coefficient en fonction des types des deux Pokémon
        attaque_type = type(self).__name__
        defense_type = type(adversaire).__name__
        if attaque_type == "Eau":
            if defense_type == "Eau":
                return 1
            elif defense_type == "Feu":
                return 2
            elif defense_type == "Terre":
                return 0.5
            else:
                return 1
        elif attaque_type == "Feu":
            if defense_type == "Eau":
                return 0.5
            elif defense_type == "Feu":
                return 1
            elif defense_type == "Terre":
                return 2
            else:
                return 1
        elif attaque_type == "Terre":
            if defense_type == "Eau":
                return 2
            elif defense_type == "Feu":
                return 0.5
            elif defense_type == "Terre":
                return 1
            else:
                return 1
        else:
            if defense_type == "Eau" or defense_type == "Feu" or defense_type == "Terre":
                return 0.75
            else:
                return 1

class Normal(Pokemon):
    def __init__(self, nom, niveau=1, vie=100, attaque=0, defense=0):
        super().__init__(nom, niveau, vie, attaque, defense)
        self.set_vie(vie * 0.75)
        self.set_attaque

import random
import json

class Pokemon:
    def __init__(self, nom, pv=100, niveau=1, attaque=0, defense=0):
        self.__nom = nom
        self.__pv = pv
        self.__niveau = niveau
        self.__attaque = attaque
        self.__defense = defense

    def __str__(self):
        return f"{self.__nom} - PV: {self.__pv}, DEF: {self.__defense}, ATT: {self.__attaque}"

    def attaquer(self, adversaire):
        degats = self.__attaque * adversaire.defense_multiplier(self)
        adversaire.perdre_pv(degats)

    def defense_multiplier(self, adversaire):
        return 1

    def perdre_pv(self, degats):
        self.__pv -= degats
        if self.__pv < 0:
            self.__pv = 0

class Normal(Pokemon):
    def defense_multiplier(self, adversaire):
        if isinstance(adversaire, Eau):
            return 0.75
        elif isinstance(adversaire, Feu):
            return 0.75
        elif isinstance(adversaire, Terre):
            return 0.75
        else:
            return 1

class Feu(Pokemon):
    def defense_multiplier(self, adversaire):
        if isinstance(adversaire, Eau):
            return 0.5
        elif isinstance(adversaire, Terre):
            return 2
        elif isinstance(adversaire, Normal):
            return 0.75
        else:
            return 1

class Eau(Pokemon):
    def defense_multiplier(self, adversaire):
        if isinstance(adversaire, Feu):
            return 2
        elif isinstance(adversaire, Terre):
            return 0.5
        elif isinstance(adversaire, Normal):
            return 0.75
        else:
            return 1

class Terre(Pokemon):
    def defense_multiplier(self, adversaire):
        if isinstance(adversaire, Eau):
            return 0.5
        elif isinstance(adversaire, Feu):
            return 0.5
        elif isinstance(adversaire, Normal):
            return 0.75
        else:
            return 1

class Combat:
    def __init__(self):
        with open("pokemon.json", "r") as f:
            self.__pokedex = json.load(f)

    def lancer_combat(self, joueur, adversaire):
        while joueur._Pokemon__pv > 0 and adversaire._Pokemon__pv > 0:
            joueur_attaque = random.randint(0, 1)
            if joueur_attaque == 1:
                joueur.attaquer(adversaire)
                print(f"{joueur._Pokemon__nom} attaque !")
                print(f"{adversaire._Pokemon__nom} perd {joueur._Pokemon__attaque} points de vie !")
            else:
                print(f"{joueur._Pokemon__nom} rate son attaque...")

            if adversaire._Pokemon__pv <= 0:
                break

            adversaire_attaque = random.randint(0, 1)
            if adversaire_attaque == 1:
                adversaire.attaquer(joueur)
                print(f"{adversaire._Pokemon__nom} attaque !")
                

