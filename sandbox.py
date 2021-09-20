import pygame as pg
from pygame.locals import * 
from entity import *
from game_world import * 
from framework import * 
from main import *

# Project Init
pg.init()
fps = 144
fps_clock = pg.time.Clock()
window = pg.display.set_mode((width, height))
pg.display.set_caption(project_title)
running = True 

# (AREA) Entity Hierachy Area - implicit 
skybox = Entity(0,-50, "assets/bluesky_1.jpg")
mountain = Entity(850, 380, "assets/mountain_1.png")
# (AREA) Entity -> Layer
gen_world_objects(-100, 550,"assets/grass_hills_1_light.png", para_x, para_x, midground_1, 0.7)
gen_world_objects(0, 577,"assets/grass_hills_1.png", para_x, para_x, midground, 0.7)
gen_world_objects(0, treeline, "assets/pinetree_2.png", tree_x, tree_x, foreground, 0.5)
gen_world_objects(0, 708,"assets/GroundTextureLong2.png", [550,650*2,650*3], [650,650*2,650*3], terrain, 1.1)
gen_world_objects(100, 586, "assets/grass_hills_1_light_test.png", para_x, para_x, midground, 0.53)
sky.add(skybox)
background_2.add(mountain)
# (AREA) Entity Scaling 
skybox.Scale(3)
from camera import * 

def render_window(window, dt, layer_data_1, layer_data_2):
    keys = pg.key.get_pressed()
    camera_differing = [0.05*dt,0.05*dt,0.1*dt,0.15*dt,0.2*dt,0.25*dt,0.3*dt]
    update_screen(window, layer_data_1)
    if keys[pg.K_d]:
        move_camera(window, sky, [background_2, background_1, background], [midground_1, midground], [foreground, terrain], "left", camera_differing)
    if keys[pg.K_a]:
        move_camera(window, sky, [background_2, background_1, background], [midground_1, midground], [foreground, terrain], "right", camera_differing)
    update_frame(foreground,window)
    update_frame(terrain,window)
    pg.display.flip()

dt = 1/fps
while running: 
    event_system(width, height)
    render_window(window, dt, layer_hierachy_bg, layer_hierachy_fg)
    dt = fps_clock.tick(fps)

pg.quit()