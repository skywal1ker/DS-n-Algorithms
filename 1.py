def sayhi(x):
    if x == 0:
        return
    else:
        print("Hello World!")
        sayhi(x-1)

sayhi(4)

