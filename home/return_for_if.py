def return_for_if():

    for i in range(0,100):
        
        if i == 10:
            pass
            

    return 'bye'
    return 'hello'


return_ = return_for_if()

assert return_for_if() == 'hello', "Should break out of for loop"

print(return_)
