import numpy as np

def median_calculation(num1, num2):

    '''array merge and median calculation'''
    arr = np.append(num1, num2)

    result = np.median(arr)
    print(arr)
    return result



try:
    # num1 array input
    user_input1 = input().split()
    num1 = list(map(int,user_input1))
    num1 = np.array(num1)

    # num2 array input
    user_input2 = input().split()
    num2 = list(map(int,user_input2))
    num2 = np.array(num2)

        # function calling
    median = median_calculation(num1, num2)
    print(median)
        
except:
    pass

