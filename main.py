import sys, os, random
 
import pygame
from pygame.locals import *


from project import *
from entity import *
from game_world import * 


pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

#width, height = 1280, 720
width, height = 1560, 800
window = pygame.display.set_mode((width, height))
pygame.display.set_caption(project_title) 

keys = pygame.key.get_pressed()

world_terrain = [0,0,0,0,0,0,0,0,0,0,0,0,0]
parallax_objs = [0,0,0]

parallax_origin = 850 
para_offset = 815

para_x = [parallax_origin, parallax_origin+para_offset, parallax_origin+para_offset*2]
para_y = 640
para_scale_buffer = 0.5

chunk_origin = 0
c_off = 140
chunk_x = [chunk_origin,c_off,c_off*2,c_off*3,c_off*4,c_off*5,c_off*6,c_off*7,c_off*8,c_off*9,c_off*10,c_off*11,c_off*12]
chunk_y = 765

treeline = 588


# (AREA) Entity Initialisation 
skybox = Entity(0,-50, "assets/bluesky_1.jpg")

hills = Entity(850,560, "assets/hills_3.png")

mountain = Entity(850, 499, "assets/grassy_mountain_1.png")

pine_tree = Entity(500, treeline, "assets/pinetree_2.png")
    


foreground = pygame.sprite.Group()
background = pygame.sprite.Group()
sky = pygame.sprite.Group()


    
def gen_chunk(y):
    index = len(chunk_x) - 1
    for chunk in world_terrain:
        for x in chunk_x:
            chunk = Entity(chunk_x[index],y,"assets/chunk_1.png")
            foreground.add(chunk)
            chunk.Scale(0.7)
        index -= 1
        # (NOTE) - Needs refining: Use index and count down to 0 to use arr values


sky.add(skybox)
#background.add(mountain)
#background.add(hills)
gen_world_objects(-100, 610,"assets/hills_3_dark.png", para_x, parallax_objs, background)
gen_world_objects(0, 640,"assets/hills_3.png", para_x, parallax_objs, background)
background.add(pine_tree)
gen_chunk(chunk_y)          



pine_tree.Scale(0.5)
skybox.Scale(3)
hills.Scale(para_scale_buffer)

def event_system():
    keys = pygame.key.get_pressed()
    is_fs = False
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() 
            sys.exit() 
        if keys[pygame.K_ESCAPE]:
            pygame.quit() 
            sys.exit() 
        if event.type == VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
        if keys[pygame.K_F11]:
            is_fs = not is_fs
            if is_fs == True:
                window = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
            else:
                window = pygame.display.set_mode((width, height), pygame.RESIZABLE)


particles = []
particles_2 = []



def create_particles():
    x = random.randint(120, 200)
    #y = random.randint(180, 200)
    y = 400
    particles.append([[x, y], [1,1], 2.5])
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(window, (0, 180, 0), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)


def tree_leaves(p_list,time_pf,duration,radius,colour,x,y,speed):
    particles.append([[x, y], [0.2,1], radius])
    timer = 10 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= time_pf
        particle[1][1] += duration
        if len(particles) < 100:
            pygame.draw.circle(window, colour, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)




layer_hierachy_bg = {
    1 : sky,
    2 : background
}
layer_hierachy_fg = {
    1 : foreground 
}

# (NOTE) Quick fix to multiple layer iteration rendering issue
def update_frame(layer,window):
    layer.draw(window)
    layer.update()

weather_handler = weather(None, window)

leaf_time = 0.01
leaf_dur = 0.0001
leaf_rad = 2
leaf_speed = [1,1]

def render_window(window, dt, layer_data_1, layer_data_2):
    # particle init
    leaves = []
    
    for layer in layer_data_1:
        render_layer = layer_data_1[layer]
        render_layer.draw(window)
        render_layer.update()
    #weather_handler.change_weather("rain", skybox,"assets/dark_sky_1.png")
    tree_leaves(leaves, leaf_time, leaf_dur, leaf_rad, (0,105,20), random.randint(275, 360),random.randint(180, 200), leaf_speed)
    update_frame(foreground,window)

    pygame.display.flip()





dt = 1/fps

# Game loop.
while True:
    event_system()
    render_window(window, dt, layer_hierachy_bg, layer_hierachy_fg)
    dt = fpsClock.tick(fps)
pygame.quit()