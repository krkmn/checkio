def fastest_horse(horses: list) -> int:

    times = [secondize(x) for one_race in horses for x in one_race]
    races = len(times)//len(horses)
    sum_times = []

    for i in range(races):
        sum_times.append(sum(times[i::races]))

    return sum_times.index(min(sum_times)) + 1


def secondize(string_time):

    minute , second = string_time.split(':')
    return int(minute)*60 + int(second)




if __name__ == '__main__':
    print("Example:")
    print(fastest_horse([['1:13', '1:26', '1:11']]))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert fastest_horse([['1:13', '1:26', '1:11'], ['1:10', '1:18', '1:14'], ['1:20', '1:23', '1:15']]) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")