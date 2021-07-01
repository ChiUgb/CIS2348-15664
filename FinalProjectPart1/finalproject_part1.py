# Chiamaka Ugbaja
# 1772427

import csv
from operator import itemgetter
from datetime import datetime

# empty lists that each csv data into so it can be easier to manipulate
manufacturer_list = []
price_list = []
service_d_list = []

# Adding the data from each csv file in to the empty lists
with open("ManufacturerList.csv") as manulist:
    read_ml = csv.reader(manulist)
    read_ml = sorted(read_ml, key=itemgetter(0))
    for line in read_ml:
        manufacturer_list.append(line)

with open("PriceList.csv") as pricelist:
    read_pl = csv.reader(pricelist)
    read_ml = sorted(read_ml, key=itemgetter(0))
    for line in read_pl:
        price_list.append(line)

with open("ServiceDatesList.csv") as sdlist:
    read_sl = csv.reader(sdlist)
    read_ml = sorted(read_ml, key=itemgetter(0))
    for line in read_sl:
        service_d_list.append(line)

# sort the list so it is in order by ID so it listed and nicely aligned
new_manufacturer_list = (sorted(manufacturer_list, key=itemgetter(0)))
new_price_list = (sorted(price_list, key=itemgetter(0)))
new_service_d_list = (sorted(service_d_list, key=itemgetter(0)))

# appending the missing service dates and prices to the main list
for i in range(0, len(new_manufacturer_list)):
    new_manufacturer_list[i].append(new_price_list[i][1])

for i in range(0, len(new_manufacturer_list)):
    new_manufacturer_list[i].append(new_service_d_list[i][1])

final_list = new_manufacturer_list
complete_inventory = (sorted(final_list, key=itemgetter(1)))

# writing the FullInventory.csv with the complete_inventory list in required order
with open('FullInventory.csv', 'w') as new_file:
    full_write = csv.writer(new_file)
    for phrase in range(0, len(complete_inventory)):
        full_write.writerow([complete_inventory[phrase][0], complete_inventory[phrase][1],
                             complete_inventory[phrase][2], complete_inventory[phrase][4],
                             complete_inventory[phrase][5], complete_inventory[phrase][3]])

# creating a list for each item type: laptop, phone, and tower
item_type = final_list
laptop_list = []
phone_list = []
tower_list = []

# searching through the list for for item type and appending it to its matching empty list
for word in range(0, len(item_type)):
    if item_type[word][2] == "tower":
        tower_list.append(item_type[word])
    elif item_type[word][2] == "phone":
        phone_list.append(item_type[word])
    elif item_type[word][2] == "laptop":
        laptop_list.append(item_type[word])
    else:
        break

# Writing each file for the laptop, phone, and tower item type
with open('LaptopInventory.csv', 'w') as newfile:
    new_lap_write = csv.writer(newfile)
    for i in range(0, len(laptop_list)):
        new_lap_write.writerow([laptop_list[i][0], laptop_list[i][1], laptop_list[i][4], laptop_list[i][5],
                                laptop_list[i][3]])

with open('PhoneInventory.csv', 'w') as newfile:
    new_phone_write = csv.writer(newfile)
    for i in range(0, len(phone_list)):
        new_phone_write.writerow([phone_list[i][0], phone_list[i][1], phone_list[i][4],
                                  phone_list[i][5], phone_list[i][3]])

with open('TowerInventory.csv', 'w') as newfile:
    new_tower_write = csv.writer(newfile)
    for i in range(0, len(tower_list)):
        new_tower_write.writerow([tower_list[i][0], tower_list[i][1], tower_list[i][4],
                                  tower_list[i][5], tower_list[i][3]])

# splits the date string by "/" in order to compare the date to current date using datetime()
new_d_list = []
present = datetime.now()


def split_servicedate(service_d_list):
    for date in service_d_list:
        x = date[1].split("/")
        item_date = datetime(int(x[2]), int(x[0]), int(x[1]))
        if item_date < present:
            new_d_list.append(date)


split_servicedate(service_d_list)

# writes new file for service dates that occur before today/day code is ran
with open('PastServiceDateInventory.csv', 'w') as newfile:
    count = 0
    new_past_sdl_write = csv.writer(newfile)
    # compares every date in the expired list to all the items in the manufacturing list
    # once it finds the matching id it writes it onto the csv file
    for item in new_d_list:
        for i in range(len(new_manufacturer_list)):
            if item[0] == new_manufacturer_list[i][0]:
                new_past_sdl_write.writerow([new_manufacturer_list[i][0], new_manufacturer_list[i][1],
                                             new_manufacturer_list[i][2], new_manufacturer_list[i][4],
                                             new_manufacturer_list[i][5], new_manufacturer_list[i][3]])

# empty list for the damaged products in the entire inventory
damagedlist = []

# looks through inventory and determines if listed item has been damaged based on position
for i in range(0, len(item_type)):
    if item_type[i][3] == "damaged":
        damagedlist.append(item_type[i])

damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))

# writing new file to put damaged products within in required order order
with open('DamagedInventory.csv', 'w') as newfile:
    damaged_write = csv.writer(newfile)
    for i in range(0, len(damagedlist)):
        damaged_write.writerow([damagedlist[i][0], damagedlist[i][1], damagedlist[i][2], damagedlist[i][4],
                                damagedlist[i][5]])

# The user input for their manufacturer and item type so output can generated

input_manuf = str(input("Enter your manufacturer: "))
input_type = str(input("Please enter your item type: "))
