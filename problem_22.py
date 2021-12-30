file = 'p022_names.txt'
with open(file, 'r') as f:
    name_list = f.read().split(',')

name_list = [name.strip('"') for name in name_list]
name_list.sort()
# print(name_list)

def alphabetical_value(name_string):
    """

    :param name_string: name in an uppercase string
    :return: alphabetical value
    """
    reference = ord('A') - 1
    alphabetical_value_dic = {chr(i): i - reference for i in range(reference + 1, reference + 1 + 27)}
    result_value = 0
    for character in name_string:
        result_value += alphabetical_value_dic[character]

    return result_value

alpha_value_mul_position_result = 0

for index, name in enumerate(name_list):
    alpha_value_mul_position_result += alphabetical_value(name) * (index + 1)
    """
    print(' name is: %s \n position is %d \n alpha_val is %d'
          % (name, index+1, alphabetical_value(name)), end='\n\n')
    """

print(alpha_value_mul_position_result)