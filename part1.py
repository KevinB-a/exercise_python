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
        print("result is ",result)
    except ZeroDivisionError:
        print("you try to divide by zero !")

divide(12,2)
print(4+9+78)
print(12-7)
print(5e4)

#exercise3 : communicate with computer
name=input("please enter your name")
print("hello and welcome!",name)

#exercise4 : first name and last name
first_name="kevin"
last_name= "billet"
print("Bonjour {} {}".format(first_name,last_name))

#exercise5 : characters to number
myNumber="123"
int_myNumber=int(myNumber) # create a new variable and converting to integer
type(int_myNumber)

#exercise6 : upper and lower case
word=input("please enter a word")
print(word.upper()) #change lower letters in upper letters
print(word.lower()) #change upper letters in lower letters
