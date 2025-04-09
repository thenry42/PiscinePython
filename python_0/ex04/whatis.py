import sys

def main():

    nums = []
    for argv in sys.argv[1:]:
        try:
            assert argv.isdigit(), "AssertionError: argument is not an integer"
            nums.append(int(argv))
        except AssertionError as e:
            print(e)
            return 1

    if len(nums) == 0:
        return 1
    try:
        assert len(nums) == 1, "AssertionError: more than one argument is provided"
    except AssertionError as e:
        print(e)
        return 1

    if nums[0] % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

    return 0

if __name__ == "__main__": 
    main()