#x = int(input("Please neter the value: "))
def fido(x):
    if x == 0:
        return 1
    else:
        return x * fido(x - 1)


print(fido(5))

