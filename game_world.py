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



def gen_world_objects(offset, y, filepath, chunk_x, world_terrain, layer, para_scale_buffer):
    index = len(chunk_x) - 1
    for chunk in world_terrain:
        for x in chunk_x:
            chunk = Entity(chunk_x[index]+offset,y,filepath)
            layer.add(chunk)
            chunk.Scale(para_scale_buffer)
        index -= 1
        # (NOTE) - Needs refining: Use index and count down to 0 to use arr values


    
def gen_chunk(y, chunk_x, terrain):
    index = len(chunk_x) - 1
    for i in chunk_x:
        for x in chunk_x:
            chunk = Entity(chunk_x[index],y,"assets/chunk_1.png")
            terrain.add(chunk)
            chunk.Scale(0.7)
        index -= 1
        # (NOTE) - Needs refining: Use index and count down to 0 to use arr values

    
# (AREA) Layer Initialisation
terrain = pygame.sprite.Group()
foreground = pygame.sprite.Group()
midground = pygame.sprite.Group()
midground_1 = pygame.sprite.Group()
background = pygame.sprite.Group()
background_1 = pygame.sprite.Group()
background_2 = pygame.sprite.Group()
sky = pygame.sprite.Group()

layer_hierachy_bg = {
    1 : sky,
    2 : background_2,
    3 : background_1,
    4 : background,
    5 : midground_1,
    6 : midground
}


layer_hierachy_fg = {
    1 : foreground,
    2 : terrain
}


# Based off code by Dafluffypotato
class custom_particles_v1:
    def __init__(self, decrement_pf, colour, increment_pf):
        self.decrement_pf = decrement_pf
        self.colour = colour
        self.increment_pf = increment_pf
    def render_particles(self, x, y, radius, window, particles = []):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.window = window
        self.particles = particles
        self.particles.append([[self.x, self.y], [0,-1], radius])
    
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= self.decrement_pf
            particle[1][1] += self.increment_pf
            pygame.draw.circle(self.window, self.colour, [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)


class custom_particles_v2:
    def __init__(self, speed, decrement_pf):
        self.speed = speed
        self.decrement_pf = decrement_pf
    def render_particles(self, x, y, radius, window, particles = []):
        self.x = x 
        self.y = y 
        self.radius = radius
        self.window = window
        self.particles = particles
        self.particles.append([[self.x, self.y], self.speed, radius])
    
        for particle in particles:
            particle[0][0] += particle[1][0]
            particle[0][1] += particle[1][1]
            particle[2] -= self.decrement_pf
            particle[1][1] += 0.1
            pygame.draw.circle(self.window, (255, 255, 255), [int(particle[0][0]), int(particle[0][1])], int(particle[2]))
            if particle[2] <= 0:
                self.particles.remove(particle)