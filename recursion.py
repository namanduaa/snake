n=6
def printn(n):
    if(n==0):
        return
    print(n)
    printn(n-1)
printn(n)


n=5
def printn(n):
    if(n==0):
        return
    print(n)
    printn(n-1)
    print("end")

printn(n)

# printn(5)
# Prints 5
# Calls printn(4)

# printn(4)
# Prints 4
# Calls printn(3)

# printn(3)
# Prints 3
# Calls printn(2)

# printn(2)
# Prints 2
# Calls printn(1)

# printn(1)
# Prints 1
# Calls printn(0)
# printn(0)

# https://copilot.microsoft.com/shares/JjgVeN5QrtsA5VjJCBNbn
# Base case → returns immediately (no output here).
# Now the recursion starts unwinding:
# After printn(0) returns, the function at n=1 prints "end".
# Then n=2 prints "end".
# Then n=3 prints "end".
# Then n=4 prints "end".
# Finally n=5 prints "end".


# fact(2) = fact(1) * 2 = 1 * 2 = 2

# fact(3) = fact(2) * 3 = 2 * 3 = 6

n = 5

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fact(n - 1) * n

print(fact(n))


def sum(n):
    if  n == 0:
        return 0
    return sum(n - 1) + n

print(sum(5))


list = ["a", "b", "c", "d"]
def elements(list, n):
    if n==len(list):
        return
    print(list[n])
    elements(list,n+1)
elements(list, 0)


sum(1) =1
sum(2) =1+2
sum(3) =1+2+3
sum(4) =1+2+3+4
sum(5) =1+2+3+4+5