def factorial(n):
    
    p=1
    for i in range(n):
        p=p*(i+1)
    print(p)
    return

factorial(7)


def factorial_recursive(n):
    if n==1 or n==0:
        return 1
    return n* factorial_recursive(n-1)      # here function call inside function 

s=factorial_recursive(5)
print(s)





