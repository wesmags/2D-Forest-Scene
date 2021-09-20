import pygame

# (NOTE) Quick fix to multiple layer iteration rendering issue
def update_frame(layer,window):
    layer.draw(window)
    layer.update()

# (NOTE)
def update_frame_c(layer,window, dir, dir_amount):
    layer.update(dir, dir_amount)

# (NOTE) Currently Depreciated 
def debug_move_camera(window, layer_data, layer_f, direction, dir_amount):
    for layer in layer_data:
        render_layer = layer_data[layer]
        render_layer.update(direction, dir_amount)
    update_frame_c(layer_f, window, direction, dir_amount)

def update_screen(window, layer_data_1):
    for layer in layer_data_1:
        render_layer = layer_data_1[layer]
        render_layer.draw(window)
        render_layer.update()

# (NOTE) 
def move_camera(window, sky, layer_b, layer_m, layer_f, direction, dir_amount):
    update_frame_c(sky, window, direction, dir_amount[0])
    update_frame_c(layer_b[0], window, direction, dir_amount[1])
    update_frame_c(layer_b[1], window, direction, dir_amount[2])
    update_frame_c(layer_b[2], window, direction, dir_amount[3])
    update_frame_c(layer_m[0], window, direction, dir_amount[4])
    update_frame_c(layer_m[1], window, direction, dir_amount[5])
    update_frame_c(layer_f[0], window, direction, dir_amount[6])
    update_frame_c(layer_f[1], window, direction, dir_amount[6])


'''
def move_camera(window, dir, amount, layer_data_1, foreground, terrain, dt):
    dir_amount = amount*dt
    for layer in layer_data_1:
        render_layer = layer_data_1[layer]
        render_layer.update(dir, dir_amount)
        dir_amount += 0.05

def move_camera(window, dir, amount, layer_data_1, layer_data_2, dt):
    dir_amount = amount*dt
    for layer in layer_data_1:
        render_layer = layer_data_1[layer]
        render_layer.update(dir, dir_amount)
        dir_amount += 0.05
    for layers in layer_data_2:
        render_layers = layer_data_2[layers]
        render_layers.update(dir, dir_amount)
        dir_amount += 0.05
'''