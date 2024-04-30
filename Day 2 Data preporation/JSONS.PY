import json

data={
'name': 'John Doe',
    'age': 25,
    'occupation': 'Data Scientist',
    'address': {
        'street': '45A Long St',
        'city': 'Kempton Park',
        'state': 'Gauteng',
        'zip':1619
    },
    'interests': ['hiking', 'reading', 'coding']
}

data['interests'][0] = 'cars'

jason_data= json.dumps(data, indent=4)
print(jason_data)

