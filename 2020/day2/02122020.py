valid_passwords = 0
with open('input.txt') as f:
    for line in f:
        found_line = line.split()
        min_value = int(found_line[0].split('-')[0])
        max_value = int(found_line[0].split('-')[1])
        check_char = found_line[1][0]
        password = found_line[2]
        count = password.count(check_char)
        if min_value <= count <= max_value:
            valid_passwords+=1
f.close()
print(valid_passwords)
valid_passwords = 0
with open('input.txt') as f:
    for line in f:
        found_line = line.split()
        min_value = int(found_line[0].split('-')[0])
        max_value = int(found_line[0].split('-')[1])
        check_char = found_line[1][0]
        password = found_line[2]
        if (password[min_value-1] == check_char or password[max_value-1] == check_char) and (password[min_value-1] != password[max_value-1]):
            valid_passwords+=1
f.close()
print(valid_passwords)
