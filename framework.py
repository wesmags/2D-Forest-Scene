import pygame, sys
from pygame.locals import * 
from camera import * 


def event_system(width, height):
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


class game_base:
    def render_window(self, window, dt, layer_data_1, layer_data_2):
        keys = pygame.key.get_pressed()
        camera_differing = [0.05*dt,0.05*dt,0.1*dt,0.15*dt,0.2*dt,0.25*dt,0.3*dt]
        for layer in layer_data_1:
            render_layer = layer_data_1[layer]
            render_layer.draw(window)
            render_layer.update()
        update_frame(layer_data_2[0],window)
        update_frame(layer_data_2[1],window)