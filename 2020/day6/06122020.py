group_list = []
answer_list = []
with open("input.txt") as f:
    for line in f:
        if not (line == "\n"):
            line = line.strip("\n")
            for answer in line:
                if not (answer in answer_list):
                    answer_list.append(answer)
        else:
            group_list.append(answer_list)
            answer_list = []
group_list.append(answer_list)
f.close()
sum_count = 0
for item in group_list:
    sum_count += len(item)
print(sum_count)

answer_list=[]
group_list=[]
first_line = True
with open("input.txt") as f:
    for line in f:
        if not (line == "\n"):
            line = line.strip("\n")
            if (first_line):
                for answer in line:
                    answer_list.append(answer)
            else:
                for item in answer_list:
                    if not item in line:
                        index_removal=answer_list.index(item)
                        answer_list[index_removal]="DELETEME"
            first_line = False
        else:
            temp_list=[]
            for item in answer_list:
                if not item == "DELETEME":
                    temp_list.append(item)
            group_list.append(temp_list)
            answer_list = []
            first_line = True
temp_list=[]
for item in answer_list:
    if not item == "DELETEME":
        temp_list.append(item)
group_list.append(temp_list)
f.close()
sum_count = 0
for item in group_list:
    sum_count += len(item)
print(sum_count)
