from entity import *
from game_world import * 
from framework import * 
import pygame

pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Sandbox") 
fps = 60
fpsClock = pygame.time.Clock()
dt = 1/fps

class Sandbox(game_base):
    def render_window(self, window, dt, layer_data_1, layer_data_2):
        return super().render_window(window, dt, layer_data_1, layer_data_2)


sandbox = Sandbox()

player = Entity(0,0,"assets/pinetree_1.png")
terrain.add(player)
fg = [foreground, terrain]


while True:
    win.fill((0,0,150))
    event_system(500, 500)
    sandbox.render_window(win, dt, layer_hierachy_bg, fg)
    dt = fpsClock.tick(fps)