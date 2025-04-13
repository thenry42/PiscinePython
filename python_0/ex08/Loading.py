def ft_tqdm(lst: range) -> range:
    """
    Accepts a range as an argument.
    Returns a range object with a progress bar.
    """

    len_lst = len(lst)
    bar_size = 50
    for elem in lst:
        percent = ((elem + 1) / len_lst) * 100
        percent_string = f"{percent:3.0f}%"

        filled_bars = int(percent / 100 * bar_size)
        empty_bars = bar_size - filled_bars
        bar = f"{'█' * filled_bars}{' ' * empty_bars}"

        # I can't print the last part of the bar because
        # it requires to import 'time'. I also can't get the width
        # of the shell without using external functions
        print(f"{percent_string}|{bar}| {elem + 1}/{len_lst}", end="\r")
        yield elem
