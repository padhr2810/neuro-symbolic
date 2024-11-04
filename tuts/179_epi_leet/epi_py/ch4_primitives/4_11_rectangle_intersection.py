"""
TRICK #1: CHECK VS. OPPOSITE ENDS. 
I.E. CHECK IF START OF R1 IS <= END OF R2.
AND CHECK IF END OF R1 IS >= MIN OF R2.

TRICK #2: RETURN THE COORDINATES OF RECTANGLE FORMED BY INTERSECTION OF 2 INPUTTED RECTANGLES.
I.E. MAX OF THE STARTING POINTS AND MIN OF THE END POINTS, THIS GIVES THE INTERSECTION RECT.
"""

import collections


Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))


def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1, r2):
        print(f"r1.x = {r1.x}")
        print(f"r2.x = {r2.x}")
        print(f"r2.width = {r2.width}")
        print(f"r1.x = {r1.x}")
        print(f"r1.width = {r1.width}")
        
        print(f"r1 = {r1}")
        print(f"r2 = {r2}")
        return (r1.x <= r2.x + r2.width and r1.x + r1.width >= r2.x
                and r1.y <= r2.y + r2.height and r1.y + r1.height >= r2.y)

    if not is_intersect(r1, r2):
        return Rect(0, 0, -1, -1)  # No intersection.
    return Rect(max(r1.x, r2.x), max(r1.y, r2.y),
                min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
                min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y))


def intersect_rectangle_wrapper(r1, r2):
    return intersect_rectangle(Rect(*r1), Rect(*r2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value

r1 = Rect(0.1, 1.4, 2, 3)
r2 = Rect(0.6, 1.5, 2, 3)
print(f"result = {intersect_rectangle(r1, r2)}")


