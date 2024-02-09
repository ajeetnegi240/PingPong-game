import pygame,sys,playsound
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
live_ball=False
cpu_score=0
player_score=0
margin=50
fps=60
winner=0
speed_increase=0
x=1


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
             
             
     def ai(self):
         if self.rect.centery < pong.rect.top and self.rect.bottom <screen_height:
             self.rect.move_ip(0,self.speed)
         if self.rect.centery > pong.rect.bottom  and self.rect.top >margin:
             self.rect.move_ip(0,-1*self.speed)
     
     def draw(self):
         pygame.draw.rect(screen,white,self.rect)
         
         
         
class ball:
    def __init__(self,x,y):
        self.reset(x,y)
        
    def move(self):
        
        #detecting collision
        #checking collision with top margin 
        if self.rect.top<margin:
            self.speed_y*=-1
        #checking collision with bottom of the screen 
        if self.rect.bottom>screen_height:
            self.speed_y*=-1
            
        #checking collision with paddles
        if self.rect.colliderect(player_paddle): 
            self.speed_x*=-1
            # playsound.playsound('ballsound.mp3.wav')
            
        if self.rect.colliderect(cpu_paddle):
            self.speed_x*=-1
            # playsound.playsound('ballsound.mp3.wav')
            global player_score
            player_score+=1
            
        #checking for out bounds:
        if self.rect.left <0:
            self.winner=1
        if self.rect.right >screen_width:
            self.winner=-1
            
     
            
        self.rect.x+=self.speed_x
        self.rect.y+=self.speed_y
        
        return self.winner
        
    def draw(self):
         pygame.draw.circle(screen,white,(self.rect.x+self.ball_radius,self.rect.y+self.ball_radius),self.ball_radius)
     
    def reset(self,x,y):
        self.x=x
        self.y=y
        self.ball_radius=10
        self.rect=Rect(self.x,self.y,self.ball_radius *2,self.ball_radius*2)
        self.speed_x=-4
        self.speed_y=4
        self.winner=0
     
     
color=(60, 0, 0)     
         
#create paddle
player_paddle =paddle(screen_width-40,screen_height//2)         
cpu_paddle=paddle(20,screen_height//2)   

pong=ball(screen_width-60,screen_height//2+50)      

 
    
   
def gameloop():
    global live_ball
    global cpu_score
    global player_score
    global margin
    global fps
    global winner
    global speed_increase
    global color
    
    pygame.display.update()
    while True:
        
        draw_board(bgcolor,screen_width,margin)
        # draw_text('CPU:'+str(cpu_score),font,white,20,15)
        #instructions for player-
        if player_score==0:
            draw_text('CLICK ANYWHERE TO START ',font,(23,234,125),100,screen_height//2-50)
        draw_text('Player:'+str(player_score),font,white,screen_width-100,15)
        
        
        #drawing paddles
        player_paddle.draw()
        cpu_paddle.draw()
        
        
        if live_ball==True:
            speed_increase+=0.5
            winner=pong.move()
            if winner==0:
                player_paddle.move()
                cpu_paddle.ai()
                #drawing pong
                pong.draw()
            else:
                live_ball=False
                draw_board(color,screen_width,margin)
                draw_text('Your score:'+str(player_score),font,white,200,200)
                draw_text('To Restart The Game  ',font,white,100,270)
                draw_text(' press any key of mouse',font,white,100,300)
                player_score=0
                    
                    
                for ev in pygame.event.get():
                    if ev.type==QUIT:
                            pygame.quit()
                            sys.exit()
                    if ev.type==pygame.KEYDOWN:
                        if event.key==pygame.K_RETURN:
                            gameloop()
                pygame.display.update()
               
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and live_ball==False:
                live_ball=True
                player_score=0
                pong.reset(screen_width-60,screen_height//2+50)
                
            
                    
        pygame.display.update()
        clock.tick(60)
      
        


gameloop()
            

 