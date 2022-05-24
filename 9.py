

lst1 = [1, 86, 15, 16, 97, 56, 23, 14, 18]

def bubble(lst):
    last_item = len(lst) - 1 
    for i in range(0, last_item):
        for x in range(0, last_item):
            if lst[x] > lst[x+1]:
                lst[x], lst[x+1] = lst[x+1], lst[x]
    return lst

lst1_sorted = bubble(lst1)

print(lst1_sorted)

