import math

def point_in_wall(point, wall):
    # print(wall["id"], abs(point["y"]-wall["end"]["y"]), wall["end"]["y"], wall["width"]/2, point)
    # Найдем вектор стены
    if (wall["end"]["x"]-wall["start"]["x"]) == 0:
        return abs(point["x"]-wall["end"]["x"])<wall["width"]/2, {"dx": abs(point["x"]-wall["end"]["x"]), "dy":0}
    if (wall["end"]["y"]-wall["start"]["y"]) == 0:
        return abs(point["y"]-wall["end"]["y"])<wall["width"], {"dx": 0, "dy": abs(point["y"]-wall["end"]["y"])}
    k = (wall["end"]["y"]-wall["start"]["y"])/(wall["end"]["x"]-wall["start"]["x"])
    b = wall["end"]["y"]-k*wall["end"]["x"]

    # найдем точку пересечения стены с перпендикуляром к ней из point
    kp = -1/k
    bp = point["y"] - kp*point["x"]
    print(f"Initial: y={k}*x+{b}")
    print(f"Perp: y={kp}*x+{bp}")
    # Решим уравнение пересечения векторов
    xp = (bp-b)/(k-kp)
    yp = kp*xp+bp
    
    print(xp, yp, math.cos(math.atan(kp)))
    
    ro = math.sqrt((yp-point["y"])**2+(xp-point["x"])**2)
    return ro<wall["width"], {"dx": abs(ro/math.cos(math.atan(kp))), "dy": abs(ro/math.sin(math.atan(kp)))}

if __name__ == "__main__":
    print(point_in_wall({"x":2, "y":1}, {
                    "start":{
                        "x":0,
                        "y":0
                    },
                    "end":{
                        "x": 500,
                        "y": 500
                    },
                    "width":15,
                    "weight":-1
                }))