 
import pygame
from pygame.locals import *

from entity import *
from game_world import * 
from framework import * 

project_title = "Arcane"

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

#width, height = 1280, 720
width, height = 1560, 800
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Arcane") 

keys = pygame.key.get_pressed()


parallax_origin = 315 
para_offset = 395

para_x = [parallax_origin, parallax_origin+para_offset, parallax_origin+para_offset*2,parallax_origin+para_offset*3,parallax_origin+para_offset*4,parallax_origin+para_offset*5]
para_y = 640
para_scale_buffer = 0.5

chunk_origin = 0
c_off = 140
chunk_x = [chunk_origin,c_off,c_off*2,c_off*3,c_off*4,c_off*5,c_off*6,c_off*7,c_off*8,c_off*9,c_off*10,c_off*11,c_off*12,c_off*13,c_off*14,c_off*15,c_off*16,c_off*17,c_off*18,c_off*19,c_off*20]
chunk_x_a = [chunk_origin,c_off,c_off*2,c_off*3,c_off*4,c_off*5,c_off*6,c_off*7]
c_origin = -140
c_off = 140
final_c = c_origin+c_off-140
chunk_x_2 = [c_origin,final_c,final_c*2,final_c*3,final_c*4,final_c*5,final_c*6,final_c*7,final_c*8,final_c*9]
chunk_y = 765


t_off  = 250
t_origin = 500
t_pos = t_off + t_origin
tree_x = [t_origin, t_pos+t_off, t_pos*2, t_pos*2]

treeline = 588


# (AREA) Entity Initialisation 
skybox = Entity(0,-50, "assets/bluesky_1.jpg")
mountain = Entity(850, 380, "assets/mountain_1.png")



sky.add(skybox)
background_2.add(mountain)
gen_world_objects(-100, 550,"assets/grass_hills_1_light.png", para_x, para_x, midground_1, 0.7)
gen_world_objects(0, 577,"assets/grass_hills_1.png", para_x, para_x, midground, 0.7)
gen_world_objects(0, treeline, "assets/pinetree_2.png", tree_x, tree_x, foreground, 0.5)
gen_world_objects(100, 586, "assets/grass_hills_1_light_test.png", para_x, para_x, midground, 0.53)

# (NOTE) - Use 1 long ground texture instead of many different smaller ones
# Or alternatively create a chunk system 
gen_world_objects(0, 708,"assets/GroundTextureLong2.png", [550,650*2,650*3], [650,650*2,650*3], terrain, 1.1)


#gen_chunk(chunk_y, chunk_x_a, terrain)          
#gen_world_objects(0, chunk_y, "assets/chunk_1.png", chunk_x_2, chunk_x_2, terrain, 0.7)
skybox.Scale(3)

import sys, random

leaf = []
leaf_2 = []
leaf_3 = []
for i in range(10):
    x = random.randrange(275, 480)
    y = random.randrange(240, 260)
    x_2 = random.randrange(475, 680)
    y_2 = random.randrange(240, 260)
    leaf.append([x, y])
    leaf_2.append([x_2, y_2])


from camera import *

def draw_particles(dt):
    camera_differing = [0.05*dt,0.05*dt,0.1*dt,0.15*dt,0.2*dt,0.25*dt,0.3*dt]
    for i in range(len(leaf)):
        pygame.draw.circle(window, (0,100,0), leaf[i], 2)
        pygame.draw.circle(window, (0,100,0), leaf_2[i], 2)
        leaf[i][1] += random.randint(0,2)
        leaf_2[i][1] += random.randint(0,2)
        if keys[pygame.K_d]:
            leaf[i][0] -= round(camera_differing[6])
            leaf_2[i][0] -= round(camera_differing[6])
        if keys[pygame.K_a]:
            leaf[i][0] += round(camera_differing[6])
            leaf_2[i][0] += round(camera_differing[6])
        if leaf[i][1] > 500:
            y = random.randrange(200, 220) 
            leaf[i][1] = y
            x = random.randrange(275, 480)
            leaf[i][0] = x
            pygame.draw.circle(window, (0,100,0), leaf[i], 2)
        if leaf_2[i][1] > 500:
            y_2 = random.randrange(200, 220) 
            leaf_2[i][1] = y_2
            x_2 = random.randrange(475, 680)
            leaf_2[i][0] = x_2
            pygame.draw.circle(window, (0,100,0), leaf_2[i], 2)


def render_window(window, dt, layer_data_1, layer_data_2):
    keys = pygame.key.get_pressed()
    # particle init
    leaves = []
    camera_differing = [0.05*dt,0.05*dt,0.1*dt,0.15*dt,0.2*dt,0.25*dt,0.3*dt]
    update_screen(window, layer_data_1)
    if keys[pygame.K_d]:
        move_camera(window, sky, [background_2, background_1, background], [midground_1, midground], [foreground, terrain], "left", camera_differing)
    if keys[pygame.K_a]:
        move_camera(window, sky, [background_2, background_1, background], [midground_1, midground], [foreground, terrain], "right", camera_differing)
    
    #tree_leaves(leaves, leaf_time, leaf_dur, leaf_rad, (0,105,20), random.randint(275, 360),random.randint(180, 200), leaf_speed)
    draw_particles(dt)

    # (NOTE) gotta optimise the shit on terrain and tree rendering
    # Terrain needs most focus, make it not render when not in camera view + 1 chunk 
    update_frame(foreground,window)
    update_frame(terrain,window)

    pygame.display.flip()





dt = 1/fps

# Game loop.
while True:
    event_system(width, height)
    render_window(window, dt, layer_hierachy_bg, layer_hierachy_fg)
    dt = fpsClock.tick(fps)
pygame.quit()