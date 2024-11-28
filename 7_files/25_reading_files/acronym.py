#Ask the user what acronym they want to look up?
#Open the file for reading
#Loop over each line of the file
    #Check if the current acronym matches the user's acronym
        #print the definition 

#open the file
#1 
#file = open('input.txt')
#try:
    #do file operations here
 #   pass
#finally:
 #   file.close()

#2 (shortcut)
# with open('input.txt') as file:

#read the file
#1
#   result = file.readline()
#   for line in result: file:
#        print(line)
#2 shortcut
#   for line in file:
#        print(file)


#Ask the user what acronym they want to look up?
look_up=input("What sofware acronym would you like to look up?\n")
#open the file
found = False
with open('acronym.txt') as file:
    #read the file
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break
if not found:
    print('The acronym does not exist')
     
