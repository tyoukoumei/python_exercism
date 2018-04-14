def binary_search(list_of_numbers, number):
    return real_search(list_of_numbers, number, 0)


def real_search(list_of_numbers, number, start):
    if len(list_of_numbers) == 0:
        raise ValueError("not found")
    if len(list_of_numbers) == 1:
        if list_of_numbers[0] == number:
            return start + 0
        else:
            raise ValueError("not found")
    half = len(list_of_numbers) // 2

    mid = list_of_numbers[half]
    if mid == number:
        return start + half
    elif mid > number:
        return real_search(list_of_numbers[0:half], number, start)
    elif mid < number:
        return real_search(list_of_numbers[half:], number, start + half)
