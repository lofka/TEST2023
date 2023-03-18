import pygame as pg
import pymunk.pygame_util
from  random import*
pymunk.pygame_util.positive_y_is_up = False

#Настройки PyGame
RES = WIDTH, HEIGHT = 1200, 700
FPS = 60

pg.init()
surface = pg.display.set_mode(RES)
clock = pg.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)


#Отрисовка PyGame
space = pymunk.Space()
space.gravity = 0, 10000    
sk_shape=1
el_shape=1



    
    
segment_shape = pymunk.Segment(space.static_body, (2, HEIGHT), (WIDTH, HEIGHT), 26)
space.add(segment_shape)
segment_shape.elasticity = el_shape
segment_shape.friction = sk_shape

segment_shape2 = pymunk.Segment(space.static_body, (2, 2), (WIDTH, 2), 26)
space.add(segment_shape2)
segment_shape2.elasticity = el_shape
segment_shape2.friction = sk_shape   

segment_shape3 = pymunk.Segment(space.static_body, (WIDTH, 2), (WIDTH, HEIGHT), 26)
space.add(segment_shape3)
segment_shape3.elasticity = el_shape
segment_shape3.friction = sk_shape   

segment_shape4 = pymunk.Segment(space.static_body, (2, 2), (2, HEIGHT), 26)
space.add(segment_shape4)
segment_shape4.elasticity = el_shape
segment_shape4.friction = sk_shape   
body=pymunk.Body()
def create_square(space, pos):
    u=randint(30, 250)
    square_mass, square_size = 1, (u, u)
    square_moment = pymunk.moment_for_box(square_mass, square_size)
    square_body = pymunk.Body(square_mass, square_moment)
    square_body.position = pos
    square_shape = pymunk.Poly.create_box(square_body, square_size)
    square_shape.elasticity = 1
    square_shape.friction = 0 
    square_shape.color=[randrange(256)for i in range(4) ]
    space.add(square_body,square_shape)
def create_ball(space, pos):
    u=randint(30, 100)
    ball_mass,ball_radius=1,u
    ball_moment=pymunk.moment_for_circle(ball_mass,0,ball_radius)
    ball_body=pymunk.Body(ball_mass,ball_moment)

    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body,ball_radius)
    ball_body.elasticity = 1
    ball_body.friction = 0
    ball_shape.color=[randrange(256)for i in range(4) ]
    space.add(ball_body,ball_shape)








while True:
    surface.fill(pg.Color('dark green'))

    for i in pg.event.get():
        if i.type == pg.QUIT:
            exit()
        if i.type == pg.MOUSEBUTTONDOWN:
            if i.button==1:
                create_square(space,i.pos)
                print(i.pos) 
            if i.button==3:
                create_ball(space,i.pos)
                print(i.pos) 


    space.step(1 / FPS)
    space.debug_draw(draw_options)
    pg.display.flip()
    clock.tick(FPS)
