def checkio(my_with_values: list) -> list:
    # TODO make beauty
    def find_not_repeated_elements(list_with: list):
        unique = {}
        for value in list_with:
            if value not in unique.keys():
                unique[value] = 1
            else:
                unique[value]+= 1
        return [key for key, value in unique.items() if value != 1]

    not_unique = find_not_repeated_elements(my_with_values)
    if not len(not_unique):
        return []
    res =  [x for x in my_with_values if x in not_unique ]
    return  res

assert checkio([1, 2, 3, 1, 3]) == [1, 3, 1, 3]
assert checkio([1, 2, 3, 4, 5]) == []
assert checkio([5, 5, 5, 5, 5]) == [5, 5, 5, 5, 5]
assert checkio([10, 9, 10, 10, 9, 8]) == [10, 9, 10, 10, 9]
assert checkio([2, 2, 3, 2, 2]) == [2, 2, 2, 2]
assert checkio([10, 20, 30, 10]) == [10, 10]
assert checkio([7]) == []
assert checkio([0, 1, 2, 3, 4, 0, 1, 2, 4]) == [0, 1, 2, 4, 0, 1, 2, 4]
assert checkio([99, 98, 99]) == [99, 99]
assert checkio([0, 0, 0, 1, 1, 100]) == [0, 0, 0, 1, 1]
assert checkio([0, 0, 0, -1, -1, 100]) == [0, 0, 0, -1, -1]
