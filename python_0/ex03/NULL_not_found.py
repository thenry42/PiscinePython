def NULL_not_found(object: any) -> int:
    if object is None:
        print("Nothing : None", object.__class__)
    elif object == float("NaN"):
        print("Garlic : float('NaN')", object.__class__)
    elif object == 0:
        print("Zero : 0", object.__class__)
    elif object == '':
        print("Empty :", object.__class__)
    elif object == False:
        print("Fake : False", object.__class__)
    else:
        print("Type not found")
        return 1
    return 0