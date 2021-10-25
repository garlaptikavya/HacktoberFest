def totalWays(n, m):
 
    # base case: invalid input
    if n < 0:
        return 0
 
    # base case: 1 way (with no steps)
    if n == 0:
        return 1
 
    count = 0
    for i in range(1, m + 1):
        count += totalWays(n - i, m)
 
    return count
