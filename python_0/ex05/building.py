import sys


def main():
    """
    This function takes a string as an argument and returns
    the number of characters in the string for each category
    of characters. (upper, lower, punctuation, digits, spaces)
    """

    try:
        assert len(sys.argv) == 2, "AssertionError"
    except AssertionError as e:
        print(e)
        return 1

    string = sys.argv[1]
    upper = 0
    lower = 0
    punctuation = 0
    digits = 0
    spaces = 0

    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            punctuation += 1

    print("The text contains", len(string), "characters:")
    print(upper, "upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")
    return 0


if __name__ == "__main__":
    # print(main.__doc__)
    main()
