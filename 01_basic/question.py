#Create a variable name to store your name and another variable age to store your age. Print them together in one sentence.

name = "shubha"
age = 14

print(name, age)


print("My name is", name)
print("my age is",age)

# Create one variable of each type: integer, float, string  and boolean.
# Print their values and check their data types using type().

number = 1
number2 = 1.1
animal = "cat"
candrive = False

print("this is a int",number)
print("this is a float",number2)
print("this is a string",animal)
print("this is a bool",candrive)

print(type(number))
print(type(number2))
print(type(animal))
print(type(candrive))


#Convert the string "123" into an integer, then add 10 to it. Print the result.

n1 = "123"
n2 = 10

n11 = int(n1)  

print(n11 + n2)

print(type(n1))
print(type(n11))

#If a = 15 and b = 4, calculate and print: Addition, Subtraction, Multiplication and Division.

a = 15
b = 4
add = a + b
sub = a - b
mult =a * b
division =a / b
print(add,sub,mult,division)




#Swap the values of two variables x = 10 and y = 20 without using a third variable.

x = 10 
y = 20

x = x + y   #30
y = x - y   #10
x = x - y   #20

print("x:", x)
print("y:", y)



# take the name and age as input from the user and print it:

name = input("enter users name: ")
age = int(input("enter users age: "))
print(name,age)