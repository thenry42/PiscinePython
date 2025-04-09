# The __class__ attribute is used to get the class of an object.
# This solution does not use any function as it is a python built-in attribute.
def all_thing_is_obj(object: any) -> int:
    if object.__class__ is list:
        print("List : ", object.__class__)
    elif object.__class__ is tuple:
        print("Tuple : ", object.__class__)
    elif object.__class__ is set:
        print("Set : ", object.__class__)
    elif object.__class__ is dict:
        print("Dict : ", object.__class__)
    elif object.__class__ is str:
        print("%s is in the kitchen : " % object, object.__class__)
    else:
        print("Type not found")
    return 42


# The isinstance() function is used to check if an object is an instance of a class.
# Apperently it is the best way to check the type of an object.
def all_thing_is_obj_isInstance(object: any) -> int:
    if isinstance(object, list):
        print("List : ", object.__class__)
    elif isinstance(object, tuple):
        print("Tuple : ", object.__class__)
    elif isinstance(object, set):
        print("Set : ", object.__class__)
    elif isinstance(object, dict):
        print("Dict : ", object.__class__)
    elif isinstance(object, str):
        print("%s is in the kitchen : " % object, object.__class__)
    else:
        print("Type not found")
    return 42

# The type() function is used to get the type of an object
# and compare it to the type of the object.
# Not good with inheritance.
def all_thing_is_obj_type(object: any) -> int:
    if type(object) == list:
        print("List : ", object.__class__)
    elif type(object) == tuple:
        print("Tuple : ", object.__class__)
    elif type(object) == set:
        print("Set : ", object.__class__)
    elif type(object) == dict:
        print("Dict : ", object.__class__)
    elif type(object) == str:
        print("%s is in the kitchen : " % object, object.__class__)
    else:
        print("Type not found")
    return 42