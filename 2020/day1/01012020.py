def read_integers(filename):
    integer_list = []
    with open(filename) as f:
        for line in f:
            integer_list.append(int(line.strip('\n')))
    return integer_list

    
    
my_list = read_integers("list.txt")

def need_value(integer_list, needed_value):
    for found_int in integer_list:
        need_int = needed_value - found_int
        if need_int in integer_list:
            return [need_int,found_int]

print(need_value(my_list,2020)[0]*need_value(my_list,2020)[1])
for found_int in my_list:
    needed_value = 2020 - found_int
    if need_value(my_list, needed_value):
        print(found_int*need_value(my_list, needed_value)[0]*need_value(my_list, needed_value)[1])
        break
    

