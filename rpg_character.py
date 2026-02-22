#Build the creation of an RPG Character
#If all values pass the verification, the function should return a string with four lines:
#the first line should contain the character name
#lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of 
#the stat, and a number of empty dots (○) to reach 10. The dots are given in the editor.
#Here's the string that should be returned by create_character('ren', 4, 2, 1):
#ren
#STR ●●●●○○○○○○
#INT ●●○○○○○○○○
#CHA ●○○○○○○○○○
full_dot = '●'
empty_dot = '○'

def create_character(name, strength=0, intelligence=0, charisma=0):
    if not(isinstance(name, (str))): #check if the name parameter is a string
        return 'The character name should be a string' #error message if the parameter name not contains a string
    
    #if (isinstance(name, (int, float, bool))):
    #    return 'The character name should be a string'
    
    if name == '': #check if the name parameter is a empty string
        return 'The character should have a name' #error message if name is a empty string
    
    if len(name) > 10: #check if the name parameter have more than 10 characters
        return 'The character name is too long' #error message if name have more than 10 characters
    
    if ' ' in name: #check if the name parameter contains spaces
        return 'The character name should not contain spaces' #error message if the name parameter contains spaces

    if not(isinstance(strength, (int))) or not(isinstance(intelligence, (int))) or not(isinstance(charisma, (int))): #check if str, int and char are integers
        return 'All stats should be integers' #error message if the respective parameters are not integers
    
    #if (isinstance(strength, (str, float, bool))) or (isinstance(intelligence, (str, float, bool))), or (isinstance(charisma, (str, float, bool))):
    #   return 'All stats should be integers'

    if (strength < 1) or (intelligence < 1) or (charisma < 1): #check if str, int and char values are less than one
        return 'All stats should be no less than 1' #error message if the respectives parameters are less than one
    
    if (strength > 4) or (intelligence > 4) or (charisma > 4): #check if str, int and char values are greater than 4
        return 'All stats should be no more than 4' #error message if any of the respective parameters are greater than 4
    
    if (strength + intelligence + charisma) != 7: #check if the sum of the numeric parameters are different than 7
        return 'The character should start with 7 points' #error message if the sum of the numeric parameters are different than 7

    return f"""{name}\nSTR {'●' * strength}{'○' * (10 - (strength))}\nINT {'●' * intelligence}{'○' * (10 - (intelligence))}\nCHA {'●' * charisma}{'○' * (10 - charisma)}"""

print(create_character('rem', 2, 1))
