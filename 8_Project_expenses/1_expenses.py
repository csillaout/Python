expenses=[10.50, 8, 5, 15, 20, 5, 3]
sum = 0
for expense in expenses:
    sum = sum + expense

#print('You spent: ' + str(sum))
print('You spent: $', sum,  sep = '') #if you use comma you dont need to convert sum into str

