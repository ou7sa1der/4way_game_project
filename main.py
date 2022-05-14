def check_for_winner(ma, player, current_position_choice):
    field = ma
    player = player
    current_choice_for_position = current_position_choice
    line = current_choice_for_position[0]
    column = current_choice_for_position[1]

    #horizontal - current position to right
    try:
        if field[line][column + 1] == player and field[line][column + 2] == player and field[line][column + 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    # horizontal - current position to left
    try:
        if field[line][column - 1] == player and field[line][column - 2] == player and field[line][column - 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #vertical - current position and down
        if field[line + 1][column] == player and field[line + 2][column] == player and field[line + 3][column] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal up and left
        if field[line - 1][column - 1] == player and field[line - 2][column - 2] == player and field[line - 3][column - 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal up and right
        if field[line - 1][column + 1] == player and field[line - 2][column + 2] == player and field[line - 3][column + 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        # diagonal down and left
        if field[line + 1][column - 1] == player and field[line + 2][column - 2] == player and field[line + 3][column - 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal down and right
        if field[line + 1][column + 1] == player and field[line + 2][column + 2] == player and field[line + 3][column + 3] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #two positions left and one right
        if field[line][column - 1] == player and field[line][column - 2] == player and field[line][column + 1] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #one position left and two right
        if field[line][column - 1] == player and field[line][column + 1] == player and field[line][column + 2] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #two positions right and one left
        if field[line][column + 1] == player and field[line][column + 2] == player and field[line][column - 1] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #one position right and two left
        if field[line][column + 1] == player and field[line][column - 1] == player and field[line][column - 2] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal right two up and left one down
        if field[line - 1][column - 1] == player and field[line - 2][column - 2] == player and field[line + 1][column + 1] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal right one up and left two down
        if field[line - 1][column + 1] == player and field[line + 1][column - 1] == player and field[line + 2][column - 2] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal left two up and right one down
        if field[line - 1][column - 1] == player and field[line - 2][column - 2] == player and field[line + 1][column + 1] == player:
            for el in matrix:
                print(el)
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    try:
        #diagonal left one up and right two down
        if field[line - 1][column - 1] == player and field[line + 1][column + 1] == player and field[line + 2][column + 2] == player:
            print(f'The winner is player {player}')
            exit()
    except IndexError:
        pass

    return False


def making_a_move(ma, player_choice, moves):

    field = ma
    selected_column = player_choice
    player = 2 if moves % 2 != 0 else 1
    flag = True
    # have to iterate through the matrix(columns) somehow
    for ro in range(rows - 1, -1, -1):
        for col in range(cols - 1, -1, -1):

            if field[ro][col] == 0 and col + 1 == selected_column:
                field[ro][col] = player
                current_position = [ro, col]
                if not check_for_winner(field, player, current_position):
                    return flag
    for el in field:
        if 0 not in el:
            print('Draw, start another game')
            exit()
    print(f'Column {selected_column} is full, please Player {player} choose another one')
    flag = False
    return flag


def check_if_input_valid(number_of_column):
    selected_column = number_of_column
    if 0 < selected_column <= cols:
        return True
    else:
        return False


# assuming the field will be with set rows and cols
rows = 6
cols = 7
# starting with 1 to check which player is on turn, the logic - if it is even or not
count_moves = 1

# setting up the field with zeros
matrix = []

for row in range(rows):
    matrix.append([0 for el in range(cols)])

while True:
    # check if the chosen column is in range of the field and if it is not a random string
    try:
        player_input = int(input('Player 1, please choose a column: ')) if count_moves % 2 != 0 else int(
            input('Player 2, please choose a column: '))
        count_moves += 1
        if not check_if_input_valid(player_input):
            print('Invalid column, please enter number between 1 and 7')
            count_moves -= 1
            continue
    except ValueError:
        print('Invalid column, please enter number between 1 and 7')
        continue

    # to reach this line the input is valid

    if not making_a_move(matrix, player_input, count_moves):
        count_moves -= 1
        continue
    # here we check if the column is full and if it is it goes back to input for a new column

    # next we have to think for the logic checking if there is a winner after the move

    # printing the field
    for el in matrix:
        print(el)
