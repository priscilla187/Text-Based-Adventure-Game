class Character:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.interactions = []  # Initialize an empty list for interactions
        self.conversation = ""  # Initialize conversation attribute

    def set_interactions(self, *interactions):
        self.interactions.extend(interactions)  # Add interactions to the list
        self.inventory = []  # Initialize an empty inventory

    def get_interactions(self, *interactions):
        self.interactions.extend(interactions) # Add interactions to the list

    def get_interactions(self):
        return self.interactions  # Return the list of interactions

    def talk(self):
        print(f"{self.name}: {self.conversation}")

    def set_conversation(self, conversation):
        self.conversation = conversation  # Set the conversation text

    def collect_item(self, item):
        self.inventory.append(item)  # Add item to inventory

    def get_inventory(self):
        return [item.get_name() for item in self.inventory]  # Return the names of items in inventory

    def fight(self, combat_item):
        # Default fight behavior for non-enemies
        print(f"{self.name} doesn't want to fight you.")
        return False  # Return False to indicate no combat happens

class Enemy(Character):  # Enemy inherits from Character
    def __init__(self, name, description):
        super().__init__(name, description)
        self.weaknesses = []
    
    def set_weakness(self, *weaknesses):
        self.weaknesses.extend(weaknesses)  # Add weaknesses to the list

    def get_weaknesses(self):
        return self.weaknesses

    def set_interactions(self, *interactions):
        self.interactions = list(interactions)

    def get_interactions(self):
        return self.interactions
    
class Accomplice(Character):  # Inherit from Character class
    def __init__(self, name, description):
        super().__init__(name, description)  # Use parent class initialization

    # Talk method to display Zoe's conversations
    def talk(self):
        print(f"{self.name}: {self.conversation}")

    # Set Zoe's conversation for each room or scenario
    def set_conversation(self, conversation):
        self.conversation = conversation

     


      
      


      