 import numpy as np


a = [int(x) for x in input().split()]

sum_of_squares = 0
for element in a:
    sum_of_squares = sum_of_squares + (element * element)


    
sum_of_it = sum_of_squares / len(a)

print("Result = ", np.sqrt(sum_by_length)) 