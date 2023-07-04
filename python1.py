message = """Hello World
Living life humbly is very important"""
print(message)

# methods are functions that belong to an object
print(message.find('o'))

greeting = 'hello'
name = 'michael'
message = greeting + ', ' + name + '.'
print(message)

# string formatting
message = '{}, {}.'.format(greeting,name)
print(message)

# using f-strings
message = f'{greeting}, {name.upper()}.'
print(message)

# using dir to check all the methods and attributes available and help for further details
print(dir(greeting))
# print(help(str))
# print(help(str.lower))

# playing with numbers
# basic arithmetic operations are same as in C++
print(3/2)  # division
print(3//2) # gif of result
print(3**2) # power
print(3%2)  # mod

num=1
num*=10
print(num)

# arguments like abs, round etc same as C++
# comparisons like >, < etc return boolean values

# casting
num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)
print(num_1 + num_2)

# lists
courses = ['History','Math','Physics']
print(courses)
print(len(courses))
print(courses[1])
print(courses[-1]) # -1 can always be used to get the last item
print(courses[:2])
print(courses[2:])
# append method to add items in a list
courses.append('Art')
print(courses)
# insert method to add items at a specific position in a list
courses.insert(2,'Art')
print(courses)
courses_2 = ['GSC','Hindi']
courses.insert(0,courses_2)
print(courses)
print(courses[0])
# to avoid this problem we use extend method
courses.extend(courses_2)
print(courses)
# use pop method to remove last element of a list
# pop method is specially useful if our list is a stack or a queue
popped = courses.pop()
print(popped)
print(courses)
# reversing
courses.reverse()
print(courses)
popped = courses.pop()
print(popped)
# sorting in alphabetical and ascending order
courses.sort()
print(courses)
nums = [1,2,5,9]
nums.sort()
print(nums)
# sorting in reverse and descending order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)

# sorting a list without altering the original list
courses_sort = sorted(courses) # use the sorted function
print(courses_sort)
print(courses)
# to find min,max,sum etc.
print(min(nums))
print(sum(nums))
# to find index of an element
print(courses.index('Math'))
# to check if an element exists in a list
print('GK' in courses)
print('History' in courses)

for index,course in enumerate(courses , start = 1):
    print(index,course)

course_str = ', '.join(courses) # Instead of comma we can use any symbol with which we want to print
print(course_str)
new_list = course_str.split(', ')
print(new_list)

# tuples are same as lists but they are immutable and created as ('')
# sets print values in unordered ways
cs_courses = {'his','math','Chemistry','Computer'}
print(cs_courses)
# sets are used to remove duplicate values\s
cs_courses = {'his','math','math','chem'}
print(cs_courses)
# sets are used to determine what values they share or don't share with another set
cs_courses = {'a','b','c','d'}
art_courses = {'e','f','a','b'}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))

# initialisations
emp_list = []
emp_tuple = ()
emp_set = set() # emp_set = {} is a dictionary not a set

# key-value pairs (dictionaries)
student = {'name':'John', 'age':23,'courses': ['Math','Computer']}
print(student)
print(student['age'])
print(student.get('name')) # in get method we can also add a msg to  be displayed if key is not found
# update method
student.update({'name':'Jane','age':32,'phone':'555-55555'})
print(student)
# delete a key-value pair
# del student['phone']
# print(student)
phone = student.pop('phone')
print(phone)
print(student)
# some other methods
print(len(student))
print(student.keys())
print(student.values())
print(student.items())
# looping through the dictionary
for key in student:
    print(key)

for key, value in student.items():
    print(key,value)
# Conditionals
# if, elif, else
# python has no switch case statement

# loops


user ='Admin'
logged_in = 'True'

if user == 'Admin' and logged_in == 'True': # or,not are another operators
    print('Admin Page')
else:
    print('Bad Credentials')
# checking if two objects have the same identity in memory
a = [1,2,3]
b = [1,2,3]
print(a == b)
print(a is b)
print(id(a))
print(id(b))

# Functions - ❤️

def hello_func():
    return 'Hello Function.'
print(hello_func())

def hello_func(greeting):
    return '{} Function.'.format(greeting)
print(hello_func('Hi'))

def hello_func(greeting, name = 'You'):
    return '{} , {}.'.format(greeting, name)
print(hello_func('Hi'))

def student_info(*args, **kwargs): # positional arguments and keyword arguments
    print(args)
    print(kwargs)

student_info('Math','Computer', name = 'Jonathan',age =22)

courses = ['Math', 'Computer']
info = {'name': 'Jonathan', 'age': 22}

student_info(courses, info)
student_info(*courses, **info)

import sys
print(sys.path)
import os
print(os.getcwd())
import antigravity




























