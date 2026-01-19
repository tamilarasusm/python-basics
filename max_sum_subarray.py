def max_sum_subarray(arr, k):
    max_sum = sum(arr[:k])
    current_sum = max_sum

    for i in range(k, len(arr)):
        current_sum += arr[i]       # add new element
        current_sum -= arr[i - k]   # remove old element
        max_sum = max(max_sum, current_sum)

    return max_sum

arr = [2, 1, 5, 1, 3, 2]
k = 3
print(max_sum_subarray(arr, k))