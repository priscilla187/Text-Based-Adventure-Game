class Room():
    def __init__(self, room_name):
        # Initialize the room with a name, description, and empty linked rooms and character
        self.name = room_name
        self.description = None
        self.linked_rooms = {}  # Dictionary to hold linked rooms
        self.character = []
        self.item = None  # Add an item attribute
        self.hint = None
        self.money = None

    def set_hint(self, hint):
        self.hint = hint

    def get_hint(self):
        return self.hint

    def set_money(self, money):
        self.money = money

    def get_money(self):
        return self.money

    def set_description(self, description):
        self.description = description

    def set_character(self, character):
        if isinstance(character, list):
            self.character.extend(character)  # Add multiple characters
        else:
            self.character.append(character)  # Add a single character

    def get_character(self):
        return self.character  # Return all characters in the room

    def remove_character(self, character):
        if character in self.character:
            self.character.remove(character)  # Remove a character

    def set_item(self, item):  # Method to set an item in the room
        self.item = item

    def get_item(self):  # Method to get the item from the room
        return self.item
        
    def get_description(self):
        # Return the room's description
        return self.description
    
    def set_description(self, room_description): 
         # Set the room's description
        self.description = room_description

    def describe(self):
         # Print the room's description
        print(self.description)

    def set_name(self, room_name):
         # Set the room's name
        self.name = room_name

    def get_name(self):
         # Return the room's name
        return self.name

    def set_character(self, new_character):
         # Set the character in the room
        self.character = new_character

    def get_character(self):
         # Return the character in the room   
        return self.character

    def link_room(self, room_to_link, direction):
        # Link another room in a specified direction
        self.linked_rooms[direction] = room_to_link

    def get_details(self):
        # Print the room's details including name, description, and linked rooms
        print(self.name)
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print(self.description)
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.get_name()} is {direction}")

    def move(self, direction):
         # Move to a linked room if it exists in the specified direction
        if direction in self.linked_rooms:
            print(f"Moving {direction} to {self.linked_rooms[direction].get_name()}") 
            return self.linked_rooms[direction]  # Return the linked room
        else:
            print(f"Can't go {direction} from {self.name}")
            return None 






