def calculate_rcr(n):
    """Recursive function to calculate the square of x numbers, with 1<=x<n
    
    Keyword arguments:
    n -- positive integer 
    Return: list of numbers
    Time complexity: T(n-1)+1 for n>0; 1 for n=0
    """

    # Base condition
    if n > 0:           #O(1)
        x = n ** 2      #O(1)
        print(x)        #O(1)
        # Recursive call
        calculate_rcr(n-1)  #T(n-1)


calculate_rcr(4)
