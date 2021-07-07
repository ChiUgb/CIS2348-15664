# Chiamaka Ugbaja
# 1772427

# Global variable
num_calls = 0


# TODO: Write the partitioning algorithm - pick the middle element as the
#       pivot, compare the values using two index variables l and h (low and high),
#       initialized to the left and right sides of the current elements being sorted,
#       and determine if a swap is necessary
def partition(user_ids, i, k):
    bottom = (i - 1)
    middle = (i + k) // 2
    pivot = user_ids[middle]
    user_ids[middle], user_ids[k] = user_ids[k], user_ids[middle]
    for j in range(i, k):
        if user_ids[j] <= pivot:
            bottom = bottom + 1
            user_ids[bottom], user_ids[j] = user_ids[j], user_ids[bottom]
    user_ids[bottom + 1], user_ids[k] = user_ids[k], user_ids[bottom + 1]
    return bottom + 1


# TODO: Write the quicksort algorithm that recursively sorts the low and
#       high partitions. Add 1 to num_calls each time quisksort() is called
def quicksort(user_ids, i, k):
    global num_calls
    num_calls += 1
    if i < k:
        pivot_index = partition(user_ids, i, k)
        quicksort(user_ids, i, pivot_index - 1)
        quicksort(user_ids, pivot_index + 1, k)


if __name__ == "__main__":
    user_ids = []
    user_id = input()
    while user_id != "-1":
        user_ids.append(user_id)
        user_id = input()

    # Initial call to quicksort
    quicksort(user_ids, 0, len(user_ids) - 1)

    # Print number of calls to quicksort
    print(num_calls)

    # Print sorted user ids
    for user_id in user_ids:
        print(user_id)
