class Pokemon:
    def __init__(self, name, hp, attack, defense):
        self._name = name
        self._hp = hp
        self._attack = attack
        self._defense = defense

    def display_info(self):
        print("Nom:", self._name)
        print("Points de vie:", self._hp)
        print("Attaque:", self._attack)
        print("Défense:", self._defense)


class NormalPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack, defense)


class FeuPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack * 1.2, defense * 0.8)


class EauPokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp, attack * 0.8, defense * 1.2)


class TerrePokemon(Pokemon):
    def __init__(self, name, hp, attack, defense):
        super().__init__(name, hp * 1.2, attack * 0.8, defense * 1.2)


class Combat:
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2
        self._pokedex = []

    def is_alive(self, pokemon):
        return pokemon._hp > 0

    def winner(self):
        if self.is_alive(self._pokemon1):
            return self._pokemon1._name
        else:
            return self._pokemon2._name

    def attack_hits(self):
        return random.randint(0, 1)

    def attack_multiplier(self, attacking_type, defending_type):
        if attacking_type == "Feu":
            if defending_type == "Eau":
                return 0.5
            elif defending_type == "Terre":
                return 2.0
        elif attacking_type == "Eau":
            if defending_type == "Feu":
                return 2.0
            elif defending_type == "Terre":
                return 0.5
        elif attacking_type == "Terre":
            if defending_type == "Feu":
                return 0.5
            elif defending_type == "Eau":
                return 2.0
        else:  # type Normal
            return 1.0

    def damage_dealt(self, attacking_pokemon, defending_pokemon):
        attacking_type = type(attacking_pokemon).__name__
        defending_type = type(defending_pokemon).__name__
        attack_power = attacking_pokemon._attack * self.attack_multiplier(attacking_type, defending_type)
        defense_power = defending_pokemon._defense
        return max(1, int(attack_power - defense_power))

    def fight(self):
        while self.is_alive(self._pokemon1) and self.is_alive(self._pokemon2):
            attacking_pokemon = random.choice([self._pokemon1, self._pokemon2])
            defending_pokemon = self._pokemon2 if attacking_pokemon == self._pokemon1 else self._pokemon1

            if self.attack_hits():
                damage = self.damage_dealt(attacking_pokemon, defending_pokemon)
                defending_pokemon._hp -= damage
                print(attacking_pokemon._name, "inflige", damage, "dégâts à", defending_pokemon._name)
            else:
                print(attacking_pokemon)
