#key -valuse pairs
acronyms = {
    'LOL' : 'laugh out loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
     }

print(acronyms['LOL']) #instead of index we use the key to look up value

#dictionary can hold anything
#string to string
acronyms1 = {
    'LOL' : 'laugh out loud',
    'IDK' : "I don't know",
    'TBH' : 'to be honest'
     }

print(acronyms)

#update the value:
acronyms1['TBH'] = 'honestly'

#delete a value
del acronyms1['LOL']
print(acronyms1)

#if you want to acces a key which it is not there, you will get  key error!!!!! 
definiton = acronyms['BTW'] #this will result in: KeyError: 'BTW'
#to avoid this use get method
definition = acronyms.get('BTW') 
print(acronyms)#you will get: NONE

print(acronyms1)
#stings to number
menu ={'soup' : 5, 'salad':10}

#anything
my_dict={10: 'hello', 3: 45}
