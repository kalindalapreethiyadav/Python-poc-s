# Python variable types

# 1. Integer (int)
# An integer is a whole number, positive or negative, without decimals.

x = 10          # Integer
y = -5          # Negative integer

# 2. Floating Point (float)
# A float is a number that has a decimal point.

a = 3.14        # Positive float
b = -0.001      # Negative float

# 3. String (str)
# A string is a sequence of characters enclosed in quotes (either single ' or double ").

name = "Alice"   # String
message = 'Hello, world!'  # Another string

# 4. Boolean (bool)
# A boolean can only be True or False.

is_active = True   # Boolean
is_logged_in = False  # Boolean

# 5. List (list)
# A list is a collection of ordered elements, which can be of mixed types.

fruits = ['apple', 'banana', 'cherry']  # List of strings
numbers = [1, 2, 3, 4, 5]  # List of integers
mixed = [1, 'apple', 3.14, True]  # List with mixed types

# 6. Tuple (tuple)
# A tuple is similar to a list but is immutable (cannot be changed after creation).

coordinates = (10, 20)  # Tuple of integers
person = ('John', 30, True)  # Tuple with mixed types

# 7. Set (set)
# A set is an unordered collection of unique elements.

unique_numbers = {1, 2, 3, 4}  # Set of integers
fruits_set = {'apple', 'banana', 'cherry'}  # Set of strings

# 8. Dictionary (dict)
# A dictionary is a collection of key-value pairs. Keys must be unique.

person = {'name': 'Alice', 'age': 30, 'is_student': False}  # Dictionary with string keys
user_info = {'username': 'john_doe', 'email': 'john@example.com'}  # Dictionary with string keys

# 9. None (NoneType)
# The None type is used to represent the absence of a value or a null value.

nothing = None  # NoneType

# set vs dict
# Set is unique, {}, 
# dict is unique, {"key": "value"}, 

# list vs tuple
#List:mutable (change, add, or remove elements after created)
# Tuple: immutable (created, you cannot change, add, or remove elements).

fruits = ['apple', 'banana', 'cherry']
fruits[0] = 'grape'  # Modifying an element
fruits.append('orange')  # Adding a new element
print(fruits)  # Output: ['grape', 'banana', 'cherry', 'orange']
