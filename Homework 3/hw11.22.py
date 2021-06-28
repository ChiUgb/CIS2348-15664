# Chiamaka Ugbaja
# 1772427

phrase = input().split()  # splits the phrase up into words
for i in phrase:  # looks at each element in phrase
    count = 0
    for j in phrase:  # loops through the phrase and iterates count it occurs more than once
        if j == i:
            count += 1
    print(i, count)  # prints word with amount of occurrences
