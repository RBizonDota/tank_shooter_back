from config.settings import *

from app.conf import socketio

from math import sin, cos, pi, trunc

from processing.utils import point_in_wall, point_in_tank


def control_bullets(field):
    bullets_to_delete = []
    tanks_to_delete = []
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
        
        for tank in field.get_data()["tanks"].values():
            if tank["id"] !=bullet["tank_fired"]:
                if point_in_tank({
                        "x": bullet["x"],
                        "y": bullet["y"],
                    }, tank):
                    tank["health"]["current"]-=bullet["damage"]
                    if tank["health"]["current"]<=0:
                        # del field.get_data()["tanks"][tank["id"]]
                        tanks_to_delete.append(tank["id"])
                        socketio.emit('tank_eliminated', tank, namespace='/field')
                    bullets_to_delete.append(i)

        move_const = BASE_BULLET_MOVE_SPEED*bullet["speed_mod"]
        
        if bullet["speed_slow"]:
            move_const*=(1-0.7*bullet["trace"]/bullet["max_trace"])

        az = bullet["az"]
        bullet["x"]+=move_const*cos(pi/180*az)
        bullet["y"]+=move_const*sin(pi/180*az)
        bullet["trace"]+=move_const

    for tank_id in tanks_to_delete:
        del field.get_data()["tanks"][tank_id]
                
    for i in bullets_to_delete:
        if field._data["bullets"]:
            del field._data["bullets"][i]

    return True

def collision_walls(field):
    pass

def collision_tanks(field):
    pass