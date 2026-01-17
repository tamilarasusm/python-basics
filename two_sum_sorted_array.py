def two_sum(arr, target):
    left = 0
    right = len(arr) -1
    current_sum = arr[left] + arr[right]
    while (left < right) :
        current_sum = arr[left] + arr[right]
        if current_sum < target:
            left = left + 1
        elif current_sum > target:
            right = right - 1
        else:
            return True
    
    return False

def two_sumTest(arr, target):
    left, right = 0, len(arr) - 1
    while(left < right):
        current_sum = arr[left] + arr[right]
        if current_sum == target: return True
        left, right = (left+1, right) if left < target else (left, right-1)
    return False


print(two_sumTest([1, 3, 5, 7, 9], 12))  # True
print(two_sumTest([1, 2, 4, 8], 10))     # True
print(two_sumTest([1, 2, 3, 4], 8))      # False

