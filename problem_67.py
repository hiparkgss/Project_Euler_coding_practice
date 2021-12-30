file = 'p067_triangle.txt'

with open(file) as f:
    line_list = [[int(element) for element in line.strip('\n').split()] for line in f.readlines()]

while len(line_list) > 1:
    dim = len(line_list)
    bottom_row = [max(line_list[dim-1][i], line_list[dim-1][i+1]) for i in range(dim-1)]
    modified_second_bottom_row = [bottom_row[i] + line_list[dim-2][i] for i in range(dim-1)]
    line_list.pop()
    line_list[dim-2] = modified_second_bottom_row

print(line_list[0][0])