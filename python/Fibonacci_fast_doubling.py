def increment(stack):
    top, nxt = stack.pop(), stack.pop()
    num = top + nxt
    stack.extend((top,num))
    return num

def double(stack): #fast doubling
    k_plus, k = stack.pop(), stack.pop()
    d = k*(2*k_plus - k)
    d_plus = k_plus**2 + k**2
    stack.extend((d, d_plus))
    return d

# get order of operations from 1 to n, by doubling or incrementing
def getOrderOfOperations(n):
    order = []
    temp = n
    while temp != 1:
        if temp & 1 == 1:
            order.append(1) # incrementing signal
            temp -= 1
        else:
            order.append(0) # fast doubling signal
            temp //= 2
    return order

def fib(n):
    assert not n < 1
    if n == 1:
        return 1
    order = getOrderOfOperations(n)
    # [k-1, k] for incrementing frist
    stack = [0,1] 
    if order[-1] == 0:
        # [k, k+1] for doubling frist
        stack = [1,1]
    while len(order) > 0:
        value = order.pop()
        if value == 1:
            increment(stack)
        if value == 0:
            double(stack)
    stack.pop()
    k = stack.pop()
    return k
