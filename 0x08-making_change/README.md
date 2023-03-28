# Making Change
## Challenge
Given a pile of coins of different values, determine the fewest number of coins needed to meet a given amount total.

Prototype: `def makeChange(coins, total)`
Return: fewest number of coins needed to meet total
If total is 0 or less, return 0
If total cannot be met by any number of coins you have, return -1
coins is a list of the values of the coins in your possession
The value of a coin will always be an integer greater than 0
You can assume you have an infinite number of each denomination of coin in the list
Your solution’s runtime will be evaluated in this task

## Requirements & Contraints
- Return fewest number of coins to meet total
- Iterate through the coins list to evaluate for each of the denomination

## Solution
- sort the coins from largest to the smallest
- from the first index of the coins list, which is the largest denomination to the smallest
  denomination evaluate how many coins you can get from the current change, 
  - if you can get change from the current denomination
        - decrement the current total amount
        - increment the count of change acquired
  - otherwise if you cannot get change from the current denomination move to the next index
- return -1 if the total is not exhausted, i.e equal to 0
- otherwise return collected change count

