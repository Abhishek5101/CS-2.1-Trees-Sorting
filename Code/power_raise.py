"""
Write a recursive function called raise_power() that takes in 
two integer parameters, the first parameter being the base number 
and the second parameter being the power you want to raise it to.
This function will return the number raised to the given power.
For example, if you called raise_power(4, 2) you would get 16 
returned which is 4^2. Remember to think about what the base and 
recursive cases will be and start with an iterative approach if you 
don't know where to begin.  
"""

"4, 2--> 4 * 4"
"6, 3--> 6*6*6"

def raise_power(num1, num2, prod=1):
    """
    I will multiply num1 by itself num2 times
    and then stop and return the answer
    """
    if num2 == 0:
        return prod
    else:
        prod *= num1
        return raise_power(num1, num2 - 1, prod=prod)



print(raise_power(23,2))
