'''
Mission is to calculate the probability of X dice with N sides to have the total sum of S

'''

from math import factorial
from functools import reduce
from itertools import combinations_with_replacement

def probability(dice_number, sides, target):

    dice_throw = range(1,sides+1)

    unique_throws = combinations_with_replacement(dice_throw,dice_number)
    # print(len(list(unique_throws)))
    throws_sum = 0

    for i in unique_throws:
        if sum(i) == target:
            r = set(i)
            l = [i.count(q) for q in r]
            m = [factorial(q) for q in l]
            throws_sum += factorial(sum(l)) / reduce(lambda x,y: x*y, m)  ##  if item i appears a_i times then the total
            ##  number of unique ways a list can be arranged is (a_1+a_2+...+a_n)!/(a_1! a_2! ... a_n!) (got help from ##math at freenode)

    return throws_sum / sides ** dice_number


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
