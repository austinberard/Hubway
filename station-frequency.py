#!/usr/bin/env python3

__author__ = 'Austin'
import csv
import operator


with open("hubway_trips.csv") as csvfile:
    readCSV = csv.reader(csvfile, delimiter=",")
    stationCount = {}
    for i in readCSV:
        station = i[5]
        if station in stationCount:
            stationCount[station] += 1
        else:
            stationCount[station] = 1
    for key, value in sorted(stationCount.items(), key=operator.itemgetter(1)):
        print(key, value)

with open("hubway_trips.csv") as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter=",")
    endStationCount = {}
    for j in readCSV2:
        end = j[7]
        if end in endStationCount:
            endStationCount[end] += 1
        else:
            endStationCount[end] = 1
    for key, value in sorted(endStationCount.items(), key=operator.itemgetter(1)):
        print(key, value)