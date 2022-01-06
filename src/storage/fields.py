from uuid import uuid4

from random import random

from utility.logger import Logger

from config.settings import *

logger = Logger()

def generate_tank_data(update_data):
    data = {
                # "id": "askjfhaskfgajsgfsajhdvajshg",
                
                # Здоровье
                "health":{
                    "current":BASE_MAX_HEALTH,
                    "max": BASE_MAX_HEALTH
                },

                # Параметры размеры
                "size":{
                    "x":BASE_SIZE_X,
                    "y":BASE_SIZE_Y,
                    "b_r":BASE_SIZE_BASE, #Радиус башни
                    "w_l": BASE_WEAPON_LENGTH,
                    "w_w": BASE_WEAPON_WIDTH
                },
                # Параметры направления
                "napr":{
                    "az":360*random(),
                    "b_az":0
                },
                # Параметры позиции
                "pos": {
                    "x": 100+800*random(),
                    "y":50+400*random()
                },
                # Параметры стрельбы (не менять)
                "fire":{
                    "current":BASE_FIRE_RATE,
                    "fire_rate": BASE_FIRE_RATE,
                    "damage": BASE_FIRE_DAMAGE
                },
                "moving":{
                    "speed":0,
                    # Параметры максимальных скоростей
                    "max_speed":{
                        "forward": BASE_MOVE_SPEED_FORWARD,
                        "back": BASE_MOVE_SPEED_BACK
                    },
                    # Ускорение
                    "acceleration":{
                        "forward": BASE_ACCELERATION,
                        "back": BASE_ACCELERATION
                    }
                },
                # Масса (пока не используется)
                "weight":50
            }
    data.update(update_data)
    return data
    

class Field:
    def __init__(self, config = None):
        self._data = {
            "tanks":{
                # tank_id: {tank data}
            },
            "bullets":[],
            "walls":[
                {
                    "id":1,
                    "start":{
                        "x":0,
                        "y":0
                    },
                    "end":{
                        "x": 0,
                        "y": 500
                    },
                    "width":15,
                    "weight":-1
                },
                {
                    "id":2,
                    "start":{
                        "x":0,
                        "y":500
                    },
                    "end":{
                        "x": 1000,
                        "y": 500
                    },
                    "width":15,
                    "weight":-1
                },
                {
                    "id":3,
                    "start":{
                        "x":1000,
                        "y":0
                    },
                    "end":{
                        "x": 1000,
                        "y": 500
                    },
                    "width":15,
                    "weight":-1
                },
                {
                    "id":4,
                    "start":{
                        "x":0,
                        "y":0
                    },
                    "end":{
                        "x": 1000,
                        "y": 0
                    },
                    "width":15,
                    "weight":-1
                },
            ],
            "sizes": {
                "height": 500,
                "width": 1000,
            }
        }

        self._user_control = {
            # tank_id: {tank control}
        }

        self.users = {
            # user_id: tank_id
        }

    # def add_user(self, user_id):
    #     self.users.append(user_id)
    
    # def delete_user(self, user_id):
    #     self.users.remove(user_id)

    def create_tank(self, user_id, tank_data={}):
        if self.users.get(user_id):
            raise ValueError("User with such uid already added")

        tank_id = str(uuid4())
        logger.debug("Tank created for user", user_id, "tank_id =", tank_id)
        self.users[user_id] = tank_id
        tank_data["id"] = tank_id
        tank = generate_tank_data(tank_data)
        self.set_tank_data(tank_id, tank)
        return tank
    
    def delete_tank(self, user_id):
        tank_id = self.users.get(user_id)

        if not tank_id:
            raise ValueError("No user found!")
        logger.debug("Tank deleted", user_id, "tank_id =", tank_id)

        del self.users[user_id]
        del self._data["tanks"][tank_id]


    def set_user_control(self, user_id, control_data):
        tank_id = self.users.get(user_id)

        if tank_id is not None:
            self._user_control[tank_id] = control_data

    def set_tank_data(self, tank_id, data):
        self._data["tanks"][tank_id] = data

    def get_data(self):
        return self._data

only_field = Field()