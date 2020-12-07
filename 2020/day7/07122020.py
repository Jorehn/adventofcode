def find_bags(bagdict,color):
    baglist = []
    for key in bagdict:
        if bagdict[key].count(color) > 0:
            baglist.append(key)
    return baglist

bag_dict = {}
with open("input.txt") as f:
    for line in f:
        line = line.strip("\n")
        if "contain no" in line:
            words = line.split()
            bag_dict[words[0]+" "+words[1]]=[]
        else:
            templist = line.split()
            bag_color = templist[0]+" "+templist[1]
            templist.clear()
            line = line.split("contain ")[1]
            bag_list = line.split(", ")
            contains_list = []
            for items in bag_list:
                for counter in range(int(items[0])):
                    templist=items.split()
                    contains_list.append(templist[1]+" "+templist[2])
                    templist.clear()
            bag_dict[bag_color]=contains_list
f.close()
color_find = "shiny gold"
ultimate_list = [color_find]
cur_list = len(ultimate_list)
for items in ultimate_list:
    bag_list = []
    bag_list = find_bags(bag_dict,items)
    for found_items in bag_list:
        if not found_items in ultimate_list:
            ultimate_list.append(found_items)
print(len(ultimate_list))

color_find = "shiny gold"
ultimate_list = []
ultimate_list = [color_find]
bag_list = []
for items in ultimate_list:
    for found_items in bag_dict[items]:
        bag_list.append(found_items)
        ultimate_list.append(found_items)
print(len(bag_list))

