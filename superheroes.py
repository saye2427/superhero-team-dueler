import random

class Ability:
    def _init_(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        # Return attack value
        # Calculate the lowest attack value as an integer
        self.lowest_attack_val = attack_strength // 2
        # Use random.randint(a, b) to select a random attack value.
        self.random_attack = random.randint(lowest_attack_val, attack_strength)
        # Return attack value between 0 and the full attack.
        return random_attack
    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack(self)

class Hero:
    def _init_(self, name):
        # Initialize starting values
        self.abilities = list()
        self.name = name
    def add_ability(self, ability):
        # Add ability to abilities list
        self.ability = ability

        abilities.append(ability)
    def attack(self):
        # Run attack() on every ability hero has
        # Call the attack method on every ability in our ability list
        for ability in abilities:
            attack(ability)
        # Add up and return the total number of attacks

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
