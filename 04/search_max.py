# 4.3
def search_max(arr):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    max_of_rest = search_max(arr[1:])
    if arr[0] > max_of_rest:
        return arr[0]
    else:
        return max_of_rest


print(search_max([6, 1, 2, 5, 3, 4]))
