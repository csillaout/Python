#ask the user what acronym they want to add
acronym = input('What acronym do you watn to add?\n')
#ask the user for the definition 
definition=input('What is the definition?\n')
#open the file
with open('acronym.txt', 'a') as file:
#write the new acronym and definition to the file
    file.write(acronym + '-' + definition + '\n')
