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

# Dragon Stats (as integers):
dragon_hp = 300
dragon_damage = 50


def show_options():
    print("Choose your character:")
    print(f"1) {wizard} - HP: {wizard_hp}, Damage: {wizard_damage}")
    print(f"2) {elf} - HP: {elf_hp}, Damage: {elf_damage}")
    print(f"3) {human} - HP: {human_hp}, Damage: {human_damage}")


show_options()
choice = input("Enter the number of your choice: ")

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
