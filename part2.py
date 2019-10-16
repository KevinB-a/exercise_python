# exercise1 true or false
variable=""
variable1="OK"
print(bool(variable)) #use function bool for display True or False here display False
print(bool(variable1)) #use function bool for display True or False here display True

#exercice2 calculate my age
actual_year=int(input("please enter current year"))
born_year=int(input("please enter year of birth"))
age=actual_year-born_year
print("Your age is" ,age)
age1=int(input("enter age of your neighboor"))
print(age +age1)

#exercise3 :Shoes issues
shoes=70
jean=59
t_shirt=20
total=shoes+jean+t_shirt
reduc=80/100
print(total*reduc)

#exercise4 : mini calculator
number1=float(input("please enter a number"))
number2=float(input("please enter a sencond number"))
print(number1+number2)

#exercise5 : work with property
name=input("please enter your name")
last_name=input("please enter your last name")
letter=name[0]
letter1=name[-1]
letter2=last_name[0]
letter3=last_name[-1]
print("{}{}{}{}".format(letter,letter1,letter2,letter3).upper())
