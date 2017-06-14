#!/usr/bin/python3
"""
Computes the total number of ways a value can be made with the given coins
It is assumed that there are infinite coins for each given denomination
Not properly tested for coin lists which exclude 1-cent coins
@coins is a list of coin denominations and @value is the $ value you're making change for
"""
def coin_change(coins, value):
    coins = sorted(coins)
    print("finding number of ways to make value: {}\nwith coin array: {}".format(value, coins))
#sort coins to ensure DP algorithm can build on previous calculations as expected

    result = [1]
#initialize list with 1 way to have 0 cents

    for i in range(value - 1):
        result.append(0)
#use append to increase the list to desired size and ensure that list indexing works properly

    for i in range(len(coins)):
        for j in range(1, value):
            if j >= coins[i]:
                result[j] += result[j - coins[i]]
#only add solutions if the coin is smaller than the value, e.g. we're at 7 and the coin is 5

        print("coin totals for max coin {}: {}".format(coins[i], result))
#print at each step to see solution array for given value. List[value] = number of solutions
    return ("Number of ways to make value {} with given coins is: {}".format
            (value, result[value - 1]))
#because list indexing requires us to count from 0
print(coin_change([1, 2, 3, 4, 5], 8))
