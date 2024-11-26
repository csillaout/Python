#2 dimensional list how to get an item? 

menus =[
['Egg Sandwich', 'Bagel', 'Coffee'],
['BLT', 'PB&J', 'Turkey Sandwich'],
['Soup', 'Salad', 'Spaghetti', 'Taco']
]

print(menus[0]) #this will print the first list
print(menus[0][1]) #this will print the first list second item 

#what if you have a dictionary of lists?
menus ={
'Breakfast':['Egg Sandwich', 'Bagel', 'Coffee'],
'Lunch':['BLT', 'PB&J', 'Turkey Sandwich'],
'Dinner':['Soup', 'Salad', 'Spaghetti', 'Taco']
}

print(menus['Breakfast']) #prints the breakfast menu 
print(menus['Lunch'])
print(menus['Dinner'])

for name, menu in menus.items():
    print(name, ':' , menu ) #for loop for dictionary