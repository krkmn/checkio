'''
convert 12 hours to 24 hours
'''

def time_converter(time):

    time, ampm = time.split()
    hour, minute = time.split(':')
    hour = int(hour)
    if ampm == 'a.m.' and hour == 12:
        hour -= 12
    elif ampm == 'p.m.' and hour != 12:
        hour += 12
    
    hour = str(hour).rjust(2,'0')

    return hour+':'+minute

if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
