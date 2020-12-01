def read_integers(filename):
    integer_list = []
    with open(filename) as f:
        for line in f:
            integer_list.append(int(line.strip('\n')))
    return integer_list

    
    
my_list = read_integers("list.txt")
for found_int in my_list:
    need_int = 2020 - found_int
    if need_int in my_list:
        result = need_int * found_int
        print(result)
        break
    

