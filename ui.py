import pygame
pygame.init()
font = pygame.font.SysFont('Comic Sans MS', 40)
blank = pygame.font.SysFont('Comic Sans MS', 70)
screen = pygame.display.set_mode(size=(720,720))

if __name__ == "__main__":
    #screen = pygame.display.set_mode(size=(720,720))
    pygame.display.set_caption("Sudoku")

    blockSize = 80
    def drawGrid():
        global blockSize #Set the size of the grid block
        for y in range(9):
            for x in range(9):

                #conditions for red and black boxes for alternate 3x3 gr
                if (((x>=0 and x<=2) and (y>=0 and y<=2)) or ((x>=6 and x<=8) and (y>=0 and y<=2)) or((x>=3 and x<=5) and(y>=3 and y<=5))
                        or ((x>=0 and x<=2) and (y>=6 and y<=8)) or ((x>=6 and x<=8) and (y>=6 and y<=8))):

                    rect = pygame.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
                    pygame.draw.rect(screen, (250, 0, 0), rect, 2)
                else:
                    rect = pygame.Rect(x*blockSize, y*blockSize,blockSize, blockSize)
                    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    screen.fill((250,250,250)) #rgb code for white
    drawGrid()

    grid = [[0 for x in range(9)] for y in range(9)]
    running = True
    from solveit import *

    while running:
        num = 0
        for event in pygame.event.get():
            key = True
            click = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                positionx = position[0]//blockSize
                positiony = position[1]//blockSize
                if position[1] % 80 == 0:
                    positiony -= 1
                if position[0] % 80 == 0:
                    positionx -= 1

            #Checks for keypress and adds the text to the screen
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    num = 1
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))  #font.render(text, alias, text_colour, foreground_colour)
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_2:
                    num = 2
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_3:
                    num = 3
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_4:
                    num = 4
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_5:
                    num = 5
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_6:
                    num = 6
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_7:
                    num = 7
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_8:
                    num = 8
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_9:
                    num = 9
                    grid[positiony][positionx] = num
                    fontsurf = font.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(fontsurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_BACKSPACE:
                    num = " "
                    grid[positiony][positionx] = num
                    blanksurf = blank.render(str(num), False, (0, 0, 0), (250, 250, 250))
                    screen.blit(blanksurf, (20+positionx*80,20+positiony*80))

                if event.key == pygame.K_SPACE:
                    solution(grid)

            if event.type == pygame.QUIT:
                running = False
        pygame.display.update()




