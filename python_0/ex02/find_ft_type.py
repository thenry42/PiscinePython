def all_thing_is_obj(object: any) -> int:
    if object.__class__ is list:
        print("List : ", end="")
    elif object.__class__ is tuple:
        print("Tuple : ", end="")
    elif object.__class__ is set:
        print("Set : ", end="")
    else:
        print("Type not found")
    return 42

def all_thing_is_obj_isInstance(object: any) -> int:
    if isinstance(object, list):
        print("List : ", end="")
    elif isinstance(object, tuple):
        print("Tuple : ", end="")
    elif isinstance(object, set):
        print("Set : ", end="")
    else:
        print("Type not found")
    return 42

def all_thing_is_obj_type(object: any) -> int:
    if type(object) == list:
        print("List : ", end="")
    elif type(object) == tuple:
        print("Tuple : ", end="")
    elif type(object) == set:
        print("Set : ", end="")
    else:
        print("Type not found")
    return 42