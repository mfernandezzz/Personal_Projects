#Build an RPG Character
import re
def create_character(name, strength, intelligence, charisma): 
    #name validation
    if (bool(re.search(r"\d", name))): #check if the name is a string
        return 'The character name should be a string.' #error message
    if len(name) > 10: #check if the name is longer than 10 characters
        return 'The character name is too long.' #error message
    if ' ' in name: #check if the character name contain spaces
        return 'The character name should not contain spaces' #error message
    
    #stats validation
    if not(bool(re.search(r"\d", strength))) or not(bool(re.search(r"\d", intelligence))) or not(bool(re.search(r"\d", charisma))):
        return 'All stats should be integers' #error message
    if (int(strength) < 1) or (int(intelligence) < 1) or (int(charisma) < 1): #check if the stats values are lower than 1
        return 'All stats should be no less than 1' #error message
    if (int(strength) > 4) or (int(intelligence) > 4) or (int(charisma) > 4): #check if one or more stats values are more than 4
        return 'All stats should be no more than 4' #error message
    if (int(strength) + int(intelligence) + int(charisma)) != 7: #check if the sum of all stats are 7
        return 'The character should start with 7 points' #error message
    
    return f"""Character name: {name}\nSTR: {'●' * int(strength)}{'○' * (10 - (int(strength)))}\nINT: {'●' * int(intelligence)}{'○' * (10 - (int(intelligence)))}\nCHA: {'●' * int(charisma)}{'○' * (10 - (int(charisma)))}"""

name = input('Ingrese el nombre del personaje: ')
strength = input('Ingrese el valor de fuerza del personaje: ')
intelligence = input('Ingrese el valor de inteligencia del personaje: ')
charisma = input('Ingrese el valor de charisma del personaje: ')

print(create_character(name, strength, intelligence, charisma))
