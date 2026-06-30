print("AOA")

# type 
# name = "ajjo"
# print(type(name))

# v = 32j  # complex data type
# Data Types #
# List 
# tupple
# dictionary
# sets

# unicode
# unicode =   "😂"
# print(ord(unicode))

# Slicing 
# myName = "Mustafa Khan"
# print(myName[0:7:1])
# print(myName[8:12:1])

# Type conversion
# a = 22
# a = str(22)

# # formated string
# print("hello my name is ",myName)
# print(f"My name is {myName}")

# Input 
# age = input("Write your age here ")
# print(age)

# type conversion input
# agee = int(input("what is your age"))
# print(agee)

# Arithmetic Operators
# a = 7
# b = 3

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# flow divisio. Flow division converts the float values into integer it is symbolized by (//)
# print(a//b)
# exponensial operator (**)
# print(5**2)
# print(32 % 5) # modulus operation its means it will provide the remainder

# Aassignment operators
# Compound assignment operators
# (a = a + 3) == (a += 3) 
# +=, *=, -=, /=, //=, **=

# Comparasion operators
# <, >, ==, !=, <=, >=
# print(a != 7)
# print(ord("Mustafa"[0]))
# print(ord("Khan"[0]))
# print("Mustafa" < "Khan")

# Logical Operators
# and, or, not
# not reverse the boolean values 
# print(12 == 12)
# print(not 12 == 12)

# Conditions 
# if a < b:
#     print("True")
# else:
#     print("False")

# money = int(input("How much you have $"))
# ganey = int(input("How much you have $"))

# if money > ganey:
#     print(f"{money} is greater")

# elif ganey > money:
#     print(f"{ganey} is greater")
# else:
#     print("Both are eqaul")

# if money == 10:
#     print("You can get the choco bar")
# elif money == 20:
#     print("You can get the Monkey bar")
# else:
#     print("You can get the Corneto")

# name = str(input("What is your name "))
# age = int(input("what is your age"))

# if age >= 18:
#     print(f"{name} you can vote")
# else: 
#     print(f"{name} you are not old enough to vote")

# Loops #
# a = range(1,21,1)
# for i in a:
#     print(i)

# for i in range(21):
#     print(i)

# for i in range (16,0,-1):
#     print(i)

# for i in range(5,51,5):
#     print(i)

# n = int(input("what number of table you want to print "))

# for i in range(n,n*10+1,n):
#     print(i)

# nami = str(input("Write your name "))
# # Length function is len()
# for i in range(len(nami)):
#     print(nami[i])

# inte = int(input("Write an integer "))
# for i in range(inte):   
#     print("Hello world ")

# n = int(input("natural numbers "))
# for i in range(1,n+1,1):
#     print(i)

# n = int(input("natural numbers "))
# for i in range(n,0,-1):
#      print(i)

# sum = 0
# for i in range(1, n+1):
#     sum = sum + i
# print(sum)

# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"The factorial is {fact}")

# even = 0
# odd = 0

# for i in  range(1, n+1):
#     if i%2 == 0:
#         even = even + i 
#     else:
#        odd = odd + i

# print(f"your even sum is {even} and odd sum is {odd}") 


# count = 0
# for i in range(1, n+1):
#     if n % i == 0:
#         count = count + 1
# print(count)

# if count == 2:
#     print("your number is prime")
# else:
#     print("Poka 😂😂")

# reverse 
# c = "anas"
# d = ""
# for i in range(len(c)-1, -1, -1):
#     d = d + (c[i])
# print(d)

# dum = 1
# while dum <= 30:
#         print(dum)
#         dum = dum + 1

# ex = 256
# while ex > 0:
#     print(ex % 10)
#     ex = ex // 10

# import random
# num = random.randint(1, 10)
# tries = 0
# while True:
#     you = int(input("Type your random number "))
#     if num == you:
#         tries += 1
#         print(f"you Won 🎉! your nubmer {you} matched correctly with {num}")
#         break
#     elif you < num:
#         tries += 1
#         print(f"Oops 🧐! your nubmer {you} is bit smaller to {num}")
#     elif you > num:
#         tries += 1
#         print(f"So Close 😮! your nubmer {you} is little higher to {num}")
#     else:
#         tries += 1
#         print(f"try again 😔! your nubmer {you} did not matched correctly with {num}")

  ##############
# Data Structure #
  ##############
# lists
# tuples
# dictionary
# sets

# Lists 
l= [2, 3, 4, -5, -6, -7]

# print("Negative elements are ")
# for i in l:
#     if i < 0 :
#         print(i)
# print("Positive elements are ")
# for i in l:
#     if i > 0 :
#         print(i)

# sum = 0 
# for i in l:
#     sum = sum + i 
# print(sum)

# larg = l[0]
# for i in range(len(l)):
#     if  l[i] > larg:
#         larg = l[i]
#         # Index = i   
#         print(f"largest number is {l[i]}")

# Tuples
# t = (2,3,3,4)
# tup = (2,)
# print(tup)

# sets
# set = {1,2,3,4,5}
# # set.pop()
# # print(set)
# set.clear()
# print(set)

s = {1,2,3,4}
d = {4,5,6,7}
u = s.union(d)   # also known as u = s|d
print(u) 
u = s&d # also known as u = s.intersection(d)
print(u)
u = s-d #also known as u =  s.difference(d)
print(u)
u = s^d #also known as symetic difference
print(u)
