#!/usr/bin/env python3
__author__ = 'Austin'
import datetime
from flow import *
import sys

# Create training sets and held sets with things like this:
# ./sample.py 100 > samples.txt || python sample.py 10 > samples.txt
# wc -l samples (to find out how many lines) ||  Get-Content C:\Users\Austin\Fastest-Route\samples.txt | Measure-Object -Line
# head -LINES > training-set.txt || (Get-Content C:\Users\Austin\Fastest-Route\samples.txt)[0 .. 364] > training-set.txt
# tail -LINES > held-set.txt || (Get-Content C:\Users\Austin\Fastest-Route\samples.txt)[-1 .. -365] > held-set.txt
# python predict.py training-set.txt held-set.txt
tempReal = ['46', '45', '34', '32', '34', '27', '29', '30', '30', '29', '26', '32', '26', '22', '24', '28', '18', '29', '36', '29', '26', '22', '15', '6', '22', '25', '30', '26', '32', '31', '21', '19', '28', '24', '25', '30', '39', '36', '28', '22', '24', '21', '30', '30', '44', '28', '30', '48', '49', '33', '27', '22', '26', '32', '34', '35', '33', '27', '36', '35', '36', '21', '29', '42', '54', '43', '32', '33', '38', '46', '45', '43', '37', '36', '39', '50', '58', '42', '35', '38', '40', '36', '35', '38', '34', '36', '38', '41', '45', '39', '37', '45', '48', '44', '50', '45', '40', '42', '48', '53', '60', '57', '46', '54', '42', '41', '55', '53', '47', '44', '49', '44', '47', '65', '52', '50', '63', '66', '67', '55', '51', '53', '63', '58', '54', '59', '61', '53', '60', '54', '57', '56', '53', '52', '54', '49', '50', '52', '56', '58', '56', '51', '58', '73', '68', '69', '76', '68', '76', '76', '69', '73', '67', '63', '58', '56', '63', '71', '73', '81', '69', '60', '56', '59', '58', '63', '75', '70', '74', '74', '73', '71', '68', '62', '59', '59', '69', '72', '74', '77', '74', '72', '71', '75', '80', '78', '82', '79', '72', '77', '76', '81', '86', '77', '68', '72', '75', '82', '81', '80', '81', '85', '92', '82', '76', '69', '72', '76', '72', '73', '81', '81', '83', '79', '70', '72', '71', '79', '74', '75', '73', '72', '73', '74', '74', '73', '66', '68', '75', '78', '80', '78', '78', '74', '71', '73', '78', '77', '75', '72', '71', '70', '72', '67', '64', '73', '77', '78', '67', '62', '61', '70', '65', '63', '72', '75', '77', '69', '58', '55', '59', '58', '61', '67', '69', '69', '73', '73', '71', '69', '67', '67', '68', '64', '62', '62', '62', '60', '57', '54', '69', '76', '75', '62', '60', '61', '63', '62', '60', '61', '62', '57', '62', '59', '57', '52', '53', '56', '49', '42', '42', '42', '41', '45', '47', '47', '53', '46', '43', '48', '54', '60', '57', '56', '50', '45', '53', '61', '62', '55', '48', '41', '45', '58', '48', '40', '41', '39', '49', '54', '47', '60', '59', '54', '44', '43', '40', '44', '54', '55', '52', '42', '44', '39', '33', '40', '38', '40', '46', '48', '35', '24', '32', '39', '45', '51', '42', '27', '31', '37', '43', '43', '28', '36', '37', '46', '42', '25', '19', '32', '38', '45', '38', '33', '39', '34', '38', '43', '27', '13', '22', '41', '37', '25', '27', '20', '23', '38', '49', '40', '36', '42', '42', '39', '36', '39', '47', '38', '32', '36', '29', '39', '38', '30', '39', '40', '35', '23', '29', '36', '39', '40', '46', '41', '39', '35', '36', '47', '48', '39', '39', '34', '39', '41', '34', '31', '29', '41', '38', '32', '30', '47', '59', '48', '36', '44', '57', '60', '49', '40', '42', '45', '58', '60', '56', '67', '70', '67', '53', '45', '41', '38', '45', '43', '44', '40', '43', '46', '48', '54', '46', '45', '45', '46', '51', '53', '49', '50', '53', '60', '66', '73', '71', '56', '57', '63', '66', '53', '54', '52', '53', '53', '49', '49', '49', '48', '48', '49', '48', '53', '54', '50', '54', '54', '60', '59', '56', '65', '70', '59', '65', '67', '62', '57', '59', '63', '57', '60', '65', '66', '66', '76', '68', '65', '63', '68', '73', '62', '59', '58', '52', '53', '57', '60', '67', '69', '68', '66', '67', '64', '65', '63', '60', '58', '60', '66', '82', '88', '85', '73', '74', '67', '67', '69', '74', '78', '80', '81', '77', '77', '76', '77', '74', '80', '80', '76', '74', '73', '75', '80', '82', '82', '80', '87', '80', '70', '68', '68', '73', '76', '80', '74', '75', '72', '68', '69', '72', '68', '73', '77', '82', '78', '80', '78', '72', '75', '76', '77', '76', '78', '79', '77', '75', '76', '76', '68', '67', '69', '75', '72', '77', '73', '72', '70', '74', '77', '69', '72', '79', '72', '68', '66', '68', '74', '72', '75', '76', '69', '63', '63', '63', '71', '71', '67', '63', '62', '67', '64', '57', '57', '62', '64', '59', '61', '67', '62', '56', '56', '56', '59', '64', '62', '61', '67', '66', '53', '51', '56', '57', '52', '47', '44', '57', '67', '54', '49', '52', '61', '66', '57', '60', '59', '51', '52', '57', '55', '54', '57', '58', '52', '51', '49', '48', '46', '39', '36', '39', '36', '46', '48', '51', '57', '52', '41', '38', '40', '42', '40', '41', '41', '44', '45', '43', '41', '36', '40', '37', '34', '38', '34', '30', '42', '50', '48', '45', '36', '37', '45', '45', '51', '45', '36', '36', '40', '37', '37', '41', '46', '42', '38', '45', '34', '34', '36', '32', '31', '39', '33', '33', '26', '28', '29', '21', '16', '30', '35', '36', '34', '37', '37', '41', '36', '41', '46', '52', '39', '33', '36', '25', '37', '42', '27', '20', '13', '13', '17', '19', '23', '26', '31', '47', '46', '29', '25', '25', '27', '25', '33', '24', '27', '18', '26', '33', '40', '36', '37', '39', '35', '25', '25', '36', '35', '29', '32', '35', '34', '35', '35', '39', '39', '38', '38', '38', '36', '38', '38', '34', '35', '35', '33', '43', '46', '45', '31', '31', '35', '32', '27', '32', '33', '33', '35', '37', '41', '39', '42', '46', '43', '48', '47', '47', '49', '37', '39', '44', '48', '40', '43', '55', '59', '50', '46', '41', '44', '49', '44', '52', '57', '54', '64', '55', '44', '43', '42', '56', '57', '48', '49', '54', '58', '54', '53', '53', '49', '48', '47', '49', '60', '60', '58', '63', '66', '62', '53', '52', '56', '68', '62', '59', '57', '69', '59', '56', '65', '61', '48', '51', '60', '58', '64', '77', '83', '81', '78', '70', '64', '65', '63', '57', '67', '71', '64', '60', '64', '60', '64', '71', '69', '75', '65', '65', '68', '73', '75', '79', '83', '81', '74', '64', '72', '77', '77', '78', '72', '77', '85', '87', '86', '84', '76', '69', '77', '78', '70', '69', '81', '83', '84', '84', '84', '89', '88', '74', '72', '75', '77', '63', '67', '73', '71', '74', '75', '74', '74', '76', '74', '74', '70', '67', '70', '73', '74', '76', '72', '75', '70', '70', '69', '71', '69', '71', '74', '78', '78', '80', '72', '66', '72', '76', '71', '67', '65', '74', '76', '75', '75', '75', '73', '64', '62', '68', '67', '62', '68', '83', '78', '69', '63', '64', '60', '52', '63', '63', '63', '67', '64', '58', '58', '58', '59', '62', '62', '57', '58', '64', '72', '70', '63', '64', '59', '69', '60', '55', '55', '59', '57', '55', '53', '58', '57', '64', '63', '59', '57', '57', '60', '50', '50', '46', '47', '51', '50', '46', '46', '52', '66', '58', '44', '37', '40', '52', '56', '44', '41', '50', '47', '40', '32', '41', '50', '50', '47', '59', '41', '36', '39', '45', '41', '26', '26', '38', '51', '33', '29', '28', '41', '39', '43', '40', '47', '46', '37', '30', '37', '33', '28', '23', '23', '21', '31', '25', '19', '28', '35', '42', '48', '45', '37', '34', '22', '29', '32', '38', '39', '32', '20']
precipReal = ['0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '0', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '0', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '1', '0', '1', '1', '1', '1', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '1', '1', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '1', '0', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '1', '0', '0', '1', '0', '0', '0', '1', '0', '1', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '1', '1', '0', '1', '1', '0', '0', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '1', '1', '1', '1', '0', '0', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '1', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '1', '1', '0', '1', '1', '0', '0', '1', '1', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '1', '1', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '0', '0', '1', '1', '1', '0', '1', '0', '0', '0', '1', '0', '0', '1', '0', '1', '0', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '1', '1', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '1', '1', '0', '0', '1', '0', '0', '1', '0', '0']

def temp(datetime):
    doy = datetime.timetuple().tm_yday
    if datetime.year == 2011:
        return tempReal[doy - 1]
    elif datetime.year == 2012:
        return tempReal[364 + doy]
    else:
        return tempReal[728 + doy]

def precip(datetime):
    doy = datetime.timetuple().tm_yday
    if datetime.year == 2011:
        return precipReal[doy - 1]
    elif datetime.year == 2012:
        return precipReal[364 + doy]
    else:
        return precipReal[728 + doy]


if __name__ == "__main__":
    allFlow = Flow()
    for stime, sstation, etime, estation in hubway.trips():
        allFlow.countStart(sstation)
        allFlow.countEnd(estation)
    avgFlow = allFlow / (365 * 3 * 24)

    DAYS = int(sys.argv[1])
    sample_trips = random.sample(hubway.trips(), DAYS)

    for trip in sample_trips:
        dt = trip[0]

        year = dt.year
        doy = dt.timetuple().tm_yday
        dow = dt.weekday()
        hour = dt.hour
        isWkEnd = 1 if weekend(dt) else 0
        temperature = temp(dt)
        precipitation = precip(dt)
        forHour = Flow.forHour(dt)
        for station, value in enumerate(allFlow.outbound):
            print(", ".join([str(e) for e in [year, doy, dow, hour, isWkEnd, station, temperature, precipitation, forHour.outgoing(station)]]))


