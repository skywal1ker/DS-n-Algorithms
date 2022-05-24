
def binarysearch(mylst, target, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) // 2
        if target == mylst[mid]:
            return mid
        elif target < mylst[mid]:
            return binarysearch(mylst, target, start, mid-1)
        else:
            return binarysearch(mylst, target, start, mid+1, stop)

mylst = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
target = 20
start = 0
stop = len(mylst)

x = binarysearch(mylst, target, start, stop)

if x == False:
    print("Item ", target, "Not Found!")
else:
    print("Item ", target, "Found at Index ", x)

   
   
   
   
   
