CELL_SIZE = 20                                       
game_field =      [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
CHECKED_CELLS = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
                                                                                                    
def setup():
    frameRate(4)                                                                                        
    size(len(game_field[0]) * CELL_SIZE, len(game_field) * CELL_SIZE)

def draw():
    draw_game_field(CELL_SIZE, game_field)
    step(game_field)
                            
def draw_game_field(CELL_SIZE, game_field):                                                                              
    for i in range(len(game_field)):                                                                              
            for j in range (len(game_field[0])):                                                                     
                if game_field[i][j] == 0:                                                                
                    fill(255)                                                                         
                else:                                                                               
                    fill(0)                                                                       
                rect(CELL_SIZE*j, CELL_SIZE*i, CELL_SIZE, CELL_SIZE)

def step(local_game_field):
    tmp_list = [[0]*len(local_game_field[0]) for _ in range(len(local_game_field))]
    n = len(local_game_field)
    m = len(local_game_field[0])
    #fill a list (each cell contains of neighbours)
    for i in range(n):
        for j in range(m):
            for pair in CHECKED_CELLS:
                i1 = i + pair[0]
                j1 = j + pair[1]
                if not (in_bounds(0, n-1, i1) and in_bounds(0, m-1, j1)):
                    if i1 < 0:
                        i1 = i1 + n
                    else:
                        i1 = i1 - n
                    if j1 < 0:
                        j1 = j1 + m
                    else:
                        j1 = j1 - m
                tmp_list[i][j] += local_game_field[i1][j1]
    
    #game rules
    for i in range(n):
        for j in range(m):
            val = tmp_list[i][j]
            if  val < 2 or val > 3:
                tmp_list[i][j] = 0
            elif val == 2:
                if local_game_field[i][j] == 1:
                    tmp_list[i][j] = 1
                else:
                    tmp_list[i][j] = 0
            elif val == 3:
                tmp_list[i][j] = 1
    #copy from tmp list to our game array
    for i in range(n):
        for j in range(m):
            local_game_field[i][j] = tmp_list[i][j]

def in_bounds(v_min, v_max, val):
    return v_min <= val <= v_max
