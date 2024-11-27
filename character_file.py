import random

# Base Character class
class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.max_health = health  # Store the original health for maximum limit

    def attack(self, opponent):
        opponent.health -= self.attack_power
        print(f"{self.name} attacks {opponent.name} for {self.attack_power} damage!")
        if opponent.health <= 0:
            print(f"{opponent.name} has been defeated!")

    def heal(self):
        heal_amount = 15
        self.health = min(self.max_health, self.health + heal_amount)
        print(f"{self.name} heals for {heal_amount}. Current health: {self.health}/{self.max_health}")

    def display_stats(self):
        print(f"{self.name}'s Stats - Health: {self.health}/{self.max_health}, Attack Power: {self.attack_power}")


# Warrior class
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, health=140, attack_power=25)
        self.shield_active = False

    def quick_shot(self, opponent):
      
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Quick Shot for {damage} damage!")

    def shield(self):
        self.shield_active = True
        print(f"{self.name} activates Shield! Next attack will be blocked.")


# Mage class
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, health=100, attack_power=35)

    def arrow(self, opponent):
       
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Arrow for {damage} damage!")

    def power_punch(self, opponent):
        
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Power Punch for {damage} damage!")


# Archer class
class Archer(Character):
    def __init__(self, name):
        super().__init__(name, health=110, attack_power=50)

    def force_kick(self, opponent):
       
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} uses Force Kick for {damage} damage!")

    def drop_kick(self, opponent):
       
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Drop Kick for {damage} damage!")


# Paladin class
class Paladin(Character):
    def __init__(self, name):
        super().__init__(name, health=120, attack_power=40)

    def light_bomb(self, opponent):
     
        damage = self.attack_power * 3
        opponent.health -= damage
        print(f"{self.name} uses Light Bomb for {damage} damage!")

    def tear_potion(self, opponent):
        
        damage = self.attack_power * 2
        opponent.health -= damage
        print(f"{self.name} uses Tear Potion for {damage} damage!")


# EvilWizard class
class EvilWizard(Character):
    def __init__(self, name):
        super().__init__(name, health=150, attack_power=15)

    def regenerate(self):
        self.health += 2
        print(f"{self.name} regenerates 2 health! Current health: {self.health}")



    
