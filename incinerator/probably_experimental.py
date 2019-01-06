from itertools import combinations_with_replacement, permutations, combinations
from math import factorial
from functools import reduce

def probability(dice_number, sides, target):
    def prob(dice_number, sides, target):
        max_throw = target - (dice_number - 1) * 1
        if max_throw > sides:
            max_throw = sides

        min_throw = target - (dice_number - 1) * sides
        if min_throw < 1:
            min_throw = 1

        if min_throw > sides:
            return 0

        if dice_number == 1:
            return 1

        throw_list = [i for i in range(min_throw, max_throw + 1)]

        possibilities = 0
        for throw in throw_list:
            n_dice = dice_number - 1
            new_target = target - throw
            possibilities += prob(n_dice, sides, new_target)

        return possibilities

    throws_OK = prob(dice_number, sides, target)

    return throws_OK / sides ** dice_number

def probability_2(dice_number, sides, target):

    dice_throw = list(range(1,sides+1))

    unique_throws = combinations_with_replacement(dice_throw,dice_number)
    # print(len(list(unique_throws)))
    throws_sum = 0

    for i in unique_throws:
        if sum(i) == target:
            perm = permutations(i,dice_number)
            throws_sum += len(set(perm))

    return throws_sum / sides ** dice_number


def probability_3(dice_number, sides, target):

    dice_throw = list(range(1,sides+1))

    unique_throws = combinations_with_replacement(dice_throw,dice_number)
    # print(len(list(unique_throws)))
    throws_sum = 0

    for i in unique_throws:
        if sum(i) == target:
            r = set(i)
            l = [i.count(q) for q in r]
            m = [factorial(q) for q in l]
            throws_sum += factorial(sum(l)) / reduce(lambda x,y: x*y, m)


    return throws_sum / sides ** dice_number

a = []
c = []
import numpy as np

n_dice = 3
n_side = 8

range_of_throws = range(n_dice, n_dice * n_side + 1)

A = probability(n_dice, n_side, 15)
A_ = A*(n_side**n_dice)
B =  probability_3(10, 10, 50)
# for i in range_of_throws:
#     a.append(probability(n_dice, n_side, i))
#     c.append(probability_2(n_dice, n_side, i))
##    print(i)

####hist = np.histogram(a,bins=list(range(5,25)))
##import matplotlib.pyplot as plt
##plt.scatter(list(range_of_throws),a)
##plt.show()

b = [i * (n_side ** n_dice) for i in a]

##assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
##assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
##assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
##assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
##assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
##print('heyo')
##cProfile.run(probability(10, 10, 50))
##assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
##print('done')
