x = int(input("Please enter the value: "))


def sum(x):
    if x == 0:
        return 0
    else:
        return x + sum(x-1)


k = sum(x)

print("your value will be", k)


