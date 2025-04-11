import sys
from ft_filter import ft_filter


def filterstring(string, number):
    """
    Accepts exactly two arguments:
    - string: a string of words
    - number: an integer
    Returns a list of words from the string that are longer than the number.
    """
    return ft_filter(lambda x: len(x) > number, string.split())


def main():
    try:
        if len(sys.argv) != 3 or not sys.argv[2].isdigit():
            raise AssertionError("the arguments are bad")
        print(filterstring(sys.argv[1], int(sys.argv[2])))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1


if __name__ == "__main__":
    main()
