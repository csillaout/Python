
#Ask the user what acronym they want to look up?
def find_acronym():
    look_up=input("What sofware acronym would you like to look up?\n")
    #open the file
    found = False
    with open('acronym.txt') as file:
        #read the file
        for line in file:
            if look_up in line:
                print:(line)
                found = True
                break
    if not found:
        print('The acronym does not exist')
        
def add_acronym():
    #ask the user what acronym they want to add
    acronym = input('What acronym do you watn to add?\n')
    #ask the user for the definition 
    definition=input('What is the definition?\n')
    #open the file
    with open('acronym.txt', 'a') as file:
    #write the new acronym and definition to the file
        file.write(acronym + '-' + definition + '\n')

def main():
    
)