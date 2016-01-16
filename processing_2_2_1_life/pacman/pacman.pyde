import our_helper_module

#==============================
#======= GAME FIELD ===========
#==============================
CELL_SIZE = 20
GAME_FIELD_WIDTH = 20
GAME_FIELD_HEIGHT = 20
game_field = [[0]*GAME_FIELD_HEIGHT for _ in range(GAME_FIELD_WIDTH)]

#==============================
#=======   PACMAN   ===========
#==============================
pacman_i = 0
pacman_j = 0

#==============================
#=======   ENEMY1   ===========
#=============================

enemy1_i = 0
enemy1_j = GAME_FIELD_HEIGHT - 1
enemy1_direction = UP
enemy1_live = True

#==============================
#=======   IMAGES   ===========
#==============================
passage_image = PImage()
wall_image = PImage()
enemy_image = PImage()
pacman_image = PImage()

#==============================
#=======   OTHER    ===========
#==============================
keyboard_key_that_was_pressed = 0 #if not pressed then contains 0 else contains one of DIRECOTOR (e.g. UP, DOWN, RIGHT or LEFT)
win = False #you will win after kill all enemies

## !!! ##
enemies_amount = 1 #kilkist vorohiv na karti

#==============================
#====== DIECTION LIST =========
#==============================
DIRECOTOR = [UP, DOWN, RIGHT, LEFT]

######################################
####### PROCESSING FUNCTIONS #########
######################################

#Vuklukaetsia odun raz na samomy pochatky, pered vuklukom draw()
def setup():
    """ Tyt mu vstanovliuemo pochatkovi dani (maliynku, heneruamo ihrove pole i t.p.) """
    frameRate(3)
    # load images
    global wall_image, passage_image, enemy_image, pacman_image
    enemy_image = loadImage("enemy.png")
    pacman_image = loadImage("pacman.png")
    wall_image = loadImage("wall.png")
    passage_image = loadImage("passage.png")
    
    global game_field
    our_helper_module.initialize_game_field_size(game_field, CELL_SIZE)
    our_helper_module.generate_game_field(game_field, GAME_FIELD_WIDTH, GAME_FIELD_HEIGHT)
    
    create_pacman()
    
    create_enemy1()
    
def draw():
    global win
    if win:
        our_helper_module.draw_game_field(CELL_SIZE, game_field, passage_image, wall_image, pacman_image, enemy_image)
        text("you win", 100, 100)
        return
    
    move_pacman_if_key_was_pressed()
    
    if check_win(): #perevirks chu mu ne vuhralu
        win = True
        return #end this function
    
    move_enemy1()
            
    if check_win(): #perevirks chu mu ne vuhralu
        win = True
        return #end this function
    
    our_helper_module.draw_game_field(CELL_SIZE, game_field, passage_image, wall_image, pacman_image, enemy_image)
    
    
    
###################################
########## OUR FUNCTIONS ##########
###################################
    
def check_win():
    global enemy1_i, enemy1_j, game_field, enemy1_live, enemies_amount
    if enemy1_i == pacman_i and enemy1_j == pacman_j:
        enemy1_i = 0
        enemy1_j = 0
        game_field[pacman_i][pacman_j] = 2 #pacman will kill enemy
        enemy1_live = False
        enemies_amount = enemies_amount - 1
    
    ## Tut pusatu vsih inshuh vorohiv
    
    return enemies_amount == 0 

def create_pacman():
    global pacman_i, pacman_j, game_field
    is_set = False
    while not is_set: #loop will work until is_set == False
        rand = int(random(GAME_FIELD_WIDTH))
        if game_field[rand][0] == 0: #if passage
            game_field[rand][0] = 2 #set pacman
            is_set = True 
            pacman_i = rand
            
def create_enemy1():
    global enemy1_i, enemy1_j, game_field
    is_set = False
    while not is_set: #loop will work until is_set == False
        rand = int(random(GAME_FIELD_WIDTH))
        if game_field[rand][GAME_FIELD_HEIGHT - 1] == 0: #if passage
            game_field[rand][GAME_FIELD_HEIGHT - 1] = 3 #set enemy
            is_set = True 
            enemy1_i = rand
        
def keyPressed():
    if win != 0:
        return
    global keyboard_key_that_was_pressed
    keyboard_key_that_was_pressed = keyCode
    
def move_pacman_if_key_was_pressed():
    N = GAME_FIELD_WIDTH
    M = GAME_FIELD_HEIGHT
    global game_field, pacman_i, pacman_j, keyboard_key_that_was_pressed
    if keyboard_key_that_was_pressed != 0:
        i = pacman_i
        j = pacman_j
        if keyboard_key_that_was_pressed == RIGHT:
            j = (j + 1) if j < M-1 else 0
        elif keyboard_key_that_was_pressed == LEFT:
            j = (j - 1) if j > 0 else M-1
        elif keyboard_key_that_was_pressed == UP:
            i = (i - 1) if i > 0 else N-1
        elif keyboard_key_that_was_pressed == DOWN:
            i = (i + 1) if i < N-1 else 0
        if game_field[i][j] == 1:
            i = pacman_i
            j = pacman_j
        
        #y poperedniu pozuciy pacman stavumo 0 (passage) y novy pushumo 3 (pacman)    
        game_field[pacman_i][pacman_j] = 0 #sprobuite zakomentuvatu i hlianytu scho byde 
        pacman_i = i
        pacman_j = j
        
        game_field[pacman_i][pacman_j] = 2
        keyboard_key_that_was_pressed = 0
        
def move_enemy1():
    if enemy1_live == False: #if our enemy - dead
        return
    
    N = GAME_FIELD_WIDTH
    M = GAME_FIELD_HEIGHT
    global game_field, enemy1_i, enemy1_j, enemy1_direction
    i = enemy1_i
    j = enemy1_j
    if enemy1_direction == RIGHT:
        if j < M - 1:
            j = j + 1
        else:
            j = M - 1
    elif enemy1_direction == LEFT:
        if j > 0:
            j = j - 1
        else:
            j = 0
    elif enemy1_direction == UP:
        if i > 0:
            i = j - 1
        else:
            i = 0
    elif enemy1_direction == DOWN:
        if i < N - 1:
            i = i + 1
        else:
            i = N - 1
    if game_field[i][j] == 1:
        i = enemy1_i
        j = enemy1_j
    if i == enemy1_i and j == enemy1_j:
        rnd = int(random(4))
        enemy1_direction = DIRECOTOR[rnd]    
    #y poperedniu pozuciy voroga stavumo 0 (passage) y novy pushumo 3 (pacman)    
    game_field[enemy1_i][enemy1_j] = 0
    enemy1_i = i
    enemy1_j = j
    game_field[enemy1_i][enemy1_j] = 3
