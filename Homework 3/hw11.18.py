# Chiamaka Ugbaja
# 1772427

list1 = list(map(int, input().split()))  # takes the list of integers and splits it
empty_list = []  # empty list need to refill with needed answer

for i in list1:  # loop to iterate through given list
    if i >= 0:  # checks if element is positive
        empty_list.append(i)  # amends element into empty_list

empty_list.sort()  # sort the empty_list list
print(*empty_list, end=' ')  # prints sorted list
