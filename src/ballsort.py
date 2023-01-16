import random
from src import addition_functions as add_func


# function generate main game field and full it with all necessary chars
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
        field[row_index][free_column_2] = field[row_index][free_column_1] = ' '

    # set different balls symbols in every column
    used_symbols = ' '

    while add_func.is_value_in_2d_list(None, field):
        random_character = add_func.get_random_char()
        while random_character in used_symbols:
            random_character = add_func.get_random_char()
        used_symbols += random_character

        while add_func.count_of_value_in_2d_list(random_character, field) < rows:
            random_row_id = random.randint(0, rows - 1)
            random_cols_id = random.randint(0, columns - 1)

            if not field[random_row_id][random_cols_id]:
                field[random_row_id][random_cols_id] = random_character

    return field


# function which carry out movement of chosen char from start column to end
def move_down_as_possible(field: list, start_column_index, end_column_index):
    # variables
    rows = len(field)
    cols = len(field[0])
    rows_max_id = rows - 1

    # start reviews
    if start_column_index == end_column_index or field[rows_max_id][start_column_index - 1] == ' '\
            or field[0][end_column_index - 1] != ' ':
        print("Ops... You chose wrong columns :(")
        return

    # get char from start in char for exchange variable
    start_index = 0
    while field[start_index][start_column_index - 1] == ' ':
        start_index += 1
    char_for_exchange = field[start_index][start_column_index - 1]

    if field[rows_max_id][end_column_index - 1] == ' ':
        field[rows_max_id][end_column_index - 1] = char_for_exchange
        field[start_index][start_column_index - 1] = ' '
        return

    # set char in end column
    end_index = 0
    while field[end_index][end_column_index - 1] == ' ':
        end_index += 1

    if field[end_index][end_column_index - 1] == char_for_exchange:
        field[end_index - 1][end_column_index - 1] = char_for_exchange
        field[start_index][start_column_index - 1] = ' '
    else:
        print("Ops... You chose wrong columns :(")
        return


# function check if all chars in every column are identical
def check_win(field: list, rows, cols):
    for i in range(cols):
        if field[rows - 1][i] != field[0][i]:
            return False
    return True


# function present game field in terminal output
def present_field(field: list):
    for row_index, row in enumerate(field):
        print(row_index+1, *row, sep='|', end='|\n')
    print(' ', *['=' for _ in range(len(field[0]))])
    print(' ', *[i + 1 for i in range(len(field[0]))])


# main game function
def run_game():
    # set variables
    num_of_rows = 4
    num_of_columns = 6
    field = field_generator(num_of_rows, num_of_columns)

    # present game field for start
    present_field(field)

    # main game loop which ends when every char in all columns are same
    while not check_win(field, num_of_rows, num_of_columns):
        start_column_position = int(input("Get char from which column? - "))
        end_column_position = int(input("Set it on which column? - "))
        move_down_as_possible(field, start_column_position, end_column_position)
        present_field(field)

    # message, when game ends
    print("Congratulations! You won : )")
