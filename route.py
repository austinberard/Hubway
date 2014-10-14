#!/usr/bin/env python3
__author__ = 'Austin'
import sys
import csv
import random
import math

stations = []
with open("hubway_stations.csv") as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter = ",")
    for rows in readCSV2:
        if rows[0] != 'id':     # Skip first line
            stations.append([float(rows[4]), float(rows[5])])

start = [random.uniform(42.309467, 42.40449),
         random.uniform(-71.035705, -71.146452)]

finish = [random.uniform(42.309467, 42.40449),
          random.uniform(-71.035705, -71.146452)]
          

# See: http://www.johndcook.com/python_longitude_latitude.html
def distance(p1, p2):
    lat1 = p1[0]
    lng1 = p1[1]

    lat2 = p2[0]
    lng2 = p2[1]
    dis = math.sqrt(((lat2 - lat1) ** 2) + ((lng2 - lng1) ** 2))
    return dis

distance([42.33363229107746, -71.06051998544072],
         [42.340575044581286, -71.10821497085833])

distance(start, finish)

def nearest(origin, pts):
    closest = None
    smallest_distance = sys.float_info.max
    for pt in pts:
        d = distance(origin, pt)
        if d < smallest_distance:
            closest = pt
            smallest_distance = d
    return closest


station1 = nearest(start, stations)
station2 = nearest(finish, stations)

def print_directions(start, station1, station2, end):
    print("Walk %0.2fkm to %s" % (distance(start, station1), station1))
    print("Bike %0.2fkm to %s" % (distance(station1, station2), station2))
    print("Walk %0.2fkm to %s" % (distance(station2, finish), finish))

print_directions(start, station1, station2, finish)

# Then try comparing several routes using sets of start and end stations
#for station1 in startstations:
#    for station2 in endstations:
#        print_directions(start, station1, station2, finish)
