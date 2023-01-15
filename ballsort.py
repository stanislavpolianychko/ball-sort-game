import random
import string
import addition_functions as add_func


def field_generator(rows: int, columns: int):
    # create 2d list for field
    field = [[None for _ in range(columns)] for _ in range(rows)]

    # get indexes of free columns
    free_column_1 = random.randint(0, columns - 1)
    free_column_2 = random.randint(0, columns - 1)

    while free_column_1 == free_column_2:
        free_column_2 = random.randint(0, columns)

    # set space symbol in free columns
    for row_index in range(rows):
        field[row_index][free_column_1] = ' '
        field[row_index][free_column_2] = ' '

    # set different balls symbols in every column
    all_symbols_string = string.ascii_letters + string.punctuation
    used_symbols = ' '

    while add_func.is_value_in_2d_list(None, field):
        random_character = random.choice(all_symbols_string)
        while random_character in used_symbols:
            random_character = random.choice(all_symbols_string)
        used_symbols += random_character

        while add_func.count_of_value_in_2d_list(random_character, field) < rows:
            random_row_id = random.randint(0, rows - 1)
            random_cols_id = random.randint(0, columns - 1)

            if not field[random_row_id][random_cols_id]:
                field[random_row_id][random_cols_id] = random_character

    return field
