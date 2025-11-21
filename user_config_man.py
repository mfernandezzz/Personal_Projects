#Build a User Configuration Manager that allows users to manage their settings such as theme, language, and notifications. 
#Implement functions to add, update, delete, and view user settings.
#For testing the code, you should create a dictionary named test_settings to store some user configuration preferences.
#The messages returned should have the key and value in lowercase. The original dictionary should have the key capitalize and the value in lowercase.

test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
} #dictionary of settings
data = ('volume', 'low') #tuple with a key-value pair
clave = 'notifications'

#function for add a setting
def add_setting(settings, data): #two parameters, a dictionary and a tuple
    new_dict = {k.lower(): v.lower() for k, v in settings.items()} #new dictionary with the key-value pair in lowercase
    for d in data:
        if d.lower() in new_dict.keys(): #check if the key exists in the dictionary
            return f'Setting {d.lower()} already exists! Cannot add a new setting with this name.' #error message if the key exists
    settings[(data[0]).capitalize()] = (data[1]).lower() #if the key doesnt exists, must be aggregate to the dictionary
    return f'Setting {(data[0]).lower()} added with value {(data[1]).lower()} succesfully!.'
#print(add_setting(test_settings, data))
#print(test_settings)


#function for update a setting
def update_setting(settings, data): #two parameters, the dictionary and a tuple
    new_dict = {k.lower(): v.lower() for k, v in settings.items()} #new dictionary with the key value pair in lowercase
    for d in data:
        if d.lower() in new_dict.keys(): #if the key setting exists
            settings[(data[0]).capitalize()] = (data[1]).lower() #update its value and return a message
            return f'Setting {(data[0]).lower()} updated to {(data[1]).lower()} successfully!'
    return f'Setting {(data[0]).lower()} does not exist! Cannot update a non-existing setting.' #if the key setting doesnt exists, return an error message
#print(update_setting(test_settings, data))
#print(test_settings)


#function for delete a setting
def delete_setting(settings, key): #two parameters, the dictionary and a key
    for k in settings:
        if k.lower() == key.lower():
            del settings[k]
            return f'Setting {key.lower()} deleted succesfully!'
    return f'Setting {key.lower()} not found'
#print(delete_setting(test_settings, clave))
#print(test_settings)


#function for view a dictionary of settings
def view_settings(settings): #a dictionary of settings
    if len(settings.keys()) == 0: #if the given dictionary of settings is empty
        return 'No settings available.' #return a message error
    print('Current User Settings: ')
    return """\n""".join(f'{(k).capitalize()}: {(v).lower()}' for k, v in settings.items())
#print(view_settings(test_settings))
