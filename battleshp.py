#    Tak 1 = Set up the game

# Characters (as strings)
wizard = "Wizard"
elf = "Elf"
human = "Human"

# Character HP (as integers):
wizard_hp = 70
elf_hp = 100
human_hp = 150

# Character Damage (as integers):
wizard_damage = 150
elf_damage = 100
human_damage = 20

dragon_damage = 50

# Dragon Stats (as integers):
dragon_hp = 300
dragon_damage = 50


def show_options():
    print("Choose your character:")
    print(f"1) {wizard} - HP: {wizard_hp}, Damage: {wizard_damage}")
    print(f"2) {elf} - HP: {elf_hp}, Damage: {elf_damage}")
    print(f"3) {human} - HP: {human_hp}, Damage: {human_damage}")

while True:
    dragon_hp = 300 

    show_options()
    choice = input("Enter the number of your choice: ")

    if choice.lower() == 'exit':
        print("Thanks for playing! Goodbye!")

    while True:
        if choice == '1':
            character = wizard
            my_hp = wizard_hp
            my_damage = wizard_damage
            break
        elif choice == '2':
            character = elf
            my_hp = elf_hp
            my_damage = elf_damage
            break
        elif choice == '3':
            character = human
            my_hp = human_hp
            my_damage = human_damage
            break
        else:
            print("Unknown character")
            choice = input("Choose your character: ")

    print(f"You have chosen: {character}")
    print(f"Your HP: {my_hp}")
    print(f"Your Damage: {my_damage}")

    # Task 4: Battle with the Dragon

    while True:
        dragon_hp = dragon_hp - my_damage
        print("\nThe", character, "damaged the Dragon!")
        print("Dragon's HP is now:", dragon_hp)

        # Check if the dragon has been defeated
        if dragon_hp <= 0:
            print("The Dragon has been defeated! You win!")
            break  # End the battle loop

        # Dragon attacks the player
        my_hp = my_hp - dragon_damage
        print("The Dragon strikes back!")
        print(character, "'s HP is now:", my_hp)

        # Check if the player has been defeated
        if my_hp <= 0:
            print("You have been defeated! The Dragon wins!")
            break  

    play_again = input("\nDo you want to play again? (yes/no) ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
