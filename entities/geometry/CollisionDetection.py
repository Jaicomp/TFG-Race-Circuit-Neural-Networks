from typing import List

# habia esto
#Shape from entities.geometry import Shape, Point2D, Triangle

# si lo cambio por esto funciona
from entities.geometry.Shape import Shape
from entities.geometry.Point2D import Point2D
from entities.geometry.Triangle import Triangle


def are_colliding(shape1: Shape, shape2: Shape) -> bool:
    if not shape1.overlaps(shape2):
        return False
    direction = Point2D(1, 1)
    c = _support(direction, shape1, shape2)
    simplex = [c]
    direction = -c
    origin = Point2D(0, 0)
    step = 1
    while True:
        b = _support(direction, shape1, shape2)
        if b.dot_product(direction) < 0:
            return False
        simplex.append(b)
        if len(simplex) == 3:
            if Triangle(simplex[0], simplex[1], simplex[2]).contains(origin):
                return True
        simplex, direction = _do_simplex(simplex)
        step += 1
        if step > 1000:
            return False


def _support(direction: Point2D, s1: Shape, s2: Shape) -> Point2D:
    s1_furthest_point = _furthest_point(direction, s1.points)
    s2_furthest_point = _furthest_point(-direction, s2.points)
    return s1_furthest_point - s2_furthest_point


def _furthest_point(direction: Point2D, points: List[Point2D]) -> Point2D:
    max_dot = 0.0
    furthest = None
    for point in points:
        current_dot = direction.dot_product(point)
        if current_dot > max_dot or furthest is None:
            max_dot = current_dot
            furthest = point
    return furthest


def _do_simplex(simplex: List[Point2D]) -> (List[Point2D], Point2D):
    if len(simplex) == 2:
        return _do_2_simplex(simplex)
    else:
        return _do_3_simplex(simplex)


def _do_2_simplex(simplex: List[Point2D]) -> (List[Point2D], Point2D):
    b = simplex[0]
    a = simplex[1]
    ab = b - a
    ao = -a
    if ab.dot_product(ao) > 0:
        new_simplex = [a, b]
        new_direction = _triple_product_expansion(ab, ao, ab)
    else:
        new_simplex = [a]
        new_direction = ao
    return new_simplex, new_direction


def _do_3_simplex(simplex: List[Point2D]) -> (List[Point2D], Point2D):
    c = simplex[0]
    b = simplex[1]
    a = simplex[2]
    ab = b - a
    ac = c - a
    ao = -a
    if _triple_product_expansion(ac, ac, ab).dot_product(ao) > 0 and ac.dot_product(ao) > 0:
        new_simplex = [a, c]
        new_direction = _triple_product_expansion(ac, ao, ac)
    else:
        if ab.dot_product(ao) > 0:
            new_simplex = [a, b]
            new_direction = _triple_product_expansion(ab, ao, ab)
        else:
            new_simplex = [a]
            new_direction = ao
    return new_simplex, new_direction


def _triple_product_expansion(v1: Point2D, v2: Point2D, v3: Point2D) -> Point2D:
    return v2.mul_by_value(v1.dot_product(v3)) - v3.mul_by_value(v1.dot_product(v2))


def line_intersection(p1: Point2D, p2: Point2D, p3: Point2D, p4: Point2D):
    xdiff = Point2D(p1.x - p2.x, p3.x - p4.x)
    ydiff = Point2D(p1.y - p2.y, p3.y - p4.y) #Typo was here

    def det(a, b):
        return a.x * b.y - a.y * b.x

    div = det(xdiff, ydiff)
    if div == 0:
       return None

    d = Point2D(det(p1, p2), det(p3, p4))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return Point2D(x, y)


def segment_intersection(p1: Point2D, p2: Point2D, p3: Point2D, p4: Point2D):
    # deben coincidir los cuadrantes
    if max(p1.x, p2.x) < min(p3.x, p4.x):
        return None
    if min(p1.x, p2.x) > max(p3.x, p4.x):
        return None
    if max(p1.y, p2.y) < min(p3.y, p4.y):
        return None
    if min(p1.y, p2.y) > max(p3.y, p4.y):
        return None

    intersection = line_intersection(p1, p2, p3, p4)
    if intersection is not None:
        epsilon = 0.001
        if ((p1.x - epsilon <= intersection.x <= p2.x + epsilon or p2.x - epsilon <= intersection.x <= p1.x + epsilon) and
                (p1.y - epsilon <= intersection.y <= p2.y + epsilon or p2.y - epsilon <= intersection.y <= p1.y + epsilon)):
            if ((p3.x - epsilon <= intersection.x <= p4.x + epsilon or p4.x - epsilon <= intersection.x <= p3.x + epsilon) and
                    (p3.y - epsilon <= intersection.y <= p4.y + epsilon or p4.y - epsilon <= intersection.y <= p3.y + epsilon)):
                return intersection
    return None

def inside_polygon(p: Point2D, points: List[Point2D]) -> bool:
    """
    Return True if a coordinate (x, y) is inside a polygon defined by
    a list of verticies [(x1, y1), (x2, x2), ... , (xN, yN)].

    Reference: http://www.ariel.com.au/a/python-point-int-poly.html
    """
    n = len(points)
    inside = False
    p1 = points[0]
    for i in range(1, n + 1):
        p2 = points[i % n]
        if p.y > min(p1.y, p2.y):
            if p.y <= max(p1.y, p2.y):
                if p.x <= max(p1.x, p2.x):
                    if p1.y != p2.y:
                        xinters = (p.y - p1.y) * (p2.x - p1.x) / (p2.y - p1.y) + p1.x
                    if p1.x == p2.x or p.x <= xinters:
                        inside = not inside
        p1 = p2
    return inside
