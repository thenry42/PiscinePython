def ft_filter(function, iterable):
    """
    Return an iterator yielding those items of iterable for which
    function(item) is true. If function is None, return the items
    that are true. (my 42 version)
    """
    # for each item in an iterable object, check if the item is true and if so,
    # add it to the new iterable object
    # return() => generator expression
    # return [] => list comprehension
    return [item for item in iterable if function(item)]


def main():
    print(filter.__doc__)
    print(ft_filter.__doc__)

    # test with a string and a function that checks if the char is uppercase
    str = "helLo woRld"
    print(list(filter(lambda x: x.isupper(), str)))
    print(list(ft_filter(lambda x: x.isupper(), str)))

    # test with a list of nb and a function that checks if the nb is even
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(filter(lambda x: x % 2 == 0, numbers)))
    print(list(ft_filter(lambda x: x % 2 == 0, numbers)))


if __name__ == "__main__":
    main()
