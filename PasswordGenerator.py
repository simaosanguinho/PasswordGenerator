''' There are two types of Passwords: 
    Numeric - with numbers
    Alphabetic - with chars
    Mixed - numbers and chars
    Fancy - with chars, numbers and specials chars.
'''



import constant
import random, time


def getChar():
    x = random.randint(0, constant.ABC_LEN-1)
    return constant.ABC[x]

def getSpecialChar():
    x = random.randint(0, constant.SPECIAL_CHARS_LEN-1)
    return constant.SPECIAL_CHARS[x]

def getNumber():
    x = random.randint(0, constant.NUMBERS_LEN-1)
    return constant.NUMBERS[x]

def getAnyKey():
    x = random.randint(0, 2) 

    if x == 0:
        return getChar()
    elif x == 1:
        return getSpecialChar()
    else:
        return getNumber()

def getCharOrSpecialChar():
    x = random.randint(0, 1)

    if x == 0:
        return getChar()
    else: 
        return getSpecialChar()

def getCharOrNumber():
    x = random.randint(0, 1)

    if x == 0:
        return getChar()
    else: 
        return getNumber()

def getNumericPassword(length):

    password = ''

    for i in range(length):
        password = password + getNumber()

    return password

def getAlphabeticPassword(length):
    password = ""
    for i in range(length):
        password = password + getChar()

    return password

def getMixedPassword(length):
    password = ""
    for i in range(length):
        password = password + getCharOrNumber()

    return password

def getFancyPassword(length):
    password = ""
    for i in range(length):
        password = password + getAnyKey()

    return password




def getPassword(chars, nums, spc_chars, length):
    if chars == 'yes':
        if nums == 'yes':
            if spc_chars == 'yes':
                return getFancyPassword(length)

            return getMixedPassword(length)

        return getAlphabeticPassword(length)

    elif nums == 'yes':
        return getNumericPassword(length)

    

def PasswordGenerator():

    
    length = input("How long should the password be:\n")
    chars = input("Should it contain characters? (yes/no)\n")
    nums = input("Should it contain numbers? (yes/no)\n")
    spc_chars = input("Should it contain special characters? (yes/no) \n")

    
    password = getPassword(chars, nums, spc_chars, int(length))
        
    print(password)



# main
print(constant.INITIAL_MESSAGE)

PasswordGenerator()

