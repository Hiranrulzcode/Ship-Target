import random
import pgzrun
import itertools

WIDTH=400
HEIGHT=400

ship=Actor("ship")
box=Actor("box")
ship.pos=200,200
box.pos=50,50
boxps=[(350,50), (350,350), (50,350), (50,50)]
boxmove=itertools.cycle(boxps)


def draw():
    screen.clear()
    ship.draw()
    box.draw()
    

def move_box():
    animate (box, "bounce_end", duration=1, pos=next(boxmove))

def pick_target():
    x=random.randint(100,300)
    y=random.randint(100,300)
    ship.target=x,y
    target_angle=ship.angle_to(ship.target)
    target_angle+=360*((ship.angle-target_angle+180)//360)
    animate(ship, angle=target_angle, duration=1, on_finished=move_ship)



def move_ship():
    a=animate(ship, tween='accel_deceel', pos=ship.target, duration=ship.distance_to(ship.target)/200, on_finished=pick_target)

pick_target()




    

move_box()
clock.schedule_interval(move_box, 2)
































pgzrun.go()