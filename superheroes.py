class Ability:
    def _init_(self, name, attack_strength):
        # Initialize starting values
        self.name = name
        self.attack_strength = attack_strength
    def attack(self):
        # Return attack value
        return attack_strength
    def update_attack(self, attack_strength):
        # Update attack value
        self.attack_strength = attack(self)

class Hero:
    def _init_(self, name):
        # Initialize starting values
        self.name = name
    def add_ability(self, ability):
        # Add ability to abilities list
        abilities = []

        self.ability = ability

        abilities.append(ability)
    def attack(self):
        # Run attack() on every ability hero has
        for ability in abilities:
            attack(ability)
