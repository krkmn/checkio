'''
convert time into string
'''
import re

def date_time(time: str) -> str:
    #replace this for solution
    time_splits = re.split('[\s:.]',time)
    day = int(time_splits[0])
    months = enumerate(['January', 'February', 'March', 'April', 
                        'May', 'June', 'July', 'August', 
                        'September', 'October', 'November', 'December',], 1)
    month = dict(months)[int(time_splits[1])]
    year = int(time_splits[2])
    hour = int(time_splits[3])
    minute = int(time_splits[4])
    
    if hour == 1:
        hour = str(hour) + ' hour'
    else:
        hour = str(hour) + ' hours'

    if minute == 1:
        minute = str(minute) + ' minute'
    else:
        minute = str(minute) + ' minutes'
    humanized_time = f"{day} {month} {year} year {hour} {minute}"
    
    return humanized_time

if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
