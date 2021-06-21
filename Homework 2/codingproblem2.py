# Chiamaka Ugbaja
# 1772427

def new_file():
    month_num = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'july': 7, 'august': 8,
                 'september': 9, 'october': 10, 'november': 11, 'december': 12
                 }  # dictionary of months with assigned into numbers
    with open('inputDates.txt') as f1:  # PART B - opens an reads the file while splitting the list
        l1 = f1.read().splitlines()
    i = 0
    l2 = []
    l3 = []

    for c in range(len(l1)):  # PART A , infinite loop, will always be -1
        if l1[c].find("/") == -1:
            l3.append(l1[c])
    print(l3)

    while l3[i] != "-1":
        string_01 = ""
        new_lis = l3[i].split(" ")
        if (new_lis[0].lower() in month_num.keys() and new_lis[1].endswith(',') and
                (1000 <= int(new_lis[2]) <= 2020)):  # checks the  month and date ending with comma with year being >
            # 1000 and < 2020
            string_01 += str(month_num[new_lis[0].lower()]) + '/' + new_lis[1][:-1] + '/' + new_lis[2] + '\n'  # this
            # is the output string that you need
            l2.append(string_01)  # append into list
        i += 1

    # this is question c
    f2 = open('parsedDates.txt', 'w+')  # if file exists, it will open. If not a new one will be made
    f2.writelines(l2)  # the elements will be formatted in lines
    f2.close()


new_file()
