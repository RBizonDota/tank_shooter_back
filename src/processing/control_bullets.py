from config.settings import *

from math import sin, cos, pi, trunc

from processing.utils import point_in_wall


def control_bullets(field):
    bullets_to_delete = []
    for i, bullet in enumerate(field._data["bullets"]):
        
        if bullet["max_trace"]<bullet["trace"]:
            bullets_to_delete.append(i)

        for wall in field.get_data()["walls"]:
                # print(field.get_data()["walls"])
                is_collision, ddata = point_in_wall({
                    "x": bullet["x"],
                    "y": bullet["y"],
                }, wall)
                if is_collision:
                    bullets_to_delete.append(i)

        move_const = BASE_BULLET_MOVE_SPEED*bullet["speed_mod"]

        if bullet["speed_slow"]:
            move_const*=(1-0.7*bullet["trace"]/bullet["max_trace"])

        az = bullet["az"]
        bullet["x"]+=move_const*cos(pi/180*az)
        bullet["y"]+=move_const*sin(pi/180*az)
        bullet["trace"]+=move_const
                
    for i in bullets_to_delete:
        if field._data["bullets"]:
            del field._data["bullets"][i]

    return True

def collision_walls(field):
    pass

def collision_tanks(field):
    pass