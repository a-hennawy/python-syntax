def count_up(start, stop):
    """Print all numbers from start up to and including stop.

    For example:

        count_up(5, 7)

   should print:

        5
        6
        7
    """
    if start > stop:
        print("Make sure the starting number is smaller than the stopping number.")
    while start < stop:
        print(start)
        start += 1
    print(stop)


count_up(1, 7)
