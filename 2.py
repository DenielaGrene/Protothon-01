import numpy as np

# list with input numbers
a = [int(x) for x in input().split()]

sum_squ = 0
for ele in a:
    sum_squ = sum_squ + (ele * ele)


    
sum_by_length = sum_squ / len(a)

print("Result = ", np.sqrt(sum_by_length)) 