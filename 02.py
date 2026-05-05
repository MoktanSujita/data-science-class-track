# rent = 500
# rent = "500"
# print(rent)

# #strings are immutable

# fullName = "Sujita Moktan"
# firstName = slice(0, 6)
# print(fullName[firstName])

# lastName = slice(7, 13)
# print(fullName[lastName])

# #spilting the string with space 
# print("Name:" , fullName.split(' '))
# print("First Name:" , fullName.split(' ')[0])
# print("Last Name:" , fullName.split(' ')[1])

# lunch = 3.
# print(type(lunch))

#parsing the input
# number = int(input("Enter a number: "))
# print(type(number))

#vaiables naming convention
#snake_case, camelCase, PascalCase,

#operators 
# a = 2
# b = 3 

# print(a ** b)#exponentiation (a to the power of b)
# print(a // b) #lower seall division (only the integer part of the remainder)
# a%=3 # a = a % 3
# print(a)

# #comparison operators return boolean values
# print(a != b) #<=, >=, ==, < , > 

# #logical operators
# my_age = 20

# print(my_age > 18 and my_age < 20)
# print(my_age > 18 or my_age < 200)

#check if the string contains a character
# my_name = "Sujita"
# print("i" in my_name) #returns boolean value

# my_first_list = [1,2]
# print(my_first_list)
# my_second_list = my_first_list
# print(my_second_list)
# my_third_list = [1,2]
# print(my_third_list is my_first_list)
# print(my_first_list is my_second_list)
# print(my_second_list is my_third_list)

#bitwise operators
# print(2 ^ 3)

# my_number = 21
# if my_number % 2 == 0:
#     print("Even")

# elif my_number == 0:
#     print("Zero")

# else:
#     print("Odd")

#list are mutable
# my_list = [1,2,3]
# my_list[0] = "10"
# print(my_list)

# for i in my_list:
#     print(i)
# my_list.append(4) #add an element to the end of the list
# print(my_list)

# my_list.pop(2) #remove the element at index 2
# print(my_list)

# print(10 in my_list) # in is a membership operator

# my_list = [1,2,3,4,5]
# my_squared_list = []

# for i in my_list:
#     my_squared_list.append(i**2)

# print(my_squared_list)

# squared_list_comprehension = [i**2 for i in my_list if i%2 ==0]
# print(squared_list_comprehension)

#Tuples
# point = (2,3)
# print(point)
# point[0] = 10 #tuples are immutable
# print(point)

#sets
a = {1,2,3,4,5}
print(a)
