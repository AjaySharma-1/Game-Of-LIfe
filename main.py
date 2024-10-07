import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the display
N= 50
WIDTH, HEIGHT = 800, 800
ROW, COLUMN = N,N
cell_size = WIDTH//COLUMN

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN= (0,255,0)
BLUE= (0,0,255)
clock = pygame.time.Clock()
font= pygame.font.SysFont(None, cell_size)
FPS= 60
grid= [[random.choice(['O',' ']) for _ in range(COLUMN)] for _ in range(ROW)]
def make_grid():
    for row in range(ROW):
        for col in range(COLUMN):
            rect = pygame.Rect(row*cell_size, col*cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, BLACK,rect,1)
            value = grid[row][col]
            text= font.render(value,True,GREEN)
            text_rect= text.get_rect(center=rect.center)
            screen.blit(text,text_rect)
            
            
def lifes(row, col):
    # values = [grid[row-1][col-1],grid[row-1][col],grid[row-1][col+1],
    #           grid[row ][col-1 ],                 grid[row][col+1  ],
    #           grid[row+1][col-1],grid[row+1][col],grid[row+1][col+1] ] 
    directions= [[-1,-1], [-1,0], [-1,1],
                [0,-1],           [0,1],
                [1,-1], [1,0],   [1,1]]
    live_count = 0
    for direction in directions :
        r = direction[0] + row
        c = direction[1] + col

        if 0<=r< ROW and 0 <=c<COLUMN:
            if grid[r][c] == "O":
                live_count+=1
                
    return live_count
    



def game_of_life():
    new_grid = [row[:] for row in grid]
    for row in range(0,ROW):
        for col in range(0,COLUMN):
            no_of_life= lifes( row, col)
            if grid[row][col]== "O"  :  
                if no_of_life < 2 or no_of_life>3:
                    new_grid[row][col] = " "  # dies  
                    
            else:
                if no_of_life == 3:
                    new_grid[row][col] = "O"
            
    return new_grid
               
            

# Main game loop
count = 0
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update

    # Draw
    screen.fill(BLACK)

    # Rendering
    make_grid()
    if count>50:
        grid=game_of_life()
        count = 0
   
    count +=1
   
    pygame.display.flip()
clock.tick(FPS)
# Quit Pygame
pygame.quit()
sys.exit()
