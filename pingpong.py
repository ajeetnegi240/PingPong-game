import pygame,sys
from pygame.locals import *


pygame.init()


screen_width=600
screen_height=500

clock=pygame.time.Clock()



screen=pygame.display.set_mode((screen_width,screen_height),pygame.RESIZABLE)
pygame.display.set_caption('PingPong')

bgcolor=(50,25,50)
white=(255,255,255)


#defining font
font=pygame.font.SysFont('Constantia',30)

#game variables
cpu_score=0
player_score=0
margin=50
fps=60


def draw_board(bgcolor,screen_width,margin):
    screen.fill(bgcolor)
    pygame.draw.line(screen,white,(0,margin),(screen_width,margin))
    
    
def draw_text(text,font,text_col,x,y):
    image=font.render(text,True,text_col)
    screen.blit(image,(x,y))
    
    
 
 
class paddle():
     def __init__(self,x,y):
         self.x=x
         self.y=y
         self.rect=Rect(self.x,self.y,20,100)
         self.speed=5
         
     def move(self):
         key=pygame.key.get_pressed()
         if key[pygame.K_UP] and self.rect.top >margin:
             self.rect.move_ip(0,-1*self.speed)
         if key[pygame.K_DOWN] and self.rect.bottom<screen_height:
             self.rect.move_ip(0,self.speed)
             
     
     def draw(self):
         pygame.draw.rect(screen,white,self.rect)
         
         
         
class ball:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.ball_radius=10
        self.rect=Rect(self.x,self.y,self.ball_radius *2,self.ball_radius*2)
        self.speed_x=-4
        self.speed_y=4
        
    def move(self):
        #detecting collision
        #checking collision with top margin 
        if self.rect.top<margin:
            self.speed_y*=-1
        if self.rect.bottom>screen_height:
            self.speed_y*=-1
            
         self.rect.x+=self.speed_x
         self.rect.y+=self.speed_y
        
    def draw(self):
         pygame.draw.circle(screen,white,(self.rect.x+self.ball_radius,self.rect.y+self.ball_radius),self.ball_radius)
         
#create paddle
player_paddle =paddle(screen_width-40,screen_height//2)         
cpu_paddle=paddle(20,screen_height//2)   

pong=ball(screen_width-60,screen_height//2+50)      

 
    
   

while True:
    clock.tick(60)
    
    draw_board(bgcolor,screen_width,margin)
    draw_text('CPU:'+str(cpu_score),font,white,20,15)
    draw_text('Player:'+str(player_score),font,white,screen_width-100,15)
    
    
    #drawing paddles
    player_paddle.draw()
    cpu_paddle.draw()
    
    #drawing pong
    pong.draw()
    
    player_paddle.move()
    
    pong.move()
    
    
    
    
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update()


            

 