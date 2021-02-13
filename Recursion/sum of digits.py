def sumOfDigits(n):
    assert n>=0 and int(n)==n , 'The number should be a non-negative integer'
    if n==0:
        return 0
    else:
        return int(n%10)+sumOfDigits(int(n/10))
