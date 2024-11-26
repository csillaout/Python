acronyms = {'LOL': 'laugh out loud', 'IDK': 'i dont know'}
definition = acronyms.get('BTW') #result: NONE
print(definition)

if definition:
    print(definition)
else:
    print("Key doesnt exist")