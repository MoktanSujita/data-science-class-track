# #wap to find a number is prime or composite
# n=int(input("enter number"))
# if n<2:
#     print("prime or composite")
# else:
#    for i in range(2,n):
#            if n%i==0:
#             print("Composite]")
#             break
#            else:
#                print("Prime")

#wap to calculate an ares of triangle and rectangle
# shape=input("Enter shape(triangle/rec)")

# if shape=="triangle":
#     x=float(input("enter base: "))
#     y=float(input("enter height: "))
#     print("Area =", (x*y)/2)

# elif shape=="rec":
#     x=float(input("enter length: "))
#     y=float(input("enter breadth: "))
#     print("Area =", (x*y))

# else:
#     print("shape not fount")

# class MyClass:
#     year=2026
#     def my_name(self,my_name):
#         print("My name is",my name)

#     new_object=MyClass()
#     print(new_object.year)
#     print(type(new_object))
#     new_object=my_name("Nischal")

# class MyClass:
#    year=2026
#    def __init__(self,My_name):
     
#      self.name=My_name
#      print(self.name)
#    def introduce_me(self):
#      print("My name is (self.name)")
# new_object=MyClass("Nischal")
# new_object.introduce_me()

#class attribute vs instant attribute

# class HumanSpecies:
#   species='sapiens'
#   def my_name(self,my_name):
#     print("Human's name is(my_name)")
    
# kriti_obj=HumanSpecies()
# kriti_obj.my_name("kriti")

#constructure
# class HumanSpecies:
#   species='sapiens'
#   def __init__(self,my_name):
#     self.name=my_name
#   def print_name(self):
#     print(f"human's name is{self.name}")

# sujita=HumanSpecies("nischal")
# sujita.print_name()

# class HumanSpecies:
#   species='sapiens'
#   def __init__(self,my_name):
#     self.name=my_name
#   def return_name(self):
#     return(f"human's name is{self.name}")
#   def print_name(self):
#     print(self.return_name())

# sujita=HumanSpecies("nischal")
# sujita.print_name()

# class HumanSpecies:
#   species='sapiens'
#   def __init__(self,my_name):
#     self.name=my_name
#   def __str__(self):
#     return(f"human's name is {self.name}") 
  
# sujita = HumanSpecies("sujita") 
# print(sujita)

class Animal:
    def __init_(self):
        print("This animal eats food")

class Dog(Animal):
   def __init_(self):
       Animal.__init_(self)
       print("Dog barks")
             
dog=Dog()
