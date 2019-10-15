# exercise 1 : display "Hello World"
print("Hello World")
var="Hello World"
print(var)

# exercise 2 :  miscellaneous calculations
print(3*3)
# create a function who divide numbers
def divide(a,b):
    try:
        result=a/b
    except:
        print("you try to divide by zero !")
    else:
        print ("result is ",result)
divide(12,0)
print(4+9+78)
print(12-7)
print(5e4)

#exercise3 : communicate with computer
nom=input("veuillez entrez votre nom")
print("bonjour et bienvenue !",nom)

#exercise4 : first name and last name
first_name="kevin"
last_name= "billet"
print("Bonjour {} {}".format(first_name,last_name))

#exercise5 : characters to number
myNumber="123"
int_myNumber=int(myNumber) # create a new variable and converting to integer
type(int_myNumber)
