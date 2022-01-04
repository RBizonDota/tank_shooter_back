from config.settings import *

from math import sin, cos, pi
sign = lambda a: (a>0) - (a<0)

from utility.logger import Logger

from processing.utils import point_in_wall

int_to_acceleration = {
    1:"forward",
    -1:"back"
}

logger = Logger(log_level=2)

def control_tanks(field):
    changed = False
    for tank_id, control_unit in field._user_control.items():
        logger.debug("Data", field._data["tanks"])
        logger.debug("User control", field._user_control)
        logger.debug("Users", field.users)
        tank_data = field._data["tanks"].get(tank_id)
        if not tank_data:
            continue

        # Поворот
        tank_data["napr"]["az"]+=BASE_ROTATE_SPEED*control_unit["rotate"]
        tank_data["napr"]["b_az"]+=BASE_ROTATE_SPEED*control_unit["rotate"]

        # Поворот башни
        tank_data["napr"]["b_az"]+=BASE_BASE_ROTATE_SPEED*control_unit["b_rotate"]
        
        if tank_data["napr"]["az"]>360:
            tank_data["napr"]["az"]-=360
        if tank_data["napr"]["az"]<0:
            tank_data["napr"]["az"]+=360
        
        if tank_data["napr"]["b_az"]>360:
            tank_data["napr"]["b_az"]-=360
        if tank_data["napr"]["b_az"]<0:
            tank_data["napr"]["b_az"]+=360
        # print(control_unit)
        
        # Скорость
        if control_unit["move"]:
            tank_data["moving"]["speed"]+=tank_data["moving"]["acceleration"][int_to_acceleration[control_unit["move"]]]*control_unit["move"]
            if not (-1*tank_data["moving"]["max_speed"]["back"]<tank_data["moving"]["speed"]<tank_data["moving"]["max_speed"]["forward"]):
                tank_data["moving"]["speed"] = -1*tank_data["moving"]["max_speed"]["back"] if tank_data["moving"]["speed"]<0 else tank_data["moving"]["max_speed"]["forward"]
        elif abs(tank_data["moving"]["speed"])<BASE_ACCELERATION_LOSS:
            tank_data["moving"]["speed"] = 0
        else:
            tank_data["moving"]["speed"]-=sign(tank_data["moving"]["speed"])*BASE_ACCELERATION_LOSS
        
        # print("SPEEEEEEED", tank_data["moving"]["speed"])

        # Движение
        move_const = tank_data["moving"]["speed"]
        az = tank_data["napr"]["az"]
        # if control_unit["move"]<0:
        #     move_const = BASE_MOVE_SPEED_BACK
        tank_data["pos"]["x"]+=move_const*cos(pi/180*az)
        tank_data["pos"]["y"]+=move_const*sin(pi/180*az)

        # Определение коллизии
        for vx,vy in [(-1, -1), (-1, 1), (1, 1), (1, -1)]:
            for wall in field.get_data()["walls"]:
                # print(field.get_data()["walls"])
                is_collision, ddata = point_in_wall({
                    "x": tank_data["pos"]["x"]+vx*tank_data["size"]["x"]/2,
                    "y": tank_data["pos"]["y"]+vy*tank_data["size"]["y"]/2,
                }, wall)
                if is_collision:
                    tank_data["pos"]["x"]-=vx*ddata["dx"]
                    tank_data["pos"]["y"]-=vy*ddata["dy"]

        # Огонь
        fire_rate = BASE_FIRE_RATE
        if control_unit["fire"] and tank_data["fire"]["current"]>=fire_rate:
            logger.warn("FIRE !!!!!!", tank_id)
            # new_bullets.push({
            #     x: new_tank_data.pos.x+new_tank_data.size.x/2,
            #     y: new_tank_data.pos.y+new_tank_data.size.y/2,
            #     az: new_tank_data.napr.b_az
            # })
            new_bullet = {
                "x": tank_data["pos"]["x"],
                "y": tank_data["pos"]["y"],
                "az": tank_data["napr"]["b_az"],
                "trace":0,
                "max_trace":BASE_BULLET_MAX_TRACE,
                "speed_mod": BASE_BULLET_SPEED_MOD,
                "speed_slow": BASE_BULLET_SPEED_SLOW
            }
            field._data["bullets"].append(new_bullet)
            tank_data["fire"]["current"] = 0
            changed=True

        if tank_data["fire"]["current"]<fire_rate:
            tank_data["fire"]["current"]+=1
    return True
    # return True

def collision_walls(walls, tank_data):
    pass