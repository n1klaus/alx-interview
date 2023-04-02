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
    if not isinstance(coins, list) or total <= 0:
        return 0

    if len(coins) == 0:
        return -1

    # sort the denomination from the largest to the smallest in place
    coins.sort(reverse=True)

    # Create our change count variable
    count = 0

    # print("{0} => {1}".format(coins, total))
    # Iterate the list of denominations to find total change count
    for den in coins:
        if den <= total:
            change_count = (total // den)
            # print("{0} - {1} = {2} \t\t: +{3}"
            #       .format(total,
            #               den * change_count,
            #               total - (den * change_count),
            #               change_count)
            #       )
            total -= (den * change_count)
            count += change_count

    # if could not get change for the total amount return Failed
    if total != 0:
        return -1
    # otherwise return the change count
    return count
