### FUNCTIONS ###

# VIDEO

#to create a function, do following
# def NAME_OF_FUNCTION(PARAMETERS):
    # these lines
    # belong to 
    # the code block 
    # for the function


#def say_hello(name, age):
#    print(f"Hello {name} you are {age} years old.")

#say_hello("Kevin", 23)

#def say_goodbye():
#    print("Goodbye")

#def greet_back(feeling):
#    if feeling == "good":
#        print("Awesome I feel good too")
#    elif feeling == "bad":
#        print("I am so sorry")
#    elif feeling == "stressed":
#        print("Coding can be hard to learn")
#    else:
#        print("Well, have a good day!")

# Driver Code
#while True:
#    response = input("What do you want to do? Say hello [H] Say goodbye [G] talke to me [T], quit [Q]")
#    if response.lower() == 'q':
#        say_goodbye()
#        break
#    elif response.lower() == 'h':
#        name1 = input("What is your name? ")
#        age1 = input("What is your age? ")
#        say_hello(name1, age1)
#    elif response.lower() == 'g':
#        say_goodbye()
#    elif response.lower() == 't':
#        feeling1 = input("How are you today?")
#        greet_back(feeling1)
#    else:
#        print("Invalid input")


#def my_function(num):
#    while num < 10:
#        print(num)
#        if num == 6:
#            return
#        num += 1

#my_function(4)


# BOOK

#def greet_user(name):
#    print("Hello, " + name.title() + "!")
#greet_user("Jack")

#def favorite_book(title):
#    print("My favorite book is " + title.title() + ".")
#favorite_book("The Hunger Games")

# Passing arguments

# positional arguments = parameters in the same order they were written in i.e
#def describe_pet(animal_type, pet_name):
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name + ".")
#describe_pet('hamster', 'Harry')
#animal_type and pet_name are positional arguments

# keyword arguments = name-value pair that you pass to a function
#def describe_pet(animal_type, pet_name):
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name + ".")
#describe_pet(animal_type='hamster', pet_name='Harry')
#describe_pet(pet_name="Bonzo", animal_type='chicken')
#In this case, order doesn't matter when inputing values in function parameters

# default parameters = if parameter is not defined when running function it will default 
#def describe_pet(pet_name, animal_type='dog'):
#    print("\nI have a " + animal_type + ".")
#    print("My " + animal_type + "'s name is " + pet_name + ".")
#describe_pet(pet_name='Harry')

# Return Values
# will take inputs, processes data and return what you make function spit out
#def get_formatted_name(first_name, last_name):
#    full_name = first_name + ' ' + last_name
#    return full_name.title()
#musician = get_formatted_name('jimmy', 'neutron')
#print(musician)

# Optional arguments
# sometimes not all information is necessary but will help
#def get_formatted_name(first_name, last_name, middle_name=''):
#    if middle_name:
#        full_name = first_name + ' '+ middle_name + ' ' + last_name
#    else:
#        full_name = first_name + ' ' + last_name
#    return full_name.title()
#musician = get_formatted_name('jimmy', 'neutron')
#print(musician)
#musician = get_formatted_name('jamie', 'curtis', 'lee')
#print(musician)

# Returning a dictionary
#def build_person(first_name, last_name, age = ''):
#    person = {'first': first_name, 'last': last_name}
#    if age:
#        person['age'] = age
#    return person
#musician = build_person('jimi','hendrix', age = 27)
#print(musician)

# Function with a while loop
#def get_formatted_name(first_name, last_name):
#    full_name = first_name + ' ' + last_name
#    return full_name.title()

#while True:
#    print("n\Please tell me your name:")
#    print("(enter 'q' any time to quit)")
#    f_name = input("First name: ")
#    if f_name == 'q':
#        break
#    l_name = input("Last name: ")
#    if l_name == 'q':
#        break
#    formatted_name = get_formatted_name(f_name, l_name)
#    print("\nHello, " + formatted_name + "!")


# Passing a list
#def greet_users(names):
#    for name in names:
#        msg = "Hello, " + name.title() + "!"
#        print(msg)
#usernames = ['hannah', 'ty', 'margot']
#greet_users(usernames)

# Modifying a list in a function
#When you pass a list to a function, the function can modify the list
#Changes made to the list in the function is permanent

#Example not using function
#unprinted_designs = ['iphone case', 'robot', 'cube']
#completed_models = []
#while unprinted_designs:
#    current_design = unprinted_designs.pop()
#    print("Printing: " + current_design)
#    completed_models.append(current_design)
#print("\nThe following designs have been completed:")
#for completed in completed_models:
#    print(completed.title())

#Example using function
#def print_models(unprinted_designs, completed_models):
#    while unprinted_designs:
#        current_design = unprinted_designs.pop()
#        completed_models.append(current_design)
#
#def show_completed_models(completed_models):
#    print("\nThe following designs have been completed: ")
#    for completed in completed_models:
#        print(completed)
#unprinted_designs = ['iphone case', 'robot', 'cube']
#completed_models = []
#print_models(unprinted_designs, completed_models)
#show_completed_models(completed_models)

# Preventing a function from modifying a list
# you can send a copy of the list to a function, which will not affect the original list
# use the slice notation [:] after the list
# function_name(list_name[:])
# for previous function, syntax would be --> print_models(unprinted_designs[:], completed_models)

# Passing an arbitrary number of arguments
# useful when you don't know how many parameters/arguments a function needs to accept
# the * notation tells python that it needs to make an empty tuple and pack whatever values it received into this tuple
#def make_pizza(*toppings):
#    print("\nMaking a pizza with the following toppings: ")
#    for topping in toppings:
#        print("- " + topping)
#make_pizza('pepperoni')
#make_pizza('mushrooms', 'pepperoni', 'sausage')

# Mixing positional and arbitrary arguments
# if you want a function to accept multiple types of arguments, you must put placea arbirtrary number of arguments last
# Example with size of pizza and toppings
#def make_pizza(size, *toppings):
#    print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
#    for topping in toppings:
#        print("- " + topping)
#make_pizza(12, 'mushroom', 'sausage', 'peppers')

# Using arbitrary keyword arguments
# When you don't know how many arguments or what kind of info will be passed to the function
#def build_profile(first, last, **user_info):
#    # Building dictionary containing all info we get about user
#    profile = {}
#    profile['first_name'] = first
#    profile['last_name'] = last
#    for key, value in user_info.items():
#        profile[key] = value
#    return profile
#user_profile = build_profile('albert', 'einstein', location= 'princeton', field='physics')
#print(user_profile)

# Storing your functions in modules
# Can save function in separate file and then import module into main program
# we will create a module called pizza.py and import it here
# to call it, just type --> import function_name
# then to use function type --> file_name.function_name()
#import pizza
#pizza.make_pizza(12, 'mushrooms', 'sausage')

# Using as to give a function an alias
# Syntax is --> from module_name import function_name as fn
#from pizza import make_pizza as mp
#mp(16, 'mushrooms')
# Can also work for module names
#import pizza as pz
#pz.make_pizza(16, 'mushrooms')
# To import all functions use *
# Syntax is --> from module_name import *

x=5
def some_function(x):
    print(x, end=" ")
print(x, end=" ")
some_function(1)
x = x-1
print(x, end=" ")
some_function(1)
