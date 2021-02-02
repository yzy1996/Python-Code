# 解算出两线段的交点
# 采用 一点和斜率，然后两直线求解


class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# 用"一点和斜率"定义的直线
class Line(object):
    def __init__(self, p, k):
        self.p = p
        self.k = k


# 解两直线的交点
def get_cross_point(l1, l2):
    cross_point = Point()
    cross_point.x = (l2.p.y + l1.p.y - l2.k * l2.p.x - l1.k * l1.p.x) * 1.0 / (
        l1.k - l2.k)
    cross_point.y = (l1.k * (l2.p.y - l2.k * l2.p.x) - l2.k *
                     (l1.p.y - l1.k * l1.p.x)) * 1.0 / (l1.k - l2.k)
    return cross_point


if __name__ == '__main__':
    p1 = Point(1, 1)
    k1 = 1
    line1 = Line(p1, k1)

    p2 = Point(1, 1)
    k2 = -1
    line2 = Line(p2, k2)

    cross_point = get_cross_point(line1, line2)
    print("Cross point:", cross_point.x, cross_point.y)
