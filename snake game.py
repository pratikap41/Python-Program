import pygame
import random
import time
from tkinter import *
highscorel = []

def quitgame():
    pygame.quit()

def quitbut():
    quit()

def Hightscore( ):
    print(highscore)
  
    

def start_window ():
    start_window = Tk()
    start_window.title("SNAKE GAME")
    start_window.geometry('300x300+500+200')
    start_window.configure(bg='light steelblue2')
    l1 = Label(start_window, text= "*SNAKE GAME*", bd=5, relief=SUNKEN, font = ('arial', 30, 'bold') ,  bg ='light steelblue2' ,fg = 'goldenrod1')
    l1.pack(ipady = 10)
    l2 = Label(start_window, text= "MENU", bg = 'lightsteelblue2', font = ('arial', 10, 'bold'), fg ='black')
    l2.pack(ipady = 25)
    play_but = Button(start_window, text= 'Play', command= game, bd=5, relief=RAISED, bg='green', font = ('arial ', 10, 'bold'), fg ='white', width=25)
    play_but.pack()
    hs_but = Button(start_window, text= 'High Score', bd=5, relief=RAISED, bg='lightpink1', font = ('arial ', 10, 'bold'), fg ='white', width=25, command = Hightscore)
    hs_but.pack()
    quit_but = Button(start_window, text= 'Quit', bd=5, relief=RAISED, bg='red', font = ('arial ', 10, 'bold'), fg ='white', width=25, command = quitbut)
    quit_but.pack()


#++++++++++++++++++++++++++++VARIABLES++++++++++++++++++++++++++++++++++++
display_width = 800
display_height = 600

######Colour######################################
red = [255, 0, 0]
white = [255, 255, 255]
black = [0, 0, 0]
blue = [0, 0, 255]
green = [0, 255, 0]
sapphire = [15, 82, 186]
orange = [252, 102, 0]

snakelist = []
def snake(char_size, snakelist):
    for snakelist_element in snakelist:
        pygame.draw.rect(gdisplay, green , [snakelist_element[0], snakelist_element[1], char_size, char_size ])
        



def message_to_screen(msg, colour):

    screen_text = font.render(msg, True, colour)
    gdisplay.blit(screen_text, [200, 300])
    
    
    

    
def game():
#++++++++++++++++++++++++++++CHANGING  ___VARIABLES++++++++++++++++++++++++++++++++++++
    pygame.init()
    font = pygame.font.SysFont(None, 25)
    global gdisplay
    gdisplay = pygame.display.set_mode((display_width,    display_height))
    pygame.display.set_caption("SNAKE GAME")
    run = True
    gameover = False
    clock = pygame.time.Clock()
    fps = 13
    char_size = 10
    x = random.randrange(0, display_width, char_size)
    y = random.randrange(0, display_height, char_size)
    applex = random.randrange(0, display_width-30, 10)
    appley = random.randrange(0, display_height-30, 10)
    x_change = 0
    y_change = 0
    snakelength=1


    
 
    globals().update(locals())  
    
    
   
##game-------------------------------------------------------------------- loope

            
        
    
    while (run == True):
        while gameover == True :
           
            
            
            gdisplay.fill(black)
            snakelist.clear()
            message_to_screen(' GAME OVER, To play again press R, To quit press Q', red)
            pygame.display.update()
            
            for event in pygame.event.get():
                if  event.type == pygame.QUIT :
                        
                        gameover = False
                        run = False
                        quitgame()
                     
                        
                if event.type == pygame.KEYDOWN :
                    if event.key == pygame.K_r:
                        game()
                    if event.key == pygame.K_q:
                        gameover = False
                        run = False
                        quitgame()
                        
        
        
        for event in pygame.event.get():
            if  (event.type == pygame.QUIT ):
                run = False
                quitgame()
                
                
                
            elif (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_RIGHT ):
                    x_change = 10
                    y_change = 0
                if (event.key == pygame.K_LEFT ):
                    x_change  = -10
                    y_change = 0
                if (event.key == pygame.K_UP ):
                    y_change = -10
                    x_change = 0
                if (event.key == pygame.K_DOWN ):
                    y_change = 10
                    x_change = 0
        if (x > display_width-10 or x < 0 or y > display_height-10 or y < 0) :
                gameover = True
                
                
               
            
                

        x  =  x + x_change
        y  = y + y_change
        
        gdisplay.fill(black )
        
        snakehead = []
        snakehead.append(x )
        snakehead.append(y )
        snakelist.append(snakehead)
        
        pygame.draw.rect(gdisplay, red, [applex, appley, char_size, char_size])
        
        if len(snakelist )> snakelength:
            del snakelist[0] 

        for segment in snakelist[:-1]:
            if segment == snakehead:
                gameover = True

                
        snake(char_size, snakelist)

        if x == applex and y == appley:
            applex = random.randrange(0, display_width-30, 10)
            appley = random.randrange(0, display_height-30, 10)
            snakelength += 1
            
     
        clock.tick(fps)
        pygame.display.update()
    






start_window()






