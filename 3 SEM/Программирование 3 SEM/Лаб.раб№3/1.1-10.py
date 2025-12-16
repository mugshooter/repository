# 1.1
set1 = {1, 2, 3, 4, 5}
print('№1.1', set1)

# 1.2
set2 = {16, 7,13}
set2.add(9)
set2.add(19)
print('№1.2', set2)

# 1.3
set3 = {11, 12, 13, 14, 15}
set3.remove(14)
set3.remove(15)
print('№1.3', set3)

# 1.4
set4 = {1, 2, 3}
set5 = {3, 4, 5}
print('№1.4', set4.intersection(set5))

# 1.5
set6 = {10, 11, 12, 13}
set7 = {14, 15, 16, 17}
print('№1.5', set6.union(set7))

# 1.6
set8 = {14, 15, 16, 17, 18}
set9 = {16, 17, 18, 19, 20}
print('№1.6', set8.difference(set9))

# 1.7
set10 = {21, 22, 23}
set11 = {23, 24, 25}
print('№1.7', set10.symmetric_difference(set11))

# 1.8
set12 = {3, 14, 53, 71, 129}
print('№1.8', 3 in set12)

# 1.9
set13 = {51, 312, 14}
set14 = {14, 33, 51, 85, 312}
print('№1.9', set13.issubset(set14))

# 1.10
list1 = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
set15 = set(list1)
list2 = list(set15)
print('№1.10', list2)
