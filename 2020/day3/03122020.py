def calculate_steps(hor_slope, vert_slope):
    maze = []
    horizontal_position=0
    trees = 0
    with open("input.txt") as f:
        for line in f:
            maze.append(line.strip('\n'))
        for row in maze:
            if (( maze.index(row) % vert_slope) == 0 ):
                found_char = row[horizontal_position % len(row)]
                if (found_char == "#"):
                    trees +=1
                horizontal_position += hor_slope
        return trees
    f.close()
print(calculate_steps(3,1))
result = (calculate_steps(3,1)*calculate_steps(1,1)*calculate_steps(5,1)*calculate_steps(7,1)*calculate_steps(1,2))
print(result)
    


    