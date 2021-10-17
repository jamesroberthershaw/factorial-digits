import numpy as np
import sys

if(len(sys.argv)>2):#in case the user has inputted too many arguments
    print("Too many arguments provided by user, please try again")

elif(len(sys.argv)==1):#in case the user has not inputted any arguments
    print("No number provided by user, please try again")

else:#user inputted command correctly
    user_input = int(sys.argv[1])
    n = np.math.factorial(user_input)
    x = [(n//(10**i))%10 for i in range(np.math.ceil(np.math.log(n, 10))-1, -1, -1)]                #Fill array x with digits of factorial
    factorial_sum = sum(x)

    print(factorial_sum)
