def rotLeft(my_array, rotation):
    helper = 1
    max_index = len(my_array) - 1
    result = [0] * len(my_array)
    for i in range(0, max_index+1):
        number = my_array[i]
        new_index = None
        if i - rotation < 0:
            new_index = max_index - rotation + helper
            helper += 1
        else:
            new_index = i - rotation

        result[new_index] = number

    return result


print(rotLeft([1, 2, 3, 4, 5], 2))
