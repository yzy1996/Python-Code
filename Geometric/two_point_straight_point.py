# 解算出两线段的交点
# 采用 两点确定一条直线，然后两直线求解


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# 用"两点"定义的直线
class Line(object):
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2


# 求直线的参数，
def get_line_parameter(line):
    line.a = line.p1.y - line.p2.y
    line.b = line.p2.x - line.p1.x
    line.c = line.p1.x * line.p2.y - line.p2.x * line.p1.y


# 解两直线的交点
def get_cross_point(l1, l2):
    get_line_parameter(l1)
    get_line_parameter(l2)
    d = l1.a * l2.b - l2.a * l1.b
    cross_point = Point()
    cross_point.x = (l1.b * l2.c - l2.b * l1.c) * 1.0 / d
    cross_point.y = (l1.c * l2.a - l2.c * l1.a) * 1.0 / d
    return cross_point


if __name__ == '__main__':
    p1 = Point(0, 1)
    p2 = Point(1, 1)
    line1 = Line(p1, p2)

    p3 = Point(1, 1)
    p4 = Point(1, 0)
    line2 = Line(p3, p4)

    cross_point = get_cross_point(line1, line2)
    print("Cross point:", cross_point.x, cross_point.y)
