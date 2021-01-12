#defined function name and set two arguements
def madlib(name, subject):
   #return string with arguements
        return "My name is", name, "My favorite subject is", subject
        
#setting the loop
while True:
    #giving values to my name arguement from user input
    name = input("Pick a name: ")
    #giving values to my subject arguement from user input
    subject = input("Pick a subject: ")
    #setting variable i'll use for printing in a sec and calling the function
    message = madlib(name, subject)
    #print message
    print(message)

    
        

