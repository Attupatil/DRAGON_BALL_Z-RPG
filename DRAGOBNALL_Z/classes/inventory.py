class Item:
    """
    Base class for Item creation.
    Takes arguments self, name, type, description, and prop
    """
    def __init__(self, name, type, description, prop):
        # defines item name
        self.name = name
        # defines item type (potion, elixir, attack)
        self.type = type
        # defines item description
        self.description = description        
        self.prop = prop
