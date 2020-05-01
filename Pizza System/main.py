from Items import *
from System import *
from Users import *

# Collect info for user object
input("Welcome to the Python Pizza system! Create an account to begin. [Press enter]")
name = input("Enter your name: ")
email = input("Enter your email: ")
address = input("Enter your delivery address: ")

user = User(name, email, address)
cart = Cart()

# Display menu and present with options
input("Welcome, " + name + "! Proceed to view the menu [Enter]")

choice = ""
while(choice.lower() != "c"):
    print("\nMenu options: \n > Build a pizza\n > Breadsticks\n > Salad\n")
    choice = input("Select option to view [pizza/breadsticks/salad] or continue [c]: ")
    
    if(choice.lower() == "pizza"):
        pizza = BuildPizza()
        print(pizza.get_description())
        size = input("What size pizza would you like? ")
        pizza.choose_size(size)
        crust = input("What kind of crust would you like? ")
        pizza.choose_crust(crust)
        topping_choice = input("Toppings? [yes/no] ")
        
        while(topping_choice.lower() != "no"):
            topping = input("What topping would you like to add? ")
            pizza.add_toppings(topping)
            topping_choice = input("Add another topping? [yes/no] ")
        
        quantity = input("How many do you want? ")
        pizza.set_quantity(quantity)
        print("\nYour pizza specifications are: ")
        print(pizza)
        cart_choice = input("Add to cart or discard? [add/discard] ")
        
        if(cart_choice.lower() == "add"):
            cart.add_item(pizza)
            input("The pizza was added to your cart [Enter] ")
        else:
            input("The pizza was not added to your cart [Enter] ")
    
    elif(choice.lower() == "breadsticks"):
        breadsticks = Breadsticks("None")
        print(breadsticks.get_description())
        sauce = input("What dipping sauce do you want? ")
        breadsticks.set_sauce(sauce)
        quantity = input("How many do you want? ")
        breadsticks.set_quantity(quantity)
        print("\nYour breadstick specifications are: ")
        print(breadsticks)
        cart_choice = input("Add to cart or discard? [add/discard] ")
        
        if(cart_choice.lower() == "add"):
            cart.add_item(breadsticks)
            input("The breadsticks were added to your cart [Enter] ")
        else:
            input("The breadsticks were not added to your cart [Enter] ")
        
    elif(choice.lower() == "salad"):
        salad = Salad("None")
        print(salad.get_description())
        
        dressing = input("What dressing do you want? ")
        salad.set_dressing(dressing)
        quantity = input("How many do you want? ")
        salad.set_quantity(quantity)
        print("\nYour salad specifications are: ")
        print(salad)
        cart_choice = input("Add to cart or discard? [add/discard] ")
        
        if(cart_choice.lower() == "add"):
            cart.add_item(salad)
            input("The salad was added to your cart [Enter] ")
        else:
            input("The salad was not added to your cart [Enter] ")
 
# Checkout stage
input("You will now proceed to checkout [Enter]")
print("Your cart contains: " + str(cart.get_cart()))
input("The total price is $" + str(cart.get_total_price()) + " [Enter] ")

verify_cart = input("Is this acceptable? [yes/no] ")
if(verify_cart.lower() == "yes"):
    print("\nFor payment, please enter valid credit card information.")
    
    paymentIsValid = False
    
    # Payment validation step. Sample valid card details: ["4012888888881881", "8/5/2021", "321"]
    while(paymentIsValid != True):
        card_num = input(" > Enter your credit card number: ")
        card_date = input(" > Enter your credit card expiration date: ")
        sec_code = input(" > Enter the 3-digit security code: ")
        card = CreditCard(card_num, card_date, sec_code)
        
        checkout = Checkout(cart, user, card)
        print("Verifying payment........")
        paymentIsValid = checkout.validate_card()
        if(paymentIsValid != True):
            input("Credit card is not valid. Please enter valid credit card details. [Enter] ")
    
    print("Credit card details are valid.")
    verify_info = input(checkout.get_verif_info() + ". Continue? [yes/no] ")
    
    #Verify purchase
    if(verify_info == "yes"):
        print(checkout.purchase())
        print("Thank you for your order, " + name + "! A confirmation email will be sent to " + email + ".")
    elif(verify_info == "no"):
        print("Your order has been canceled.")
        
#Cancel order
elif(verify_cart.lower() == "no"):
    print("Your order has been canceled.")
        