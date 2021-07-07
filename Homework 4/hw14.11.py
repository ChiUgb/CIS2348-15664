# Chiamaka Ugbaja
# 1772427

def selection_sort_descend_trace(chi):
    for i in range(len(chi) - 1):  # looks through length of input
        lvi = i  # sets each value equal to i for loop
        for k in range(i + 1, len(chi)):  # if next value larger then replace it and print in new order
            if chi[k] > chi[lvi]:
                lvi = k
        chi[i], chi[lvi] = chi[lvi], chi[i]
        for m in chi:
            print(m, end=' ')
        print()
    return chi


if __name__ == '__main__':  # run program first and puts in correct order
    numbers = [int(x) for x in input().split()]
    selection_sort_descend_trace(numbers)
