my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_numbers(numbers):
    if len(numbers) == 0:
        print("Конец списка")
        return
    else:
        print(numbers[0])

    print_numbers(numbers[1:])


print_numbers(my_list)
