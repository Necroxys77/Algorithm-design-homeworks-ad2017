import math

class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

def getBoundingBoxSize(A):
    x_max = x_min = A[0].x
    y_max = y_min = A[0].y
    for point in A[1:]:
        if point.x > x_max:
            x_max = point.x
        if point.x < x_min:
            x_min = point.x
        if point.y > y_max:
            y_max = point.y
        if point.y < y_min:
            y_min = point.y
    h = y_max - y_min
    w = x_max - x_min
    return h,w

def getApproximateDiameter(h,w):
    approximateDiameter = 0
    if h>w:
        approximateDiameter = h
    else:
        approximateDiameter = w
    return approximateDiameter

#assuming five points in the 2dimensional space
p1 = Point(0,2)
p2 = Point(2,3)
p3 = Point(1,1)
p4 = Point(1,4)
p5 = Point(7,3)

A = [p1,p2,p3,p4,p5]

h,w = getBoundingBoxSize(A)

approximateDiameter = getApproximateDiameter(h,w)
print "Output: " + str(approximateDiameter)

