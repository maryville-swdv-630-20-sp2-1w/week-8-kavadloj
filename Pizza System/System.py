from datetime import datetime
from Items import *
from Users import *

#Singleton
class Cart():
    __instance = None

    def getInstance():
        if Cart.__instance == None:
            Cart()
        return Cart.__instance
    
    def __init__(self):
        if Cart.__instance != None:
            raise Exception("There can only be one cart!")
        else:
            Cart.__instance = self
        self.cart = []
 
    def get_total_price(self):
        total_price = 0
        for item in self.cart: 
            total_price += (item.get_price() * float(item.get_quantity()))
        return round(total_price, 2)
    
    def get_cart(self):
        cart_items = []
        for item in self.cart: 
            cart_items.append(item.get_name())
        return cart_items
    
    def add_item(self, menu_item):
        self.cart.append(menu_item)

#Facade
class Checkout():
    def __init__(self, cart, user, card):
        self.cart = cart
        self.user = user
        self.card = card

    #Combine shipment verification into one method:
    def get_verif_info(self):
        return "Cart items: " + str(self.cart.get_cart()) + " will be shipped to " + self.user.get_address()
    
    #Combine payment validation into one method:
    def validate_card(self):
        valid_payment = False
        if(self.card.validate_num() and self.card.validate_date() and self.card.validate_sec_code()):
            valid_payment = True
            return valid_payment
    
    def purchase(self):
        return "Your order has been placed. $" + str(self.cart.get_total_price()) + " has been charged to your card."
