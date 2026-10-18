
import secrets
import random

def get_int_value(max = False, max_n = 0 , min = False , min_n = 0):
    while(True):
        try:
             value = int(input())
             if(max and value not in range(0 , max_n + 1)):
                  raise ValueError
             if(min and value < min_n):
                  raise ValueError
             return value
        except ValueError:
             print("PLease Enter a Correct int value")

        
    
def get_yesno_value():
     while(True):
        try:
          value = input().strip().lower()
          if(value not in ["y" , "n"]):
               raise ValueError
          return value
        except ValueError:
              print("PLease Enter a Correct (y/n) value")
def get_user_pref():
    print("how many passwords to generate? max:50")
    numberOfPasswords = get_int_value(max = True , max_n=50)
    print("passwords length? max:50 , min = 3")
    passwordLength = get_int_value(max= True , max_n= 50 ,min=True, min_n=3)
    print("Include uppercase letters? (y/n)")
    uppercaseLetters = get_yesno_value() 
    print("Include numbers? (y/n)")
    numbers = get_yesno_value() 
    print("Include symbols? (y/n)")
    symbols = get_yesno_value()

    return {"nop" : int(numberOfPasswords) , "pl" : int(passwordLength) , "uc" : uppercaseLetters , "n" : numbers , "sym" : symbols}


pref = get_user_pref()
def generate_passwords(pref):
    allowed = "abcdefghijklmnopqrstuvwxyz"
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    symbols = "!@#$%^&*"
    if(pref["uc"] == "y"):
            allowed += uppercase
    if(pref["n"] == "y"):
           allowed += digits
    if(pref["sym"] == "y"):
           allowed += symbols
       
           
    generatedPassword = []
    for i in range(pref["nop"]):
        password = []
        if(pref["uc"] == "y"):
            password.append(secrets.choice(uppercase))
        if(pref["n"] == "y"):
            password.append(secrets.choice(digits))
        if(pref["sym"] == "y"):
            password.append(secrets.choice(symbols))
        for j in range(pref["pl"] - len(password)):
            password.append(secrets.choice(allowed))
        random.SystemRandom().shuffle(password)
        generatedPassword.append("".join(password))

    return generatedPassword

print(generate_passwords(pref))

