def fib(num):
    a = 1
    b = 1
    test = "1 1 "
    for x in range(num):
        c = b + a
        test += str(c) + (" ")
        a = b
        b = c
    print(test)
fib(5)