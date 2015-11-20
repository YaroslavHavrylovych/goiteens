WIDTH = 50
HEIGHT = 30
CELL_SIZE = 20                                       
game_field = [[0]*HEIGHT for _ in range(WIDTH)]
CHECKED_CELLS = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
seconds = second()
                                                                                                    
def setup():                                                                                        
    size(len(game_field) * CELL_SIZE, len(game_field[0]) * CELL_SIZE)

def draw():
    global seconds
    draw_game_field(CELL_SIZE, game_field)
    if seconds != second():
        step(game_field)
        seconds = second()
                            
def draw_game_field(CELL_SIZE, game_field):                                                                              
    for i in range(len(game_field)):                                                                              
            for j in range (len(game_field[0])):                                                                     
                if game_field[i][j] == 0:                                                                
                    fill(255)                                                                         
                else:                                                                               
                    fill(0)                                                                       
                rect(CELL_SIZE*i, CELL_SIZE*j, CELL_SIZE, CELL_SIZE)

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
                if in_bounds(0, n-1, i1) and in_bounds(0, m-1, j1):
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

def mousePressed(): 
    global game_field
    i = mouseX / CELL_SIZE
    j = mouseY / CELL_SIZE
    if i > WIDTH - 1 or j > HEIGHT - 1 or i < 0 or j < 0:
        return
    game_field[i][j] = 1
    
def mouseDragged():
    mousePressed()  
