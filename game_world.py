import pygame, random, os, sys
from entity import * 
# (NOTE) Abstract terrain content from main file into here

'''class terrain:
    def __init__(self):
        pass'''
particles = []

def rain(window):
    x = random.randint(120, 1000)
    y = random.randint(180, 200)
    #y = 400
    #particles.append([[x, y], [1,1], 2.5])
    particles.append([[x, y], [1,1], 3])
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= 0.1
        particle[1][1] += 0.1
        pygame.draw.circle(window, (0, 20, 100), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

def custom_particles(window, time_pf, x_range, y_range, colour):
    x = random.randint(120, 1000)
    y = random.randint(180, 200)
    #y = 400
    #particles.append([[x, y], [1,1], 2.5])
    particles.append([[x, y], [1,1], 3])
 
    for particle in particles:
        particle[0][0] += particle[1][0]
        particle[0][1] += particle[1][1]
        particle[2] -= time_pf
        particle[1][1] += 0.1
        pygame.draw.circle(window, colour, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
        if particle[2] <= 0:
            particles.remove(particle)

        
class weather:
    def __init__(self, curr_weather, window):
        self.curr_weather = curr_weather
        self.window = window
    def change_weather(self, weather_type, sky, new_sky):
        self.sky = sky
        self.weather_type = weather_type
        if self.weather_type == "rain":
            sky.swapSprite(new_sky)
            sky.Scale(3)
            x_range = random.randint(120, 1000)
            y_range = y = random.randint(180, 200)
            colour = (0, 20, 200)
            #rain(self.window)
            custom_particles(self.window, 0.01, x_range, y_range, colour)
        # Change Background 


para_scale_buffer = 0.5
def gen_world_objects(offset, y, filepath, chunk_x, world_terrain, layer):
    index = len(chunk_x) - 1
    for chunk in world_terrain:
        for x in chunk_x:
            chunk = Entity(chunk_x[index]+offset,y,filepath)
            layer.add(chunk)
            chunk.Scale(para_scale_buffer)
        index -= 1
        # (NOTE) - Needs refining: Use index and count down to 0 to use arr values