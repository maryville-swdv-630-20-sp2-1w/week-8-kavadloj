#Generic Item parent class
class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return self.name + ', ' + '$' + str(self.price) + ' x ' + str(self.quantity)

    def get_description(self):
        return 'No description available.'
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def set_quantity(self, new_quantity):
        self.quantity = new_quantity
    
    def get_quantity(self):
        return self.quantity  

    
#Builder
class BuildPizza(Item):
    def __init__(self):
        Item.__init__(self, 'Pizza', 6.99, 0)
    
        self.crust = None
        self.size = None
        self.toppings = []
    
    def __str__(self):
        return self.crust + ", " + self.size + ", " + str(self.toppings) + ' x ' + str(self.quantity)
       
    def get_description(self):
        return 'Hand-tossed crust topped with sauce and cheese, with toppings of your choice. $6.99 Each.'

    def get_price(self):
        return self.price

    def choose_crust(self, crust_style):
        self.crust = crust_style
    
    def choose_size(self, new_size):
        self.size = new_size
        
    def add_toppings(self, new_topping):
        self.toppings.append(new_topping)

            
class Breadsticks(Item):
    def __init__(self, sauce):
        Item.__init__(self, 'Breadsticks', 4.99, 0)
        self.sauce = sauce

    def __str__(self):
        return self.name + ', ' + '$' + str(self.price) + ", " + str(self.sauce) + ' x ' + str(self.quantity)
    
    def get_description(self):
        return 'Handmade from fresh buttery-tasting dough and baked to a golden brown. $4.99 for 6.'
    
    def set_sauce(self, new_sauce):
        self.sauce = new_sauce
        
    def get_sauce(self):
        return self.sauce
    
class Salad(Item):
    def __init__(self, dressing):
        Item.__init__(self, 'Salad', 3.99, 0)
        self.dressing = dressing
    
    def __str__(self):
        return self.name + ', ' + '$' + str(self.price) + ", " + str(self.dressing) + ' x ' + str(self.quantity)
    
    def get_description(self):
        return 'A crisp combination of tomatoes, onion, carrots, cheese and brioche garlic croutons, all atop a blend of romaine and iceberg lettuce. $3.99 each.'
    
    def set_dressing(self, new_dressing):
        self.dressing = new_dressing
        
    def get_dressing(self):
        return self.dressing
