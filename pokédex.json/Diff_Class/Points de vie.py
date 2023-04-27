def battle_simulation():
    """Lancer une simple simulation interactive de combat Pokémon"""
    mew = Pokemon()
    user_pokemon = Pokemon()
    while True:
        print("\nCHOIX D'ATTAQUE\n1. Attaque à courte portée\n2. Attaque à longue portée\n3. Guérison")
        attack_choice = int(input("\nSélectionnez une attaque : "))
        # NE PAS UTILISER eval sur l'entrée de l'utilisateur, cela peut être dangereux !

        # Mew sélectionne une attaque, mais se concentre sur l'attaque si la santé est pleine.
        mew_choice = random.randint(1, 2 if mew.health == 100 else 3)
        # c'est votre distinction originale juste condensée en une seule ligne

        # Les attaques de l'utilisateur et de Mew sont effectuées simultanément
        # avec les modifications apportées à Pokemon, il n'est pas nécessaire de sauvegarder tous les
        # valeurs intermédiaires de dégâts/soins -> code agréable et court
        if attack_choice != 3:
            print(f"Vous avez infligé {user_pokemon.attack(mew, attack_choice)} dégâts.")

        if mew_choice != 3:
            print(f"Mew a infligé {mew.attack(user_pokemon, mew_choice)} dégâts.")

        if attack_choice == 3:
            print(f"Vous avez guéri {user_pokemon.heal()} points de vie.")

        if mew_choice == 3:
            print(f"Mew a guéri {mew.heal()} points de vie.")

        if mew.health == 0 or user_pokemon.health == 0:
            break

        print(f"Votre état de santé actuel est {user_pokemon.health}")
        print(f"La santé actuelle de Mew est {mew.health}")

    print(f"Votre santé finale est {user_pokemon.health}")
    print(f"La santé finale de Mew est {mew.health}")

    if user_pokemon.health < mew.health:
        print("\nVous avez perdu ! Meilleure chance la prochaine fois !")
    else:
        print("\nTu as gagné contre Mew !")

if __name__ == "__main__":
    battle_simulation()