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

neibor_pairs = [
    ((1,1), (1,-1)),
    ((1,-1), (-1,-1)),
    ((-1,-1), (-1,1)),
    ((-1,1), (1,1))
]

def d_func(p1,p2,point):
        # A = -(y2 - y1)
        koef_a = -1*(p2[1]-p1[1])
        # B = x2 - x1
        koef_b = (p2[0]-p1[0])
        # C = -(A * x1 + B * y1)
        koef_c = -1*(koef_a*p1[0]+koef_b*p1[1])
        # D = A * xp + B * yp + C
        d = koef_a*point["x"]+koef_b*point["y"]+koef_c
        return d


def point_in_tank(point, tank):
    # print("point_in_tank", tank)
    # Если расстояние слишком велико
    max_l = math.sqrt(tank["size"]["x"]**2+tank["size"]["y"]**2)
    ro = math.sqrt((tank["pos"]["x"]-point["x"])**2+(tank["pos"]["y"]-point["y"])**2)
    # print(max_l, ro, tank["id"])
    if ro>max_l:
        return False

    # Если теоретически попадание возможно
    # Рассчет соседних точек (граней)
    # D = (x2 - x1) * (yp - y1) - (xp - x1) * (y2 - y1)
    # Если D > 0 , то точка находится с левой стороны. Если D < 0 , то точка находится с правой стороны. Если D = 0 , то точка находится на прямой.
    neibor_points = [
        (
            (tank["pos"]["x"]+i[0]*tank["size"]["x"]/2, tank["pos"]["y"]+i[1]*tank["size"]["y"]/2),
            (tank["pos"]["x"]+j[0]*tank["size"]["x"]/2, tank["pos"]["y"]+j[1]*tank["size"]["y"]/2)
        )
        for i,j in neibor_pairs
    ]

    # dd = [d_func(p1,p2,point) for p1,p2 in neibor_points]
    # print(dd)
    
    for p1,p2 in neibor_points:
        d = d_func(p1,p2,point)
        if d>0:
            return False

    
    return True


if __name__ == "__main__":
    # print(point_in_wall({"x":2, "y":1}, {
    #                 "start":{
    #                     "x":0,
    #                     "y":0
    #                 },
    #                 "end":{
    #                     "x": 500,
    #                     "y": 500
    #                 },
    #                 "width":15,
    #                 "weight":-1
                # }))

    pass