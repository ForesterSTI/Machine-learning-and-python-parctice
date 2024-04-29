# Asks user for name of fruit and add to list

my_list = ["apple", "orange", "pineapple", "pear"]  
fruit = input("Please enter a fruit name")
my_list.extend(fruit.split() )  
print(my_list)

