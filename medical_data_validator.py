import re
# dictionary with medical records
medical_records = [
    {
        'patient_id': 'P1001',
        'age': 34,
        'gender': 'Female',
        'diagnosis': 'Hypertension',
        'medications': ['Lisinopril'],
        'last_visit_id': 'V2301',
    },
    {
        'patient_id': 'p10s2',
        'age': 47,
        'gender': 'male',
        'diagnosis': 'Type 2 Diabetes',
        'medications': ['Metformin', 'Insulin'],
        'last_visit_id': 'v2302',
    },
    {
        'patient_id': 'P1003',
        'age': 29,
        'gender': 'female',
        'diagnosis': 'Asthma',
        'medications': ['Albuterol'],
        'last_visit_id': 'v230A',
    },
    {
        'patient_id': 'p1004',
        'age': 56,
        'gender': 'Male',
        'diagnosis': 'Chronic Back Pain',
        'medications': ['Ibuprofen', 'Physical Therapy'],
        'last_visit_id': 'V2304',
    }
]

# this function return a list with the names of keys with a invalid value
def find_invalid_records(patient_id, age, gender, diagnosis, medications, last_visit_id):
    constraints = {
        # with re library, check if the value of the key patient_id starts with letter p followed by a sequence of numbers
        'patient_id': isinstance(patient_id, str) and re.fullmatch('p\d+', patient_id, re.IGNORECASE),

        'age': isinstance(age, int) and age >= 18,

        # check if the value of the gender key is male or femal
        'gender': isinstance(gender, str) and gender.lower() in ('male', 'female'),

        # check if the value of the diagnosis key is a string or the value is None
        'diagnosis': isinstance(diagnosis, str) or diagnosis is None,

        # check if the value of the medications key is a list and if all the elements of the mentioned list are strings
        'medications': isinstance(medications, list) and all([isinstance(i, str) for i in medications]),

        # very similar to patient_id
        'last_visit_id': isinstance(last_visit_id, str) and re.fullmatch('v\d+', last_visit_id, re.IGNORECASE)
    }
    return [key for key, value in constraints.items() if not value]

def validate(data):
    # this variable will contain True if the data paremeter is a list, otherwise, will contain False
    is_sequence = isinstance(data, (list, tuple))

    # if the data parameter is not a list or tuple, print an error message
    if not is_sequence:
        print('Invalid format: expected a list or tuple.')
        return False
        
    is_invalid = False #initially, set the value of this variable to False

    # a set with the keys of each dictionary
    key_set = set(['patient_id', 'age', 'gender', 'diagnosis', 'medications', 'last_visit_id'])

    # iterate over the list (data parameter) and check if contains dictionaries
    # index variable represent the position of the element in the list and dictionary the element itself
    for index, dictionary in enumerate(data):
        # if the list contains an element that is not a dictionary, print a message error with the position of the invalid element
        if not isinstance(dictionary, dict):
            print(f'Invalid format: expected a dictionary at position {index}.')
            is_invalid = True #if an error occured, change the value of the is_invalid variable to True
            continue

        # if a dictionary contains a different number or different names of keys in comparation to the key_set variable, print an error message 
        # convert the list of keys in a set and perform a operation between sets
        if set(dictionary.keys()) != key_set:
            print(f'Invalid format: {dictionary} at position {index} has missing and/or invalid keys.')
            is_invalid = True #if an error occured, change the value of the is_invalid variable to True
            continue

        # call the function find_invalid_records with the dictionary variable from the initial for as a parameter, unpacking the respective keys
        invalid_records = find_invalid_records(**dictionary)

        # iterate over the list with the name of invalid keys and return a message error with the name of the key, his value and the position of the dictionary on the list
        for key in invalid_records:
            print(f'Unexpected format {key}: {dictionary[key]} at position {index}') 
            is_invalid = True #if an error occured, change the value of this variable to True

    if is_invalid:
        return False #return False if an error occured in a previous step
    print('Valid format.') # message in console if all the requeriments was fulfilled
    return True

validate(medical_records)
