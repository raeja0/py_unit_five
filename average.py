total = 0
divide = 0
x = 0
while True:
    x = input("Give me an integer! If not, enter q to end the program.")
    if x == "q":
        break
    divide += 1
    total += int(x)
y = total/divide
print("The average is", str(y))