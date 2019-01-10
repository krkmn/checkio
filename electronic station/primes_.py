'''
File used primarily for testing for number_factory.py
'''


orig_number = 20
number = orig_number
array = []

def prime(number):

    for i in range(2,int(number**0.5)+1):

        if number/i == int(number/i) and not number/i == 1:
            array.append(i)
            prime(number/i)
            return None

    array.append(int(number))
    return 0



prime(number)
print(array)
new_array = []
L = 0
iter_ = iter(range(1,len(array)))

joined_array = ','.join(map(str,array))

joined_array = joined_array.replace('2,2','4')
joined_array = joined_array.replace('2,3','6')
joined_array = joined_array.replace('2,2,2','8')
joined_array = joined_array.replace('3,3','9')

number = int(''.join(sorted(joined_array.split(','))))



# for i in iter_:
#     if array[i]*array[i-1] <10:
#         new_array.append(array[i]*array[i-1])
#         next(iter_)
#     elif array[i]*array[i-1] >=10:
#         new_array.append(array[i])
#
#     #else:
#        #new_array.append(array[i])
