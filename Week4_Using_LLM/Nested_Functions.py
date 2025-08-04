
## Average numbers entered by user

def average_numbers(input_list):
    total = 0
    for number in input_list:
        total += number

    if len(input_list) > 0:
        return total / len(input_list)
    else:
        return 0


# test = []
# print(average_numbers(test))


def average_user_numbers():
    keep_asking = "yes"
    number_list = []
    while keep_asking != "quit":
        keep_asking = input("Enter a number or quit to end ")
        if keep_asking != "quit":
            number_list.append(int(keep_asking))
    output = average_numbers(number_list)
    return output


# print(average_user_numbers())





