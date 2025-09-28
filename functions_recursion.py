def sum(a,b):
    return a+b

result=sum(2,3)
print(result)

# recursion

def show(n):
    if n==0:
        return
    print(n)
    show(n-1)

show(5)       

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
factorial=fact(5)
print(factorial)   