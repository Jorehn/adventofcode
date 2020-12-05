def calculate_bin(encoded_string, one_char, zero_char):
    encoded_string = encoded_string.replace(one_char,"1")
    encoded_string = encoded_string.replace(zero_char,"0")
    return "0b"+encoded_string

with open("input.txt") as f:
    ID_s=[]
    for line in f:
        line = line.strip("\n")
        encoded_row=line[:7]
        encoded_column=line[-3:]
        binary_row = calculate_bin(encoded_row,"B","F")
        binary_column = calculate_bin(encoded_column,"R","L")
        row = int(binary_row, 2)
        column = int(binary_column,2)
        seat_id = (8*row)+column
        ID_s.append(seat_id)
    print(max(ID_s))
    for counter in range(8):
        if (counter in ID_s):
            ID_s.remove(counter)
        if ((counter+1016) in ID_s):
            ID_s.remove(1016+counter)
    for seat in ID_s:
        if not (seat +1) in ID_s:
            if (seat +2) in ID_s:
                print("found free seat:"+str(seat +1))
        
