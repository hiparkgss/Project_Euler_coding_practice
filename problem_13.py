file = 'problem_13_number.txt'

with open(file) as f:
    number_list_in_str = f.read().split()
    number_list = [int(num) for num in number_list_in_str]
    print(str(sum(number_list))[0:10])