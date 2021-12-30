import random as rand


def generate_random_number(mag: float or int, event: int, dim: int) -> list:
    """

    :param mag: range [0, mag]
    :param event: number of random events
    :param dim: dimension of coordinate
    :return: return a 2-D list of random numbers
    """
    l = [[rand.uniform(0, mag) for i in range(dim)] for j in range(event)]
    return l


number_of_event = 10000000
rand_list = generate_random_number(1, number_of_event, 2)  # only consider a quarter circle as it is y-axis symmetry
selected_list = [rand_list[i] for i in range(number_of_event) if rand_list[i][0] ** 2 + rand_list[i][1] ** 2 <= 1]
num_of_points = len(selected_list)
print(num_of_points)
y_bar = sum(selected_list[i][1] for i in range(num_of_points))/num_of_points

pi_est = 4/(3 * y_bar)
print(pi_est)