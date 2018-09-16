import random

class Hero:
    def __init__(self, name):
        # Initialize starting values
        self.abilities = []
        self.name = name
    def add_ability(self, ability):
        # Add ability to abilities list
        self.ability = ability

        self.abilities.append(ability)
    def attack(self):
        # Run attack() on every ability hero has
        self.num_attacks = 0
        # Call the attack method on every ability in our ability list
        for x in self.abilities:
            x.attack()
        # Add up and return the total number of attacks
            self.num_attacks += 1
        return self.num_attacks

class Ability:
    def __init__(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        # Return attack value
        # Calculate the lowest attack value as an integer
        self.lowest_attack_val = self.attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        self.random_attack = random.randint(self.lowest_attack_val, self.attack_strength)
        # Return attack value between 0 and the full attack.
        return self.random_attack
    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = random_attack.attack()

def test():
    if __name__ == "__main__":
        hero = Hero("Wonder Woman")
        print(hero.attack())
        ability = Ability("Divine Speed", 300)
        hero.add_ability(ability)
        print(hero.attack())
        new_ability = Ability("Super Human Strength", 800)
        hero.add_ability(new_ability)
        print(hero.attack())

test()
