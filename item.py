class Item:
    def __init__(self):
        self.name = None
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

class Key(Item):  # Inheriting from the Item class
    def __init__(self, name="Mansion Key"):
        super().__init__()  # Call the parent class constructor
        self.set_name(name)  # Set the key's name using the passed parameter
        self.set_description("An antique key with an elaborate design. It feels heavier than it should, as if the secrets it unlocks have been weighing it down for years. Its handle is shaped like a lion's head, the symbol of the mansion's long-lost grandeur.")

# Define the Hint class
class Hint(Item):
    def __init__(self, hint_text):
        super().__init__()
        self.set_name("Hint")
        self.set_description(hint_text)

# Define the Money class
class Money(Item):
    def __init__(self, amount):
        super().__init__()
        self.set_name("Money")
        self.set_description(f"An amount of ${amount} cash.")
        self.amount = amount

    def get_amount(self):
        return self.amount
    
    def get_name(self):
        return f"${self.amount}"
   

