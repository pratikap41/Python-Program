import pygame
from tkinter import  messagebox

pygame.init()
gamewindow = pygame.display.set_mode((800, 600))
pygame.display.set_caption("SNAKE")







##GAMELOOP

def gameloop():
    run = True
    red = (255, 0, 0)
    black = (0, 0, 0)
    clock = pygame.time.Clock()
    lead_x = 100
    lead_y = 100
    lead_x_change = 0
    lead_y_change = 0
    font = pygame.font.SysFont(None, 25)
    fps = 160000
    gameover = False

    
    while  run == True :
        while gameover == True :
            font.render
        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                run = False
            elif event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_RIGHT:
                        lead_y_change = 0
                        lead_x_change  = 1
                    elif event.key == pygame.K_LEFT:
                        lead_y_change = 0
                        lead_x_change  = -1
                    elif event.key == pygame.K_UP:
                        lead_x_change = 0
                        lead_y_change  = -1
                    elif event.key == pygame.K_DOWN:
                        lead_x_change = 0
                        lead_y_change  = 1
        lead_x += lead_x_change
        lead_y += lead_y_change

        if lead_x >= 800 or lead_x <= 0 or lead_y >= 600 or lead_y <= 0 :
            msg = messagebox.showinfo("GAME OVER", "GAME OVER")
            if msg == 'ok':
                pygame.quit()
                quit()
             
            

        
        gamewindow.fill(black)
        pygame.draw.rect(gamewindow, red, [lead_x, lead_y, 10, 10] )
        clock.tick(fps )
        pygame.display.update()

        
gameloop()
pygame.quit()
quit()
