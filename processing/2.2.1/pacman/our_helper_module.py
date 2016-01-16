def draw_game_field(cell_size, game_field, img0, img1, img2, img3):
    """ maliye ihrove pole (game_field) na ekran """                                                                              
    for i in range(len(game_field)):                                                                              
            for j in range (len(game_field[0])):                                                                     
                x = cell_size * j
                y = cell_size * i
                if game_field[i][j] == 0:                                                                
                    image(img0, x, y, cell_size, cell_size)                                                                     
                elif game_field[i][j] == 1:
                    image(img1, x, y, cell_size, cell_size)
                elif game_field[i][j] == 2:
                    image(img2, x, y, cell_size, cell_size)
                elif game_field[i][j] == 3:
                    image(img3, x, y, cell_size, cell_size)

def initialize_game_field_size(game_field, cell_size):
    """ zadaie rozmir ihrovoho ekrany z zadanum rozmirom klitunku (cell_size) """   
    size(len(game_field) * cell_size, len(game_field[0]) * cell_size)
    
def generate_game_field(field_of_the_game, field_width, field_height):
    """ mu tse robulu na pari """
    for i in range(field_width):
        for j in range(field_height):
            rnd = int(random(0, 5))
            if rnd == 0:
                field_of_the_game[i][j] = 1
            else:
                field_of_the_game[i][j] = 0
    
