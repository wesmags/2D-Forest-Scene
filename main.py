import sys, os, random
 
import pygame
from pygame.locals import *
from project import *
from entity import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

width, height = 1280, 720
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(project_title) 

keys = pygame.key.get_pressed()

world_terrain = [0,0,0,0,0,0,0,0,0,0]



origin = 0
offset = 140
chunk_x = [origin,offset,offset*2,offset*3,offset*4,offset*5,offset*6,offset*7,offset*8,offset*9]




skybox = Entity(0,-50, "assets/bluesky_1.jpg")

hills = Entity(850,499, "assets/hills_2.png")

    


foreground = pygame.sprite.Group()
sky = pygame.sprite.Group()

def gen_parallax_layer(parallax_amount,parallax_x,y):
    index = len(chunk_x) - 1
    for chunk in world_terrain:
        for x in chunk_x:
            chunk = Entity(chunk_x[index],y,"assets/chunk_1.png")
            foreground.add(chunk)
            chunk.Scale(0.7)
        index -= 1

def gen_chunk(y):
    index = len(chunk_x) - 1
    for chunk in world_terrain:
        for x in chunk_x:
            chunk = Entity(chunk_x[index],y,"assets/chunk_1.png")
            foreground.add(chunk)
            chunk.Scale(0.7)
        index -= 1
    
            # Use index and count down to 0 to use arr values


sky.add(skybox)
foreground.add(hills)
gen_chunk(685)          


skybox.Scale(2)
hills.Scale(0.6)

def event_system():
    keys = pygame.key.get_pressed()
    is_fs = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit() 
        if event.type == VIDEORESIZE:
            window = pygame.display.set_mode((width, height), pygame.RESIZABLE)
        if keys[pygame.K_F11]:
            is_fs = not is_fs
            if is_fs == True:
                window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            else:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)


particles = []
particles_2 = []

def redraw_window(window, dt):
    # Redraw window here.
    sky.draw(window)
    sky.update()
    foreground.draw(window)
    foreground.update()

    x = random.randint(120, 200)
    y = random.randint(180, 200)
    particles.append([[x, y], [1,1], 2.5])
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(window, (0, 180, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)
    pygame.display.flip()

dt = 1/fps

# Game loop.
while True:
    event_system()
    redraw_window(window, dt)
    dt = fpsClock.tick(fps)