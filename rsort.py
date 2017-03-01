l1 = [1,3,12,312,321,545,213,435,12,32,4]

def bigger(a,b):
    if a > b:
        return -1
    if a < b:
        return 1
    return 0

print sorted(l1,bigger)
