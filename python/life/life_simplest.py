import time

game_first_list = [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
game_second_list = [[0]*len(game_first_list[0]) for _ in range(len(game_first_list))]
checker_sequence_list = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]

def fill_zero(two_dimen_list):
    for row in two_dimen_list:
        for i in range(len(row)):
            row[i] = 0

def bounds(v_min, v_max, val):
    return v_min <= val <= v_max

def step(current_state_list, next_state_list):
    fill_zero(next_state_list)
    n = len(current_state_list)
    m = len(current_state_list[0])
    for i in range(n):
        for j in range(m):
            for pair in checker_sequence_list:
                i1 = i + pair[0]
                j1 = j + pair[1]
                if bounds(0, n-1, i1) and bounds(0, m-1, j1):
                    next_state_list[i][j] += current_state_list[i1][j1]

    for i in range(n):
        for j in range(m):
            val = next_state_list[i][j]
            if  val < 2 or val > 3:
                next_state_list[i][j] = 0
            elif val == 2:
                if current_state_list[i][j] == 1:
                    next_state_list[i][j] = 1
                else:
                    next_state_list[i][j] = 0
            elif val == 3:
                next_state_list[i][j] = 1

def print_list(to_print):
    """ prints the list """
    for row in to_print:
        print(str(row))
    print()


def life_cycle():
    """ game lifecycle """
    current_state_list = game_first_list
    next_state_list = game_second_list
    while True:
        print_list(current_state_list)
        time.sleep(1)
        step(current_state_list, next_state_list)
        if current_state_list == game_first_list:
            current_state_list = game_second_list
            next_state_list = game_first_list
        else:
            current_state_list = game_first_list
            next_state_list = game_second_list

if __name__ == "__main__":
    life_cycle()
