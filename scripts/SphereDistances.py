# This program will attempt to compute the average euclidean distance between
# two random points on a sphere of radius 30.

import math
import random

def spherePoint(theta, phi):
    return [ 30 * math.sin(phi) * math.cos(theta), 30 * math.sin(phi) * math.sin(theta), 30 * math.cos(phi)]

def dist(p1,p2):
    return math.sqrt( (p1[0]-p2[0])*(p1[0]-p2[0]) + (p1[1]-p2[1])*(p1[1]-p2[1]) + (p1[2]-p2[2])*(p1[2]-p2[2]) )

distList = []

##for i in range(0,100000):
##    p1 = spherePoint( random.uniform(0,2*math.pi), random.uniform(0, math.pi)  )
##    p2 = spherePoint( random.uniform(0,2*math.pi), random.uniform(0, math.pi)  )
##    distance = dist(p1,p2)
##    distList.append(distance)
### I learned something!  This code does not randomly sample points on the sphere
### because the area element sin(phi)d(phi)d(theta) depends on phi. Let's update
### this code!  Let u = -cos(phi) and do a u substitution to get area element =
### du*d(theta)

for i in range(0,2000000):
    u = random.uniform(-1,1)
    v = random.uniform(-1,1)
    p1 = spherePoint(random.uniform(0,2*math.pi), math.acos(-u) )
    p2 = spherePoint(random.uniform(0,2*math.pi), math.acos(-v) )
    distance = dist(p1,p2)
    distList.append(distance)


avg = sum(distList)/len(distList)

print(avg)
