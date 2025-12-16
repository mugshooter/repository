def two_sum_hashed_all(lst, target):
    hash_table = {}
    result = []
    for i, num in enumerate(lst):
        hash_table[num] = i
    for i, num in enumerate(lst):
        complement = target - num
        if complement in hash_table and hash_table[complement] != i:
            pair = (i, hash_table[complement]) if i < hash_table[complement] else (hash_table[complement], i)
            if pair not in result:
                result.append(pair)
    return result



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 8
result = two_sum_hashed_all(lst, target)
print(result)