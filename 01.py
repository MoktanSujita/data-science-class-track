#Print hello world
# print("Hello world!")
# print("Swastik College")

#formatting Output
#print("Hello World", end=" ") #end is used to print the next statement in the same line
#myName = "Sujita"
#print("\nMy first name is", myName)
firstName = "Sujita"
lastName = "Moktan"
#print("\nMy first name is {} and last name is {}".format(firstName, lastName))
print(f"My first name is {firstName} and last name is {lastName}")
print(f"{lastName[0]}")
print(f"{firstName[5]}")

firstName = "Samrachana"
n = len(firstName)
print("Name:", firstName[3:n])
print("Nickname:", firstName[:3])
print("Name:",firstName.split("a"))
print('Jenish said "He is very happy staying at Swastik\'s College"')
print('''
    Jenish said "He is very happy staying at Swastik's College"
    ''')
