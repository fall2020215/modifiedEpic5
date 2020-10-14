"""  
Check.py file include classes to check and test input value from users
"""

import student as s
import manage as m

class Password_account:

    #at least 8 characters
    def min_character(self, password):
        if len(password) < 8:
            print("The password needs at least 8 characters")
            return False
        else:
            return True

    #at most 12 characters
    def max_character(self, password):
        if len(password) > 12:
            print("The password needs at most 12 characters")
            return False
        else:
            return True

    #at least one capital letter
    def capital_letter(self, password): 
        if not any(character.isupper() for character in password):
            print("The password needs at least one capital")
            return False
        else:
            return True

    #at least one digit 
    def digit(self, password):
        if not any(character.isdigit() for character in password):
            print("The password needs at least one digit")
            return False
        else:
            return True

    #at least one non_alpha
    def non_alpha(self,password):
        if password.isalnum():
            print("The password needs at least one non-alpha character")
            return False
        else: 
            return True


class Name_Password:

    def name_check(self, user_name):
        manage = m.Manage()
        
        for element in manage.get_list():
            if element.get_user_name() == user_name:
                
                return True

        print("Don't have any account with name:", user_name)
        return False

    def password_check(self, user_name, password):
        manage = m.Manage()

        for element in manage.get_list():
            if element.get_user_name() == user_name and element.get_password() == password:
                return True

        return False

    
class Input_Value:
    #If the value is number (int, float)
    def isNumber(self,input):
        try:
            float(input)
            return True
        except ValueError:
            return False

    def isInt(self,input):
        try:
            int(input)
            return True
        except ValueError:
            return False

#check the value of option input
def check_option(value, low, high):
    p = Input_Value()
    while not p.isInt(value) or int(value) < low or int(value) > high:
        print("\nThe option should be a integer number between " + str(low) + " and " + str(high) + "!")
        print("Try again for your option!\n")
        value = input("Your selection: ")
        
    return value




        



        
