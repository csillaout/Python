#checking for errors that we expect it makes our code easier to understand, read and troubleshoot

def reaminder_division(a,b):
    if b ==0:
       #instead of  this: raise ZeroDivisionError #raising an exception as it is not possible to divide a number by 0 
       raise Exception('Divisor cannot be 0')
    result = a//b
    remainder = a%b
    print(a, '/', b, 'is', result, 'remainder', remainder)
    
#main program
reaminder_division(10,0)