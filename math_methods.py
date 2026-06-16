def factorials(n): #factorials
    factorials = 1
    if not isinstance(n, int):
        return "The input is not an integer"
    
    elif n < 0:
        return "undefined"
    
    else:
        for i in range(1,n+1):
            factorials = factorials * i
        return factorials

def nCr(n, r): #combinations
    if not isinstance(factorials(n), int) or not isinstance(factorials(r),int):
        return "input is not an integer"
    
    elif n < 0 or r < 0:
        return "n and/or r cannot be less than zero."

    elif n < r:
        return 0
    
    else:
        return (factorials(n) / (factorials(r) * factorials(n-r)))