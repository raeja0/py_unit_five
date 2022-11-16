def multi(num):
    test = ""
    for x in range(1, 13):
        test += str(x*num) + (" ")
    return test
def main():
    print(multi(7))
main()