def fibonacci(n):
    x = 0
    y = 1
    
    if n == 1:
        return 0
        
    if n == 2:
        return 1
    
    for _ in range(n - 2):
        foo = int(x)
        x = int(y)
        y = y + foo
    
    return y