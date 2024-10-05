import pygame
from room import Room
from character import Enemy, Character, Accomplice
from item import Key, Hint, Money

# Initialize pygame's mixer for sound playback
pygame.mixer.init()

# Game description function
def game_description():
    print("WELCOME TO THE RESIDENT EVIL TEXT BASE GAME")
    print("===========================================")
    print("\nSTORY:")
    print("You are Ethan Winters, an ordinary man forced into horrifying situations. Your wife, Mia, "
          "has gone missing, and your search has led you to an eerie mansion. "
          "Inside, you will face grotesque enemies, including mutants and twisted beings that will stop "
          "at nothing to defeat you.")
    print("\nAIM OF THE GAME:")
    print("The goal is to explore the mansion and defeat enemies"
          "You must find a key to unlock the main door of the mansion, You must find a key to unlock the main door, but you cannot move forward unless the enemy in the current room is defeated.")
    print("\nMAIN CHARACTERS:")
    print("1. **Ethan Winters** - The protagonist of the game, a man desperately searching for his wife.")
    print("2. **Jack Barker** - A relentless mutant who hunts Ethan through the mansion.")
    print("3. **Zoe Baker** - An accomplice who helps Ethan via phone, giving crucial hints for survival.")
    print("4. **Lickers** - Grotesque mutants with exposed brains and deadly tongues.")
    print("5. **Chainsaw Man** - A terrifying figure wielding a chainsaw, ready to end Ethan's life.")
    print("\nGAME CONTROLS:")
    print("• 'north', 'south', 'east', 'west' - Move in that direction.")
    print("• 'talk' - Speak to a character in the room.")
    print("• 'fight' - Engage in combat with an enemy.")
    print("• 'interact' - Interact with a character or object.")
    print("• 'take' - Collect an item in the room.")
    print("• 'use key' - Use the key to unlock a door if you have one.")
    print("• 'hint' - Use the hint to help you defeat an enemy in the room.")
    print("• 'take money' - Use the take money action to save up and buy better armoury"
          "this feature to actually use the money will be implimented in level 2!).")
    print("\nYour journey begins now. Will you make it out alive?")

# Load and play background music
pygame.mixer.music.load('eerie_music.mp3') 
pygame.mixer.music.play(-1)  # Play the music in an infinite loop

# Display the game description
game_description()

# Prompt the player to start the game
while True:
    start_command = input("\nType 'start' to begin the game: ").lower().strip()
    if start_command == "start":
        break
    else:
        print("Invalid command. Please type 'start' to begin the game.")

game_active = True 

# Define the rooms
main_hall = Room("Main Hall")
kennel_room = Room("Kennel Room")
gallery_room = Room("Gallery Room")
creepy_basement = Room("Creepy Basement")

# Set room descriptions
main_hall.set_description("A vast, imposing hall with grand staircases, lit dimly by antique chandeliers...")
kennel_room.set_description("The metallic scent of blood fills the air. The once orderly cages are now empty...")
gallery_room.set_description("Lined with disturbing portraits of the mansion's previous residents, the gallery...")
creepy_basement.set_description("The basement is damp, with the faint sound of dripping water echoing...")

# Create and set the enemy characters
jack_barker = Enemy("Jack Barker", "A relentless mutant")
jack_barker.set_conversation("You think you can hurt me?")
jack_barker.set_weakness("chainsaw", "fire", "acid")
jack_barker.set_interactions("loot enemy", "analyze", "fight", "block", "counterattack")
main_hall.set_character(jack_barker)

lickers = Enemy("Lickers", "Grotesque mutants with exposed brains and large tongues...")
lickers.set_conversation("Unsettling growls and screeches.")
lickers.set_weakness("shotgun", "sound")
lickers.set_interactions("loot enemy", "analyze", "fight", "block", "counterattack")
kennel_room.set_character(lickers)

chainsaw_man = Enemy("Chainsaw man", "Dr. Salvador is a villager equipped with a chainsaw...")
chainsaw_man.set_conversation("Aggressive chainsaw-revving")
chainsaw_man.set_weakness("shotgun", "rifles", "grenades")
chainsaw_man.set_interactions("loot enemy", "analyze", "fight", "block", "counterattack")
gallery_room.set_character(chainsaw_man)

# Create and set the character in the main hall
ethan_winters = Character("Ethan Winters", "An ordinary man thrust into horrifying situations...")
ethan_winters.set_conversation("I just want my wife back!")
ethan_winters.set_interactions("loot enemy", "analyze", "fight", "block", "counterattack")
creepy_basement.set_character(ethan_winters)

# Create key
mansion_key = Key()  # Default key for the main door

# Set key in the room
main_hall.set_item(mansion_key)  # Key for the main door

# Hints for different rooms
creepy_basement_hint = Hint("This room seems too quiet... if you find yourself in the Kennel room next. A loud noise might startle what lurks here. Use something that can create a ruckus.")
gallery_room_hint = Hint("Look closely at the art. There is more here than meets the eye. A sharp weapon might be the key to unraveling this mystery.")
kennel_room_hint = Hint("This beast thrives in the shadows but recoils at sudden noises. Something that packs a punch might bring it down.")
main_hall_hint = Hint("When facing an overwhelming foe, think big! An explosive surprise might give you the upper hand, but be careful not to catch yourself in the blast!")

# Set hints in rooms
creepy_basement.set_hint(creepy_basement_hint)
gallery_room.set_hint(gallery_room_hint)
kennel_room.set_hint(kennel_room_hint)
main_hall.set_hint(main_hall_hint)

# Money for different rooms
creepy_basement_money = Money(100)  # $100 in Creepy Basement
gallery_room_money = Money(200)  # $200 in Gallery Room
kennel_room_money = Money(50)  # $50 in Kennel Room

# Set money in rooms
creepy_basement.set_money(creepy_basement_money)
gallery_room.set_money(gallery_room_money)
kennel_room.set_money(kennel_room_money)

# Create Zoe Baker (Accomplice)
zoe_baker = Accomplice("Zoe Baker", "Contacts Ethan via phone and helps him navigate the Baker estate.")

# Define room-specific Zoe Baker conversations in a dictionary
zoe_conversations = {
    main_hall: "You made it to the Main Hall. Good. But you are not out yet. There is a way out, through the main door, but you need to find the key. Look around. You do not have much time before Jack finds you again.",
    kennel_room: "I do not know what is in there, but it does not sound good. Stay low and move quietly. There might be something you can use, but be careful. They do not play nice here.",
    gallery_room: "You have made it to the gallery? Good. There should be something hidden there, but watch out. There is more to those paintings than meets the eye.",
    creepy_basement: "The basement… it is dangerous. Stay sharp. There is no telling what you will find down there. And for Gods sake, keep moving."
}

# Link rooms together
creepy_basement.link_room(gallery_room, "east")
creepy_basement.link_room(kennel_room, "south")
creepy_basement.link_room(main_hall, "west")

# Reverse links for the connected rooms
gallery_room.link_room(creepy_basement, "west")
kennel_room.link_room(creepy_basement, "north")
main_hall.link_room(creepy_basement, "east")  # Link back to Creepy Basement from Main Hall

# Track the player's inventory
player_inventory = {
    "keys": []  # Use a list to hold collected keys
}

# Track the player's defeated enemies and collected key
player_inventory = {"key": False}
defeated_enemies = set()

# Start the game in the creepy basement
current_room = creepy_basement

def fight_enemy(enemy, combat_item):
    if combat_item in enemy.get_weaknesses():
        return True
    else:
        return False

# Game loop
while True:
    print("\n")
    current_room.get_details()
    print(f"You are currently in: {current_room.get_name()}")

    # Check for item in the room
    if current_room.get_item() is not None:
        print(f"You see a {current_room.get_item().get_name()} here.")

    # Trigger Zoe's conversation based on Ethan's current location using dictionary lookup
    if current_room in zoe_conversations:
        zoe_baker.set_conversation(zoe_conversations[current_room])
        zoe_baker.talk()

    enemy = current_room.get_character()

    # If all enemies are defeated and the player finds the key
    if all([main_hall.get_character() is None, kennel_room.get_character() is None, gallery_room.get_character() is None]) and player_inventory["key"]:
        print("You have found the key and defeated all enemies!")
        print("YOU HAVE DEFEATED LEVEL 1! Are you ready for Level 2?")
        next_level = input("Type 'yes' to proceed to Level 2, or 'no' to quit: ").lower().strip()
        if next_level == "yes":
            print("Level 2 coming soon... Stay tuned!")
            break  
        else:
            print("Thanks for playing!")
            break

    command = input("Type 'talk', 'fight', 'interact', 'take', 'use key', 'hint', 'take money', or a direction (north, south, east, west): ").lower().strip()

    if command == "hint":
        hint = current_room.get_hint()
        if hint is not None:
            print(f"Hint: {hint.get_description()}")
            current_room.set_hint(None)  # Optionally remove the hint after taking it
        else:
            print("There are no hints available in this room.")

    # Handling the money pickup
    elif command == "take money":
        money = current_room.get_money()  # Assume you have a method to get money from the room
        if money is not None:
            print(f"You found {money.get_name()}!")
            ethan_winters.collect_item(money)  # Collect the money
            current_room.set_money(None)  # Remove the money from the room after it's taken
        else:
            print("There's no money to take in this room.")

    # Handling other item pickups (keys, hints)
    elif command == "take":
        if current_room.get_item() is not None:
            item = current_room.get_item()  # Get the item in the room
            
            # Handle the item if it's a Key and in the Main Hall
            if isinstance(item, Key) and current_room == main_hall:
                ethan_winters.collect_item(current_room.get_item())  # Ethan collects the item
                print(f"You took the {current_room.get_item().get_name()}.")
                player_inventory["key"] = True
                current_room.set_item(None)  # Remove the key from the room 

                # Handle the case if the item is a Hint
            elif isinstance(item, Hint):
                print(f"You found a hint: {item.get_description()}")
                current_room.set_item(None)  # Remove the hint after taking it
            
            # Handle the case if the item is Money
            elif isinstance(item, Money):
                print(f"You found ${item.get_amount()}!")
                current_room.set_item(None)  # Remove the money after taking it

            # If the item is a Key but NOT in the Main Hall, prevent the player from taking it                 
            elif isinstance(item, Key) and current_room != main_hall:
                print("You can't take the key yet; defeat all enemies in the level first!")
            
            # Handle any other items or no items
            else:
                print("There's nothing to take in this room.")
        else:
            print("There's nothing to take in this room.")

    elif command == "use key":
        if player_inventory.get("key", False):  # Check if the inventory contains the key
            print("You used the key to unlock the door!")
            # Implement door unlocking logic here
            # Logic to change the room or mark the door as unlocked goes here
        else:
            print("You don't have any keys!")

    elif command == "talk":
        if enemy is not None:
            enemy.talk()
        else:
            print("There's no one to talk to in this room.")

    elif command == "fight":
        if enemy is not None and isinstance(enemy, Enemy):
            fight_with = input("What will you fight with? ").strip().lower()
            if fight_enemy(enemy, fight_with):
                print(f"You defeated {enemy.name}!")
                current_room.set_character(None)
                defeated_enemies.add(current_room)
                # If all enemies in the level are defeated, allow key retrieval in Main Hall
                if current_room == main_hall and not player_inventory.get("key", False):
                    print("You can now collect the key!")
            else:
                print(f"{enemy.name} defeated you!")
                print("GAME OVER")
                game_active = False  # Set a flag to indicate the game is over
        else:
            print("There's no one to fight in this room.")

    elif command == "interact":
        if enemy is not None:
            interactions = enemy.get_interactions()
            interaction_choice = input(f"Possible interactions: {', '.join(interactions)}\nChoose an interaction: ").strip().lower()
            if interaction_choice in interactions:
                print(f"You chose to {interaction_choice} {enemy.name}.")
            else:
                print("Invalid interaction.")
        else:
            print("There's no one to interact with.")

    elif command in ["north", "south", "east", "west"]:
        new_room = current_room.move(command)
        if new_room is not None:
            current_room = new_room
        else:
            print("You can't go that way!")

    else:
        print("Invalid command. Type 'talk', 'fight', 'interact', 'take', 'hint', 'take money', or a direction (north, south, east, west).")

    # After handling commands, check if the game is still active
    if not game_active:
        # End game logic 
        print("Thank you for playing!")

# Stop the music when the game ends
pygame.mixer.music.stop()
pygame.quit()



