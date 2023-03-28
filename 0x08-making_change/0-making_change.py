#!/usr/bin/python3
"""Making Change"""


def makeChange(coins: list, total: int) -> int:
    """
    Args:
        coins (list): a list of coin denominations
        total (int): the total amount to get change for
    Returns:
        (int): fewest number of coins needed to meet a given amount total
    """
    # Check if the coins list is None or empty or
    # the total change amount is equal to or less than 0
    if not coins or total <= 0:
        return 0

    # check if our coins variable is iterable
    # i.e instance of (list, tuple, set, sequence, iterable)
    try:
        coins = list(iter(coins))
    except BaseException:
        return -1

    # sort the denomination from the largest to the smallest
    coins = sorted(coins, reverse=True)

    # Create our change count variable
    count: int = 0

    # print("{0} => {1}".format(coins, total))
    # Iterate the list of denominations to find total change count
    while True:
        get_change: bool = False
        for den in coins:
            if den <= total:
                get_change = True
                change_count: int = (total // den)
                # print("{0} - {1} = {2} \t\t: +{3}"
                #       .format(total,
                #               den * change_count,
                #               total - (den * change_count),
                #               change_count)
                #       )
                total -= (den * change_count)
                count += change_count
        if not get_change:
            break
    # if could not get change for the total amount return Failed
    if total != 0:
        return -1
    # otherwise return the change count
    return count
