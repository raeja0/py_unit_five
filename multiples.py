def get_sum(number):
    sum = 0
    for x in range(number):
        print("x =", x)
        if x % 3 == 0 or x % 5 == 0:
            print("Adding", x, "to the total")
            sum += (x)
            print("Total =", sum)
    print(sum)
get_sum(10)