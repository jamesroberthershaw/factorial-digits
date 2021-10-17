import numpy as np
import sys

if(len(sys.argv)>2):
    print("Too many arguments provided by user, please try again")

elif(len(sys.argv)==1):
    print("No number provided by user, please try again")

else:
    user_input = int(sys.argv[1])
    n = np.math.factorial(user_input) 
    x = [(n//(10**i))%10 for i in range(np.math.ceil(np.math.log(n, 10))-1, -1, -1)]
    factorial_sum = sum(x)

    print(factorial_sum)
