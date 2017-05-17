#!/usr/bin/python
#encoding=utf-8
import pygame,sys,time
from pygame.locals import *
pygame.init()
FPS=30
fpsClock=pygame.time.Clock()
#set up the windows
SCREEN=pygame.display.set_mode((400,300),0,32)
pygame.display.set_caption('plane')
WHITE=(255,255,255)
BLACK=(0,0,0)
GREP=(128,128,128)
plane=pygame.image.load('/home/xdw/桌面/爬虫/plane.jpg')
#bullet=pygame.image.load('/home/xdw/桌面/爬虫/zidan.jpg')
pygame.mixer.music.load('/home/xdw/下载/%E6%B4%9B%E5%A4%A9%E4%BE%9D+-+%E9%9C%9C%E9%9B%AA%E5%8D%83%E5%B9%B4.mp3')
pygame.mixer.music.play(-1,0.0)
planex=10
planey=250
while True:#the main game loop
    #pygame.mixer.music.play(-1,0.0)
    if planex==350:
        k=0
    elif planex==10:
        k=1    
    if k==1:
        planex+=5
    elif k==0:
        planex-=5
    SCREEN.fill(WHITE)
    SCREEN.blit(plane,(planex,planey))
    #SCREEN.blit(bullet,(planex+15,planey-25))
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    #time.sleep(0.5)
    
    pygame.display.update()
    fpsClock.tick(FPS)
