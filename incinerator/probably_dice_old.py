from itertools import product

def probability(dice_number, sides, target):


    max_throw = target-(dice_number-1)*1
    max_throw = min(max_throw, sides)

    min_throw = target - (dice_number-1)*sides
    min_throw = max(min_throw, 1)

    if min_throw >= sides:
        return 0

    throw_list = [i for i in range(min_throw,max_throw+1)]
    # print(throw_list)
    all_combos = product(throw_list, repeat=dice_number)

    i = 0
    o = 0
    for c in all_combos:
        # print(c)
        # print(sum(c))
        # o += 1
        if sum(c) == target:
            i += 1
            # print(c)

    return i / sides ** dice_number


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    # probability(2, 3, 7)
    # assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    # assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    # assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    # assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    # assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    # assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    # assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
