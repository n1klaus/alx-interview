#!/usr/bin/python3
""" Prime Game """


def get_primes_until(max):
    """
    Args:
        max(int): the maximum value to collect all primes
    Returns:
        (list): a list of all the primes below max
    """
    # Confirm our arguments are valid
    if max is None or max <= 1:
        return []

    # Create our primes list
    result = [num for num in range(2, max + 1)]

    for index in range(len(result[:])):
        for divisor in range(2, max):
            if index < len(result) and result[index] != divisor and\
                    result[index] % divisor == 0:
                del result[index]
    return result


def remove_prime_multiples(prime, source):
    """
    Args:
        prime(int): prime numer
        source(list): list to remove the prime and its multiples
    Returns:
        (list)Modified list
    """
    # check our arguments are valid
    if prime is None or source is None:
        return False

    # Start the operation to remove the prime and its multiple
    return [
        num for num in source
        if num % prime != 0
    ]


def isWinner(x, nums):
    """
    Args:
        x(int): number of rounds for each player to choose a prime number
        nums(list): an array of number choice range for each game round
    Returns:
        (str): name of the player who won the game
    """
    # Check the arguments are valid
    if not isinstance(x, int) or not isinstance(nums, list) \
            or x <= 0 or len(nums) == 0:
        return None

    # Initialize our prime number choices list
    primes = []
    # Initialize our player identifier
    player = 0
    # Initialize a player's prime number choice for the round
    choice = 0
    # Initialize Ben's number of wins
    Ben = 0
    # Initialize Maria's number of wins
    Maria = 0

    # Start the game rounds
    for round in range(x):
        # Create a new working set
        choices = nums[:]
        num = choices[round]
        primes = get_primes_until(num)

        # Let the players make their choices
        while True:
            # if there is no prime number choice to choose from
            if len(primes) <= (player + 1):
                break
            # Let Maria make her choice
            choice = primes[player]
            # Remove the prime number choice and all its multiples
            new_choices = remove_prime_multiples(choice, choices)
            # if there are no more valid choice options
            if len(new_choices) == 0 or len(choices) == len(new_choices)\
                    or (len(new_choices) == 1 and new_choices[0] == 1):
                break

            # if there is no prime number choice to choose from
            if len(primes) <= (player + 1):
                break
            # Let Ben make his choice
            player += 1
            choice = primes[player]
            # Remove the prime number and all its multiples
            choices = remove_prime_multiples(choice, new_choices)
            # if there are no more valid choice options
            if len(choices) == 0 or len(choices) == len(new_choices)\
                    or (len(choices) == 1 and choices[0] == 1):
                break

            player += 1

        # declare the winner for the round
        if player != 0 and player % 2 == 0:
            Maria += 1
        else:
            Ben += 1

    # Return the winner
    return "Maria" if Maria > Ben else "Ben"
