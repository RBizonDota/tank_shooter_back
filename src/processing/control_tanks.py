from config.settings import *

from math import sin, cos, pi

from utility.logger import Logger

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

        # Движение
        move_const = BASE_MOVE_SPEED_FORWARD
        az = tank_data["napr"]["az"]
        if control_unit["move"]<0:
            move_const = BASE_MOVE_SPEED_BACK
        tank_data["pos"]["x"]+=move_const*cos(pi/180*az)*control_unit["move"]
        tank_data["pos"]["y"]+=move_const*sin(pi/180*az)*control_unit["move"]

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
                "x": tank_data["pos"]["x"]+tank_data["size"]["x"]/2,
                "y": tank_data["pos"]["y"]+tank_data["size"]["y"]/2,
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