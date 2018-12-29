def sun_angle(time):
    #replace this for solution
    hour, minute = int(time[0:2]), int(time[3:])
    if ( (hour*60 + minute) < 6*60 ) or ((hour*60 + minute) > 18*60):
        return "I don't see the sun!"
    else:
        return 180 / (12 * 60) * ((hour - 6) * 60 + minute)


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
