def sort_list_imperative(array:list) -> list:
    for i in range(len(array) - 1):
        max_numb = i
        for j in range(i + 1, len(array)):
            if array[j] > array[max_numb]:
                max_numb = j
        array[i], array[max_numb] = array[max_numb], array[i]
    return array


def sort_list_declaratuve(array: list) -> list:
    return sorted(array, reverse=True)


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sort_list_imperative(array))
    print(sort_list_declaratuve(array))