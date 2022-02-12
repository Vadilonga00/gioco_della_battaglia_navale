import warnings
import ship_types
import Utils


def create_board(args, type_list):
    board = [[0] * args.columns for x in range(args.rows)]
    ship_list = []
    for i in type_list:
        successful_insertion = False

        while not successful_insertion:
            start_row = int(input(f'\nInsert row. Integer from 1 to {args.rows}: '))
            start_col = int(input(f'\nInsert column. Integer from 1 to {args.columns}: '))
            if not Utils.check_start_point(args, start_row, start_col):
                print('\nError! The given starting point is not valid. Try again')
                continue

            orientation = input('\nInsert orientation. Must be horizontal or vertical: ')
            if not Utils.check_orientation(orientation):
                print(
                    '\nError! The given orientation is not valid. Try again making sure you spell correctly your choice')
                continue

            if orientation == 'horizontal':
                error, coordinates = check_horizontal_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            else:
                error, coordinates = check_vertical_ship_positioning(args, board, start_row, start_col, i)
                if not error:
                    successful_insertion = True
            print_board(board, args)

        if i == 5:
            ship = ship_types.Carrier(i, orientation, start_row, start_col, coordinates)
        elif i == 4:
            ship = ship_types.Battleship(i, orientation, start_row, start_col, coordinates)
        elif i == 3:
            ship = ship_types.Submarine(i, orientation, start_row, start_col, coordinates)
        elif i == 2:
            ship = ship_types.Destroyer(i, orientation, start_row, start_col, coordinates)
        ship_list.append(ship)
    return board, ship_list

def print_board(game_board, args):
    print("\n  " + " ".join(str(x) for x in range(1, args.columns + 1)))
    for r in range(args.rows):
        print(str(r + 1) + " " + " ".join(str(c) for c in game_board[r]))
    print()


def check_horizontal_ship_positioning(args, board, start_row, start_col, size):
    error = False
    if start_col + size - 1 <= args.columns:
        i = start_col - 1
        while i < start_col + size -1 and not error:
            if board[start_row - 1][i] == 1:
                warnings.warn("\nError! There is already another ship here")
                error = True
            if start_row == 1:
                if board[start_row][i] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_row == args.rows:
                if board[start_row - 2][i] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_row > 1 and start_row < args.rows:
                if board[start_row][i] == 1 or board[start_row - 2][i] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_col != 1:
                if board[start_row - 1][start_col - 2] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_col + size - 2 != args.columns - 1:
                if board[start_row - 1][start_col + size - 1] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_col - 1, start_col + size - 1):
                board[start_row - 1][i] = 1
                coordinates.append([start_row, i+1])
    else:
        warnings.warn("\nError! Ship is out of board")
    return error, coordinates


def check_vertical_ship_positioning(args, board, start_row, start_col, size):
    error = False
    if start_row + size - 1 <= args.rows:
        i = start_row - 1
        while i < start_row + size -1 and not error:
            if board[i][start_col - 1] == 1:
                warnings.warn("\nError! There is already another ship here")
                error = True
            if start_col == 1:
                if board[i][start_col] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_col == args.columns:
                if board[i][start_col - 2] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_col > 1 and start_col < args.columns:
                if board[i][start_col] == 1 or board[i][start_col - 2] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_row != 1:
                if board[start_row - 2][start_col - 1] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            if start_row + size - 2 != args.rows - 1:
                if board[start_row + size - 1][start_col - 1] == 1:
                    warnings.warn("\nError! You are adjacent to another ship")
                    error = True
            i = i + 1
        if not error:
            coordinates = []
            for i in range(start_row - 1, start_row + size - 1):
                board[i][start_col - 1] = 1
                coordinates.append([i+1, start_col])
    else:
        warnings.warn("\nError! Ship is out of board")
    return error, coordinates