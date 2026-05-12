#dictionary
subject_dict ={
    "dot_net" : "Sunil",
    "Python" : "Anish",
}
# print(subject_dict)
# print(subject_dict["dot_net"])
# for key in subject_dict:
#     print(key)
#     print(subject_dict[key])

# print(subject_dict.keys())
# print(subject_dict.values())
# print(subject_dict.items())

# for value in subject_dict.values():
#     print(value)

# for item in subject_dict.items():
#     print(item)

#loops
# i = 0 
# while i < 5:
#     print(i)
#     i += 1

# #print(help(range)) #range is a built in function that returns a sequence of numbers (to read documentation)
# print(list(range(0,5))) #from i to j-1

# for i in range(0,5,3): #from i to j-1 with step size 3
#     print(i)


# i = 1;
# list = []
# squared_list = []
# while i <= 20:
#     list.append(i)
#     squared_list.append(i**2)
#     i +=1
# print(list)
# print(squared_list)

# squared_list = [i**2 for i in range(1,21)]
# print(squared_list)

# squared_list = []
# for i in range(1,21):
#     squared_list.append(i**2)
# print(squared_list)


#functions
# def function():
#     print("Hello World from function")

# function()

# def greet(name = "Guest"):
#     print(f"Hello! ,{name}")
# greet()
# greet("Sujita")

# def function_with_return():
#     return "Hello World from function with return"
# print(function_with_return())

# def sum(a,b):
#     return a + b
# print(sum(2,3))

# def sub(a , b):
#     return a - b
# print(sub(5,3))

# #Args kwargs
# def my_function(*args): #when the no of arguments isnt known
#     print(f"Hello", args)
#     print(f"Hello {args[4]}")

# my_function("Sujita", "Anish", "Sunil", "Jashika", "Jenish", "Sujal")

# def my_fuction_with_kwargs(name, **kwargs):
#     print(f"Hello {name}")
#     print(f"kwargs: {kwargs}")
#     print(f"Teacher: {kwargs['Teacher']}")

# print(my_fuction_with_kwargs("Sujita", Teacher = "Jahika"))

# def my_function(name, **kwargs):
#     print("Args:", args)
#     print("kwargs:", kwargs)

def square(n):
    return n**2
print(square(2))

square_lambda = lambda initial_value : initial_value**2 #instead of traditional function and defining a function in one line we can use lambda function 
print(square_lambda(2))
