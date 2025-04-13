import sys


NESTED_MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/',
}


def sos(string):
    """
    Accepts a string as an argument.
    Returns the same string encoded in morse code.
    """

    res = ""
    for char in string:
        if char.upper() not in NESTED_MORSE:
            raise AssertionError("the arguments are bad")
        else:
            res += NESTED_MORSE[char.upper()] + " "
    return res[:-1]  # remove the last space


def main():
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")
        for char in sys.argv[1]:
            if char.upper() not in NESTED_MORSE:
                raise AssertionError("the arguments are bad")
        print(sos(sys.argv[1]))
    except AssertionError as e:
        print(f"AssertionError: {e}")
        return 1
    return 0


if __name__ == "__main__":
    main()
