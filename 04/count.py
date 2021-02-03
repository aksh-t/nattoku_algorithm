# 4.2
def count(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return 1
    return 1 + count(arr[1:])


print(count([1, 2, 3, 4]))
