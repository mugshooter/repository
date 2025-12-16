def two_sum_hashed(lst, target):
    hash_table = {}
    for i, num in enumerate(lst):
        complement = target - num
        if complement in hash_table:
            return (hash_table[complement], i)
        hash_table[num] = i
    return None



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed(lst, target)
print(result)