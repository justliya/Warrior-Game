from character_file import *

# Function to create a character
def create_character():
    print("Choose your character class:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Archer")
    print("4. Paladin")

    class_choice = input("Enter the number of your class choice: ")
    name= input('What is the characters name?:')

    if class_choice == '1':
        return Warrior(name)
    elif class_choice == '2':
        return Mage(name)
    elif class_choice == '3':
        return Archer(name)
    elif class_choice == '4':
        return Paladin(name)
    else:
        print("Invalid choice. Defaulting to Warrior.")
        return Warrior(name)


def battle(player, opponent):
    while player.health > 0 and opponent.health > 0:
        # Attacker damages the defender
        #opponent.health -= player.attack_power
        # Swap roles: defender becomes attacker
        #player, opponent = opponent, player
        print("\n--- Your Turn ---")
        print("1. Attack")
        print("2. Heal")
        print("3. View Stats")
        print("4. Use Special Ability")  # Added this option

        choice = input("Choose an action: ")

        if choice == '1':
            player.attack(opponent)
        elif choice == '2':
            player.heal()
        elif choice == '3':
            player.display_stats()
        elif choice == '4':
            # Handle special abilities based on the player's class
            if isinstance(player, Warrior):
                print("1. Quick Shot")
                print("2. Shield")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.quick_shot(opponent)
                elif ability_choice == '2':
                    player.shield()
                else:
                    print("Invalid choice.")
            elif isinstance(player, Mage):
                print("1. Arrow")
                print("2. Power Punch")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.arrow(opponent)
                elif ability_choice == '2':
                    player.power_punch(opponent)
                else:
                    print("Invalid choice.")
            elif isinstance(player, Archer):
                print("1. Force Kick")
                print("2. Drop Kick")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.force_kick(opponent)
                elif ability_choice == '2':
                    player.drop_kick(opponent)
                else:
                    print("Invalid choice.")
            elif isinstance(player, Paladin):
                print("1. Light Bomb")
                print("2. Tear Potion")
                ability_choice = input("Choose an ability: ")
                if ability_choice == '1':
                    player.light_bomb(opponent)
                elif ability_choice == '2':
                    player.tear_potion(opponent)
                else:
                    print("Invalid choice.")

        # Opponent's turn
        if opponent.health > 0:
            print(f"\n--- {opponent.name}'s Turn ---")
            opponent.attack(player)
            opponent.regenerate()

    # End of battle
    if player.health <= 0:
        print(f"{player.name} has been defeated!")
    else:
        print(f"{opponent.name} has been defeated!")

# Main function
def main():
    player = create_character()
    opponent= EvilWizard('EvilWizard')
    battle(player, opponent)


if __name__ == "__main__":
    main()