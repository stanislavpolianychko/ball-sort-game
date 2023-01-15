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


def move_down_as_possible(field: list, start_column_index, end_column_index):
    # review if start and end indexes are same
    if start_column_index == end_column_index:
        print("you can not move symbol on same column")
        return

    # get real indexes to use in list
    start_column_index -= 1
    end_column_index -= 1

    # get a top symbol of start column
    if field[len(field) - 1][start_column_index] == ' ':
        print("you choose a free column")
        return

    i = 0
    while field[i][start_column_index] == ' ':
        i += 1
    top_symbol_of_start_column = field[i][start_column_index]

    # put symbol on the top of end column
    if field[0][end_column_index] != ' ':
        print("you choose blocked column")
        return

    if field[len(field) - 2][end_column_index] == ' ':
        field[len(field) - 2][end_column_index] = top_symbol_of_start_column
        field[i][start_column_index] = ' '
        return

    j = 0
    while field[j][end_column_index] == ' ':
        j += 1

    if field[j][end_column_index] != top_symbol_of_start_column:
        print("wrong move")
        return

    j -= 1
    field[i][end_column_index] = top_symbol_of_start_column
    field[j][start_column_index] = ' '
