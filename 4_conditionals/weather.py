from operator import truediv


temperature = 75
if  temperature > 70 :
    print("It's too hot!")
    print("Stay inside!")
print("Have a good day!") #indentation is really important! Whitespace indents in python need to be consistent, otherwise there will be an indentationError

temp = 80
if temp > 90:
    print("It's too hot!")
    print("Stay inside!")
else:
    print("Enjoy the outdoors")


temp1 = 50
if temp1 > 80:
    print("Its too hot!")
elif temp1 < 60:
    print("its too cold!")
else: 
    print("Enjoy the outdoors!")

#combine comparisons
temp2 = 50
if temp2 > 80 or temp2<60:
    print("Stay inside!")
else:
    print("Enjoy the outdoors! ")

#logical operators and stores forecast as a string
temp3 = 75
forecast = "rainy"

if temp3 < 80 and forecast != "rainy":
    print("Go outside!")
else:
    print("Stay inside!")

#other way to write a statement
forecast1 ="rainy"
if not forecast1 == "rainy":
    print("Go outside!")
else:
    print("Stay inside")

raining = True
if raining:
    print("Stay inside it's raining!")

raining2 = True
if not raining:
    print("Go outside it is not raining")
else:
    print("Stay inside it is raining mate!")