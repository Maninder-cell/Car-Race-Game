'''.............'''

#game creater=Maninder Singh
#game animations and models create in inkscape.
#music company=Kings Media

import pygame
import random
import time

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()

##colours______
white=(255,255,255)
black=(0,0,0)
green=(127,255,42)
gray=(108,83,83)

#display_____________-----
screen_width=600
screen_height=650
display=pygame.display.set_mode((screen_width,screen_height))

#name and icon=======================

pygame.display.set_caption('Overdose Racing')

##images______________----------------++++++++++

#button images------------------------------------------
quit_image=pygame.image.load('cargame/image/quit.png')
running_image=pygame.image.load('cargame/image/running.png')
pause_image=pygame.image.load('cargame/image/pause.png')
pause_image1=pygame.image.load('cargame/image/pause_image.png')
reset_image=pygame.image.load('cargame/image/reset.png')

#blast images-----------------------------------
blast_image=[pygame.image.load('cargame/image/blast/1.png'),
        pygame.image.load('cargame/image/blast/2.png'),
        pygame.image.load('cargame/image/blast/3.png'),
        pygame.image.load('cargame/image/blast/4.png'),
        pygame.image.load('cargame/image/blast/5.png'),
        pygame.image.load('cargame/image/blast/6.png'),
        pygame.image.load('cargame/image/blast/7.png'),
        pygame.image.load('cargame/image/blast/8.png'),
        pygame.image.load('cargame/image/blast/9.png'),
        pygame.image.load('cargame/image/blast/10.png')]

#layout images------------------------------------------------
menu_picture=pygame.image.load('cargame/image/menu_picture.png')
start_picture=pygame.image.load('cargame/image/start.png')
control_picture=pygame.image.load('cargame/image/control.png')
about_picture=pygame.image.load('cargame/image/about.png')
back_picture=pygame.image.load('cargame/image/back.png')
control_image=pygame.image.load('cargame/image/control_image.png')
about_image=pygame.image.load('cargame/image/about_image.png')

#characters images--------------------------------------------
road1=pygame.image.load('cargame/image/road.png')
road2=pygame.image.load('cargame/image/road.png')
zebra=pygame.image.load('cargame/image/zebra.png')
clip=pygame.image.load('cargame/image/clip.png')
cars=[pygame.image.load('cargame/image/car2.png'),
      pygame.image.load('cargame/image/car3.png'),
      pygame.image.load('cargame/image/truck.png')]
car1=pygame.image.load('cargame/image/car1.png')
clip_set=pygame.image.load('cargame/image/clip.png')

#mask and rotation and other stuff--------------------------------------------
clip2=pygame.transform.rotate(clip_set,180)
car1_mask=pygame.mask.from_surface(car1)
obstacle_list=[pygame.mask.from_surface(cars[0]),
              pygame.mask.from_surface(cars[1]),
              pygame.mask.from_surface(cars[2])]
car1_copy=car1
center=car1.get_rect().center

#main car class___
class main_car:
    def __init__(self,y,change_y,x,move_car,change_x):
        self.y=y
        self.x=x
        self.change_y=0
        self.move_car=move_car
        self.change_x=change_x
    def draw_car(self):
        display.blit(car1,(self.x,self.y))

class other_car:
    def __init__(self,x,y,position):
        self.x=x
        self.y=y
        self.position=position
    def draw_car(self):
        display.blit(cars[self.position],(self.x,self.y))

class class_zebra:
    def __init__(self,zebra_y,check_zebra):
        self.zebra_y=zebra_y
        self.check_zebra=check_zebra
    def draw_zebra(self):
        display.blit(zebra,(147,self.zebra_y))

def rotate_image(rotate):
    car1=pygame.transform.rotate(car1_copy,rotate)
    car1.get_rect().center=center
    car1_mask=pygame.mask.from_surface(car1)
    return car1,car1_mask

def play_music(location,repeat):
    pygame.mixer.music.load(f'{location}')
    pygame.mixer.music.play(repeat)
    
def stop_music():
    pygame.mixer.music.stop()

def pause_music():
    pygame.mixer.music.pause()

def unpause_music():
    pygame.mixer.music.unpause()

channel1=pygame.mixer.Channel(0)
channel2=pygame.mixer.Channel(1)
channel3=pygame.mixer.Channel(2)
channel4=pygame.mixer.Channel(3)
channel4.set_volume(0.09)


control=False
menu=True
about=False
game=True
pause=False
reset=False
start=True

def menu_start():
    global menu
    global control
    global about
    global game
    x=5
    x1=5
    x2=5
    channel1.play(pygame.mixer.Sound('cargame/music/menu_music.wav'),-1)
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                menu=False       
        display.blit(menu_picture,(0,0))
        display.blit(start_picture,(x,380))
        display.blit(control_picture,(x1,465))
        display.blit(about_picture,(x2,560))
        pygame.display.update()
        mouse_position=pygame.mouse.get_pos()
        mouse_press=pygame.mouse.get_pressed()
        if (mouse_position[0]>=5 and mouse_position[0]<=305) and (mouse_position[1]>=380 and mouse_position[1]<=455):
            x=25
            if mouse_press[0]==1:
                channel2.play(pygame.mixer.Sound('cargame/music/button_move.wav'),0)
                menu=False
                control=False
                about=False
                channel1.stop()
                time.sleep(1)
                channel2.stop()
                display.fill(black)
        else:
            x=5
        if (mouse_position[0]>=5 and mouse_position[0]<=305) and (mouse_position[1]>=465 and mouse_position[1]<=540):
            x1=25
            if mouse_press[0]==1:
                channel2.play(pygame.mixer.Sound('cargame/music/button_move.wav'),0)
                menu=False
                control=True
                about=False
                channel1.stop()
                time.sleep(1)
                channel2.stop()
                display.fill(black)
        else:
            x1=5
        if (mouse_position[0]>=5 and mouse_position[0]<=305) and (mouse_position[1]>=560 and mouse_position[1]<=635):
            x2=25
            if mouse_press[0]==1:
               channel2.play(pygame.mixer.Sound('cargame/music/button_move.wav'),0)
               menu=False
               control=False
               about=True
               channel1.stop()
               time.sleep(1)
               channel2.stop()
               display.fill(black)
        else:
            x2=5
        clock.tick(10)
        

def control_fun():
    global control
    global menu
    global game
    x=5
    play_music('cargame/music/both_music.mp3',-1)
    while control:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                control=False
        display.blit(control_image,(0,0))
        display.blit(back_picture,(x,560))
        pygame.display.update()
        mouse_position=pygame.mouse.get_pos()
        mouse_press=pygame.mouse.get_pressed()
        if (mouse_position[0]>=5 and mouse_position[0]<=305) and mouse_position[1]>=560 and mouse_position[1]<=635:
              x=25
              if mouse_press[0]==1:
                  play_music('cargame/music/button_move.mp3',0)
                  control=False
                  menu=True
                  about=False
                  time.sleep(1)
                  display.fill(black)
        else:
            x=5
        clock.tick(10)


def about_fun():
    global control
    global menu
    global about
    global game
    x=5
    play_music('cargame/music/both_music.mp3',-1)
    while about:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
                about=False
        display.blit(about_image,(0,0))
        display.blit(back_picture,(x,560))
        pygame.display.update()
        mouse_position=pygame.mouse.get_pos()
        mouse_press=pygame.mouse.get_pressed()
        if (mouse_position[0]>=5 and mouse_position[0]<=305) and mouse_position[1]>=560 and mouse_position[1]<=635:
              x=25
              if mouse_press[0]==1:
                  play_music('cargame/music/button_move.mp3',0)
                  control=False
                  menu=True
                  about=False
                  time.sleep(1)
                  display.fill(black)
        else:
            x=5
        clock.tick(10)

def game_button_check(x,width,y,height,button_name):
     global pause
     global menu
     global control
     global about
     global reset
     mouse_position=pygame.mouse.get_pos()
     mouse_press=pygame.mouse.get_pressed()
     if (mouse_position[0]>=5 and mouse_position[0]<=5+width) and (mouse_position[1]>=y and mouse_position[1]<=y+height):
         if mouse_press[0]==1:
              if button_name=='running':
                  channel3.pause()
                  channel4.pause()
                  play_music('cargame/music/button_click.mp3',0)
                  pause=True
                  display.blit(pause_image,(5,80))
                  time.sleep(0.6)
              if button_name=='quit':
                  play_music('cargame/music/button_click.mp3',0)
                  time.sleep(0.6)
                  menu=True
                  reset=False
                  new_game()
                  display.fill(black)
              if button_name=='pause':
                  play_music('cargame/music/button_click.mp3',0)
                  time.sleep(0.6)
                  pause=False
                  #unpause_music()
                  channel3.unpause()
                  channel4.unpause()
                  

def pause_fun():
    global pause
    global game
    #pause_music()
    #channel3.pause()
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pause=False
                game=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    pause=False
                    channel3.unpause()
                    channel4.unpause()
                    #unpause_music()
        game_button_check(5,52,80,52,'pause')
        display.blit(pause_image1,(140,350))
        pygame.display.update()
        clock.tick(20)

        
#classes objects_________------
_car1=main_car(450,0,200,0,0)
_car2=other_car(130,50,0)
_car3=other_car(270,150,1)
_truck=other_car(350,450,2)
_zebra=class_zebra((-(road1.get_height())*2)-34,0)

#important_variables_____________++++++++++========

collision_list=[_car2,_car3,_truck]
car_choice=[0,1,2]
road_y1=0
road_y2=-road1.get_height()+20
area_change=0
clip_y1=0
clip_y2=-clip.get_height()+10
blast=False
car2_blast=False
car3_blast=False
truck_blast=False
i=0
fps=60


def reset_fun():
    global blast
    global car2_blast
    global car3_blast
    global truck_blast
    global control
    global menu
    global about
    global game
    global pause
    global area_change
    global road_y1
    global road_y2
    global clip_y1
    global clip_y2
    global i
    global fps
    global reset
    play_music('cargame/music/reset_music.mp3',-1)
    while reset:
        game_button_check(5,52,20,52,'quit')
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                reset=False
                game=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RETURN:
                    
                    _car1.y=450
                    _car1.change_y=0
                    _car1.x=200
                    _car1.move_car=0
                    _car1.change_x=0

                    _car2.x=130
                    _car2.y=-100
                    _car2.position=0

                    _car3.x=270
                    _car3.y=-20
                    _car3.position=1

                    _truck.x=350
                    _truck.y=-200
                    _truck.position=2

                    _zebra.zebra_y=(-(road1.get_height())*2)-34
                    _zebra.check_zebra=0

                    road_y1=0
                    road_y2=-road1.get_height()+20
                    clip_y1=0
                    clip_y2=-clip.get_height()+10
                    area_change=30
                    i=0
                    fps=60
                    
                    blast=False
                    car2_blast=False
                    car3_blast=False
                    truck_blast=False
                    control=False
                    menu=False
                    about=False
                    game=True
                    pause=False
                    reset=False
                    display.fill(white)
                    stop_music()
                    #play_music('cargame/music/car_move.mp3',-1)
                    channel4.play(pygame.mixer.Sound('cargame/music/background.wav'),-1)
                    channel3.play(pygame.mixer.Sound('cargame/music/car_move.wav'),-1)
        display.blit(reset_image,(47,440))
        pygame.display.update()
        clock.tick(20)


def new_game():
    global blast
    global car2_blast
    global car3_blast
    global truck_blast
    global control
    global about
    global game
    global pause
    global area_change
    global road_y1
    global road_y2
    global clip_y1
    global clip_y2
    global i
    global fps
    global reset
    global start
    
    _car1.y=450
    _car1.change_y=0
    _car1.x=200
    _car1.move_car=0
    _car1.change_x=0

    _car2.x=130
    _car2.y=-100
    _car2.position=0

    _car3.x=270
    _car3.y=-20
    _car3.position=1

    _truck.x=350
    _truck.y=-200
    _truck.position=2

    _zebra.zebra_y=(-(road1.get_height())*2)-34
    _zebra.check_zebra=0

    road_y1=0
    road_y2=-road1.get_height()+20
    clip_y1=0
    clip_y2=-clip.get_height()+10
    area_change=0
    i=0
    fps=60
    
    blast=False
    car2_blast=False
    car3_blast=False
    truck_blast=False
    control=False
    about=False
    game=True
    pause=False
    reset=False
    start=True
                    
while game:
    if menu==True:
        menu_start()
    elif control==True:
        control_fun()
    elif about==True:
        about_fun()
    elif pause==True:
        pause_fun()
    elif reset==True:
        reset_fun()
    else:
        if start==True:
            if not pygame.mixer.music.get_busy():
                play_music('cargame/music/reset_music.mp3',-1)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game=False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP and start==False:
                    _car1.change_y=-10
                if event.key==pygame.K_RIGHT and start==False:
                    car1,car1_mask=rotate_image(-10)
                    _car1.change_x=15
                if event.key==pygame.K_LEFT and start==False:
                    car1,car1_mask=rotate_image(10)
                    _car1.change_x=-15
                if event.key==pygame.K_RETURN:
                    if start==True:
                        stop_music()
                        time.sleep(0.2)
                        area_change=30
                        start=False
                        #play_music('cargame/music/car_move.mp3',-1)
                        channel4.play(pygame.mixer.Sound('cargame/music/background.wav'),-1)
                        channel3.play(pygame.mixer.Sound('cargame/music/car_move.wav'),-1)
            if event.type==pygame.KEYUP and start==False:
                if event.key==pygame.K_RIGHT:
                    _car1.change_x=0
                    car1,car1_mask=rotate_image(0)
                if event.key==pygame.K_LEFT:
                    _car1.change_x=0
                    car1,car1_mask=rotate_image(0)

        road_y1+=area_change
        road_y2+=area_change
        clip_y1+=area_change
        clip_y2+=area_change
        if road_y1>=screen_height:
            road_y1=-road1.get_height()+20
            _zebra.check_zebra+=1
        if clip_y1>=screen_height:
            clip_y1=-clip.get_height()+10
        if clip_y2>=screen_height:
            clip_y2=-clip.get_height()+10   
        if road_y2>=screen_height:
            road_y2=-road1.get_height()+20
            _zebra.check_zebra+=1
        if _zebra.zebra_y>=screen_height:
            _zebra.zebra_y=-road1.get_height()-34
            _zebra.check_zebra=0
        display.fill(green)
        pygame.draw.rect(display,white,[110,0,366,650])
        display.blit(road1,(110,road_y1))
        display.blit(road2,(110,road_y2))
        display.blit(clip,(20,clip_y1))
        display.blit(clip,(20,clip_y2))
        display.blit(clip2,(466,clip_y1))
        display.blit(clip2,(466,clip_y2))
        pygame.draw.rect(display,gray,[110,0,10,650])
        pygame.draw.rect(display,gray,[466,0,10,650])
        display.blit(quit_image,(5,20))
        display.blit(running_image,(5,80))
        game_button_check(5,52,20,52,'quit')
        if start==False and blast==False:
            game_button_check(5,52,80,52,'running')
        if start==True:
            display.blit(reset_image,(47,380))
        
        if _zebra.check_zebra>=10:
            _zebra.draw_zebra()
            _zebra.zebra_y+=area_change
        if blast!=True:
            _car1.draw_car()
        else:
            try:
                display.blit(blast_image[i],(_car1.x,_car1.y))
                i+=1
            except:
                reset=True
        if car2_blast==True:
            display.blit(new_car,(position))
        else:
            _car2.draw_car()
        if car3_blast==True:
            display.blit(new_car,(position))
        else:
            _car3.draw_car()
        if truck_blast==True:
            display.blit(new_car,(position))
        else:
            _truck.draw_car()
        check=0
        for obstacle in collision_list:
            if blast!=True:
                offset=(int(_car1.x)-obstacle.x,int(_car1.y)-obstacle.y)
                if (obstacle_list[check].overlap(car1_mask,(offset))!=None):
                    if obstacle.x<=160 and obstacle.x>=120:
                        car2_blast=True
                        new_car=cars[_car2.position]
                        new_car=pygame.transform.rotate(new_car,40)
                        _car2.y-=20
                        position=(_car2.x,_car2.y)
                    elif obstacle.x<=270 and obstacle.x>=230:
                        car3_blast=True
                        new_car=cars[_car3.position]
                        new_car=pygame.transform.rotate(new_car,-30)
                        _car3.y-=20
                        position=(_car3.x,_car3.y)
                    elif obstacle.x<=366 and obstacle.x>=330:
                        truck_blast=True
                        new_car=cars[_truck.position]
                        new_car=pygame.transform.rotate(new_car,30)
                        _truck.y-=20
                        position=(_truck.x,_truck.y)
                    blast=True
                    area_change=0
                    fps=10
                    channel3.stop()
                    channel4.stop()
                    play_music('cargame/music/explosion.mp3',1)
                else:
                    check+=1
        if _car1.x<110 or _car1.x>415:
            if blast==False:
                play_music('cargame/music/explosion.mp3',1)
            blast=True
            channel3.stop()
            channel4.stop()
            area_change=0
            fps=10
        if _car2.y>=screen_height:
            _car2.y=-random.choice([x for x in range(130,205,5)])
            _car2.x=random.choice([x for x in range(120,160,2)])
            _car2.position=random.choice(car_choice)
        else:
            _car2.y+=area_change
        if _car3.y>=screen_height:
            _car3.y=-random.choice([x for x in range(330,405,5)])
            _car3.x=random.choice([x for x in range(230,270,2)])
            _car3.position=random.choice(car_choice)
        else:
            _car3.y+=area_change
        if _truck.y>=screen_height:
            _truck.y=-random.choice([x for x in range(530,605,5)])
            _truck.x=random.choice([x for x in range(330,366,2)])
            _truck.position=random.choice(car_choice)
        else:
            _truck.y+=area_change

        _car1.y+=_car1.change_y
        _car1.x+=_car1.change_x
        if _car1.y<=100:
            _car1.change_y=15
        elif _car1.y>=450:
            _car1.change_y=0
        if menu==True:
            new_game()
            display.fill(black)
        pygame.display.update()
        clock.tick(fps)

#####################        
pygame.quit()
quit()
