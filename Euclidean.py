#find the gcd of 2 numbers a and b with recursive subtraction
def gcd_subtract(a, b):
    if a == b:
        return a
    if a > b:
        gcd_subtract(a - b, b)
    else:
        gcd_subtract(a, b - a)

#find the gcd of 2 numbers a and b with recursive division
def gcd_divide(a, b):
    if a % b == 0:
        return a
    else:
        return gcd(b, a % b)
