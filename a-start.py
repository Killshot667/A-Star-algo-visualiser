import pygame
import math
from queue import PriorityQueue

WIDTH = 800;
WIN = pygame.display.set_mode((WIDTH, WIDTH))

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165 ,0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)

class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
    
    def get_pos(self):
        return self.row, self.col
    
    def is_closed(self):
        return self.color == RED
    
    def is_open(self):
        return self.color == GREEN
    
    def is_barrier(self):
        return self.color == BLACK
    
    def is_start(self):
        return self.color == ORANGE
    
    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE
    
    def make_closed(self):
        self.color = RED 

    def make_open(self):
        self.color = GREEN
    
    def make_barrier(self):
        self.color = BLACK

    def make_start(self):
        self.color = ORANGE
    
    def make_end(self):
        self.color = TURQUOISE
    
    def make_path(self):
        self.color = PURPLE
    
    def draw(self,win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self):
        pass

    def __lt__(self,other):
        return False
    
def h(a, b):
    x1, y1 = a
    x2, y2 = b
    return abs(x1-x2) + abs(y1-y2)

def make_grid(rows, span):
    gap = span // rows
    grid = []

    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid

def draw_grid(win, rows, span):
    gap = span // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (span, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, span))

def draw(win, grid, rows, span):
    win.fill(WHITE)
    for row in grid:
        for spot in row:
            spot.draw(win)
    
    draw_grid(win, rows, span)
    pygame.display.update()

def get_clicked(pos, rows, span):
    gap = span // rows
    y, x = pos
    row = y // gap
    col = x // gap
    return row, col

def main(win, span):
    ROWS = 50
    make_grid(ROWS, span)

    start = None
    end = None
    run = True
    started = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.quit(): # have to try pygame.cdrom.quit()
                run = False
            
            if started:
                continue
            
            if pygame.mouse.get_pressed()[0]:
                
            
            elif pygame.mouse.get_pressed()[2]:



    
    

    




