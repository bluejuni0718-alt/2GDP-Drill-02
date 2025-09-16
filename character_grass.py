from operator import truediv
import pygame
from pico2d import *

open_canvas()

grass=load_image('grass.png')
character=load_image('character_R.png')
x=400
y=90
Direction=4



while(1):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    if(x==800 and y==90):
        Direction=1
    elif(x==800 and y==600):
        Direction=2
    elif(x==0 and y==600):
        Direction=3
    elif(x==0 and y==90):
        Direction=4

    if(Direction==1):
        y+=2
    elif(Direction==2):
        x-=2
    elif(Direction==3):
        y-=2
    elif(Direction==4):
        x+=2

    delay(0.01)

close_canvas()
