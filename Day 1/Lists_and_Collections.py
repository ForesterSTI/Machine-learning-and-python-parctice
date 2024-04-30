# Asks user for name of fruit and add to list then prints it

my_list = ["apple", "orange", "pineapple", "pear"]  
'''
fruit = input("Please enter a fruit name")
my_list.extend(fruit.split() )  
print(my_list)
'''   
Person = { 'name': 'John', 
          'surname':'Smith',
          'Age':18,
          'Address':{'Number':123,
                     'street': "Oak",
                     'Suburb':"Apprilia",
                     "City":"Swollow Ville"},

}

password = input("Please enter your password")
attempt = 1

    

def check_password(password):
     if password == "carly":
        print("Name:", Person['name'])
     else:
        print("incorrect password")
        attempt = attempt + 1 


    
        
while attempt <= 3: 
   check_password(password)   
else:
    if attempt >= 3:
        
        print("too many password attempts")  
      


        
'''
import pandas as pd
my_dict1 = {
    'California': 38332521,
    'Texas': 26448193,
    'New York': 19651127,
    'Florida': 19552860,
    'Illinois': 12882135
}
my_series = pd.Series(my_dict1)
print(my_series.values)

  
 '''