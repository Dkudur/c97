print("Hello World!!")

x , y = 10 , 20

print(x)

# name = input("Enter your name : ")
# print(name)
# print(type(name))

# by default input takes data in string



# age = int(input("Enter your age : "))
# print(age)

# ------------------------------------ if-else ----------------------------------------------

# if age > 18 : 
#     print("You can vote")

# elif age == 18 :
#     print("You need to wait")

# else:
#     print("KID!!")


# ------------------------------------ functions in python ----------------------------------------------

# f = 9/5 times c + 32

print("------------------------------------------")
def convert_temperature():
    c = 20
    f = 9/5*c + 32
    print("the temp in celcius is" ,c , "and the temp in farenheit is",f)

convert_temperature()

# ----------------------------------------------------

print("------------------------------------------")
def largest(a , b):
    if a > b:
        print("The largest number is ",a)
    elif b > a:
        print("The largest number is ",b)


largest(100,200)

# ----------------------------------------------------

print("------------------------------------------")
def larger(a, b, c):
    if a > b and a > c:
        print("The largest number is ",a)
    elif b > a and b > c:
        print("The largest number is ",b)
    elif c > a and c > b:
        print("The largest number is ",c)


larger(100,200,300)

# ----------------------------------------------------

print("------------------------------------------")

def operation(num, num2):
    choice = int(input("Enter 1 for Addition or Enter 2 for Multiplication : "))
    if choice == 1:
        answer = num + num2
        print("The addition of those numbers is",answer)
    if choice == 2:
        answer = num * num2
        print("The multiplication of those numbers is",answer)



n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))

operation(n1, n2)

