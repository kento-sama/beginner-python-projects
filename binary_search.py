import random

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
        return -1
    
def binary_search(l, target):
    low = 0
    high = len(l) - 1
    mid = (low + high // 2)
    
    while target != l[mid]:
        print(l[low:high])
        if low > high:
            return -1
        elif target > l[mid]:
            low = mid + 1
        else:
            high = mid - 1
        mid = (low + high) // 2
        
    return mid

def binary_search_rec(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1
    print(l[low:high])
    if low > high:
        return -1
    
    mid = (low + high) // 2
    
    if target == l[mid]:
        return mid
    elif target > l[mid]:
        return binary_search_rec(l, target, mid + 1, high)
    else:
        return binary_search_rec(l, target, low, mid - 1)    
    
    
my_list = [1, 3, 4, 5, 12, 14, 16, 17, 20, 21, 26, 32, 35, 37, 39, 42, 43, 47, 48, 52, 53, 54, 56, 57, 58, 61, 63, 69, 74, 76, 77, 81, 86, 88, 90, 91, 92, 96, 99]
index = binary_search(my_list, 16)
print(index)
print(my_list[index])

index = binary_search_rec(my_list, 16)
print(index)
print(my_list[index])