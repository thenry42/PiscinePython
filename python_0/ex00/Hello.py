# A list is a collection of items in a particular order.
# Lists are mutable, meaning that the items in a list can be changed, added, or removed.
# Lists are defined by enclosing the items in square brackets [].
# Example: my_list = [1, 2, 3, 4]
ft_list = ["Hello", "tata!"]

# A tuple is a collection of items in a particular order.
# Tuples are immutable, meaning that the items in a tuple cannot be changed.
# Tuples are defined by enclosing the items in parentheses ().
# Example: my_tuple = (1, 2, 3, 4)
ft_tuple = ("Hello", "toto!")

# A set is a collection of items in a particular order.
# Sets are mutable, meaning that the items in a set can be changed, added, or removed.
# Sets are defined by enclosing the items in curly braces {}.
# Example: my_set = {"Hello", "tutu!"}
ft_set = {"Hello", "tutu!"}

# A dictionary is a collection of key-value pairs.
# Dictionaries are mutable, meaning that the items in a dictionary can be changed, added, or removed.
# Dictionaries are defined by enclosing the items in curly braces {}.
# Example: my_dict = {"Hello": "titi!"}
ft_dict = {"Hello": "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

print("--------------------")

# list can be modified using the index
ft_list[1] = "World!"

# tuple can't be modified using the index so we must convert it to a list and then back to a tuple
tmp = list(ft_tuple)
tmp[1] = "France!"
ft_tuple = tuple(tmp)

# set can be modified using the remove and add methods
ft_set.remove("tutu!")
ft_set.add("Paris!")

# dictionary can be modified using the key
ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)