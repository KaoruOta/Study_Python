# Import the module collections and be able to access namedtuple
# wihtout having to write collections.namedtuple each time.
from collections import namedtuple
# Create a tuple of class 'Person'
Person = namedtuple("Person", ["name", "age", "gender"])

# Build a list of people by using Person
people = [
    Person("Andy", 30, "m"),
    Person("Ping", 1, "m"), 
    Person("Tina", 32, "f"),
    Person("Abby", 14, "f"),
    Person("Adah", 13, "f"),
    Person("Sebastian", 42, "m"),
    Person("Carol" , 68, "f"),
]

# first, let's show how this namedtuple works.
# Get the first entry in the list (which is Andy from above)
andy = people[0]

# From here, you can access andy like it was a class with attributes
# name, age, and gender (as seeon from the namedtuple)
print("name:  ", andy.name)
print("age:   ", andy.age)
print("gender:", andy.gender)

# now let's show what we can do with a list comprehension
male_names = [person.name for person in people if person.gender=="m"]
print("Male names:", male_names)

# Create a list of names where there age 
teen_names = [p.name for p in people if 13 <= p.age <= 18 ]
print("Teen names:", teen_names)
