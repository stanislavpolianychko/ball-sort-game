def is_value_in_2d_list(value, lst_2d: list):
    for nested_list in lst_2d:
        if value in nested_list:
            return True
    return False


def count_of_value_in_2d_list(value, lst_2d: list):
    result = 0
    for nested_list in lst_2d:
        result += nested_list.count(value)
    return result
