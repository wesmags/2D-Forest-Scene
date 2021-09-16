# Based off of code by Dafluffypotato
import pygame, sys, random
from framework import * 
from game_world import *

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption(' Particles ')
screen = pygame.display.set_mode((500, 500),0,32)
 

particles = []


    
speed = [random.randint(0, 20) / 10 - 1, -2]
radius = random.randint(4, 6)

world_particles = custom_particles_v1(0.35, (100, 200,0), -0.2)

#world_particles_v2 = custom_particles_v2([1,1], 0.1)

while True:
    event_system(500, 500)
    screen.fill((0,0,0))
    mx, my = pygame.mouse.get_pos()
    world_particles.render_particles(mx, my, random.randint(6, 8), screen, particles)
    #world_particles_v2.render_particles(mx, my, random.randint(4, 6), screen, particles)

               
    pygame.display.update()
    mainClock.tick(60)