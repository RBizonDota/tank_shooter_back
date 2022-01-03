from uuid import uuid4

from random import random

from utility.logger import Logger

from config.settings import *

logger = Logger()

def generate_tank_data(update_data):
    data = {
                "id": "askjfhaskfgajsgfsajhdvajshg",
                "size":{
                    "x":50,
                    "y":30,
                    "b_r":12, #Радиус башни
                    "w_l": 12,
                    "w_w": 4
                },
                "napr":{
                    "az":360*random(),
                    "b_az":0
                },
                "pos": {
                    "x": 100+800*random(),
                    "y":50+400*random()
                },
                "fire":{
                    "current":20
                },
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
        self.set_tank_data(tank_id, generate_tank_data(tank_data))
    
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