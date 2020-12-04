def check_range(min_val, found_val, max_val):
    if not (min_val <= int(found_val) <= max_val):
        return False
    else:
        return True
    
def check_byr(found_value):
    return check_range(1920, found_value, 2002)

def check_iyr(found_value):
    return check_range(2010, found_value, 2020)

def check_eyr(found_value):
    return check_range(2020, found_value, 2030)

def check_hgt(found_value):
    metric = found_value[-2:]
    height = found_value[:-2]
    if not metric in ["in","cm"]:
        return False
    if metric == "in" and (not check_range(59, int(height),76)):
        return False    
    if metric == "cm" and (not check_range(150, int(height),193)):
        return False    
    return True

def check_hcl(found_value):
    if not found_value[0] == "#":
        return False
    colorcode = found_value[1:]
    if not len(colorcode) == 6:
        return False
    for position in colorcode:
        if (not position in "1234567890abcdef"):
            return False
    return True

def check_ecl(found_value):
    if not found_value in ["amb","blu","brn","gry","grn","hzl","oth"]:
        return False
    return True

def check_pid(found_value):
    if not len(found_value) == (9):
        return False
    for position in found_value:
        if (not position in "1234567890"):
            return False
    return True


def check_valid(required_fields, found_fields):
    for check_field in required_fields:
        if not check_field in found_fields:
            return False
    return (check_byr(found_fields["byr"]) and 
            check_iyr(found_fields["iyr"]) and 
            check_eyr(found_fields["eyr"]) and
            check_hgt(found_fields["hgt"]) and
            check_hcl(found_fields["hcl"]) and
            check_ecl(found_fields["ecl"]) and
            check_pid(found_fields["pid"]))

valid = 0
invalid = 0
check_values = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
check_pass = {}
with open("input.txt") as f:
    for line in f:
        if  line == "\n":
            if (check_valid(check_values,check_pass)):
                valid +=1
            else:
                invalid +=1
            check_pass = {}
        else:
            items = line.strip('\n').split()
            for item in items:
                check_pass[item.split(":")[0]]=item.split(":")[1]
    if (check_valid(check_values,check_pass)):
        valid +=1
    else:
        invalid +=1
f.close()
print("number of valid passports:"+str(valid))
