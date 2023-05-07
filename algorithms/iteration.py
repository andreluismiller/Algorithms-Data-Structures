def calculate_itr(n):
    """Iterative function to calculate the square of x numbers, with 1<=x<n
    
    Keyword arguments:
    n -- positive integer
    Return: list of numbers
    Time complexity: 0(n)
    """
    
    #Loop
    while n > 0:    #O(n+1)
        x = n ** 2  #O(1) 
        print(x)    #O(1)
        n = n - 1   #O(1)


calculate_itr(4)
    