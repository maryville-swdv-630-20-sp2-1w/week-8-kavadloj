from datetime import datetime

class User():
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_email(self):
        return self.email
    
    def get_address(self):
        return self.address

class CreditCard():
    def __init__(self, card_number, card_date, sec_code):
        self.card_number = card_number
        self.card_date = card_date
        self.sec_code = sec_code
        
    def get_card_number(self):
        return self.card_number
    
    def get_card_date(self):
        return self.card_date
    
    def get_sec_code(self):
        return self.sec_code
        
    def validate_num(self):
        valid_num = False
        if(self.card_number[0] == "4"):
            valid_num = True
        return valid_num

    def validate_date(self):
        user_date = datetime.strptime(self.card_date, "%d/%m/%Y")
        present = datetime.now()
        valid_date = False
        if(user_date.date() > present.date()):
            valid_date = True
        return valid_date
        
    def validate_sec_code(self):
        valid_code = False
        if(len(self.sec_code) == 3):
            valid_code = True
        return valid_code
        