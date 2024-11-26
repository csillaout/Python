
for i  in range(7):
    print(i)

for i in range(2,18, 2):
    print(i)

total = 0
expenses=[]
num_expenses = int(input('Enter # of expenses:'))
for i in range(num_expenses):
    expenses.append(float(input('Enter an expense:')))

total= sum(expenses)

print('You spent $', total, sep='')