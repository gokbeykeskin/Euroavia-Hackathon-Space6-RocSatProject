import csv
from mpl_toolkits.basemap import Basemap
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

def start2dMap():

    # setup mercator map projection.

    prevLat = 0
    prevLong = 0
    plt.figure()
    map = Basemap()

    # nylat, nylon are lat/lon of New York
    nylat = 38; nylon = 26
    # lonlat, lonlon are lat/lon of London.
    lonlat = 40; lonlon = 45
    # draw great circle route between NY and London
    #map.drawgreatcircle(nylon,nylat,lonlon,lonlat,linewidth=2,color='b')
    map.drawcoastlines()
    map.drawmapboundary(fill_color='aqua')
    map.fillcontinents(color='coral',lake_color='aqua')
    map.drawcountries()
    # draw parallels
    map.drawparallels(np.arange(10,90,20),labels=[1,1,0,1])
    # draw meridians
    map.drawmeridians(np.arange(-180,180,30),labels=[1,1,0,1])


    time, altitude, vertV, vertA, totalV, totalA, lateralV, lateralA = [], [], [], [], [], [], [], []
    latitude, longitude, rollRate, pitchRate, yawRate, mass, thrust = [], [], [], [], [], [], []
    dragForce, windV, airTemp, airPres, comment, commentTimes = [], [], [], [], [], []


    with open("Flight_data_3.csv", mode='r', errors='ignore') as file:
        # Reading the file
        csvFile = csv.reader(file)

        ignoreCount = 0
        array = []

        for line in csvFile:

            if("#" not in line[0][0]):
                time.append(line[0]), altitude.append(line[1])
                vertV.append(line[2]), vertA.append(line[3])
                totalV.append(line[4]), totalA.append(line[5])
                lateralV.append(line[6]), lateralA.append(line[7])
                latitude.append(line[8]), longitude.append(line[9])
                rollRate.append(line[10]), pitchRate.append(line[11])
                yawRate.append(line[12]), mass.append(line[13])
                thrust.append(line[14]), dragForce.append(line[15])
                windV.append(line[16]), airTemp.append(line[17])
                airPres.append(line[18])
            elif(ignoreCount >= 4):
                comment.append(line[0][2:])
                commentTimes.append(comment[-1].split(" ")[4][2:])

            ignoreCount += 1

        cmtIndex = 2

        print(comment[0] + "\n" + comment[1])
        x = 0
        for attrIndex in range (len(time)):
            if(time[attrIndex] == commentTimes[cmtIndex]):
                print(comment[cmtIndex])
                cmtIndex += 1
            
            print("Time: " + time[attrIndex])
            print("------------")
            print("Altitude:\t\t " + altitude[attrIndex])
            print("Vertical Velocity:\t", vertV[attrIndex])
            print("Vertical Acceleration:\t", vertA[attrIndex])
            print("Total Velocity:\t\t", totalV[attrIndex])
            print("Total Acceleration:\t", totalA[attrIndex])
            print("Lateral Velocity:\t", lateralV[attrIndex])
            print("Lateral Acceleration:\t", lateralA[attrIndex])
            print("Latitude:\t\t", latitude[attrIndex])
            print("Longitude:\t\t", longitude[attrIndex])
            print("Roll Rate:\t\t", rollRate[attrIndex])
            print("Pitch Rate:\t\t", pitchRate[attrIndex])
            print("Yaw Rate:\t\t", yawRate[attrIndex])
            print("Mass:\t\t\t", mass[attrIndex])
            print("Thrust:\t\t\t", thrust[attrIndex])
            print("Drag Force:\t\t", dragForce[attrIndex])
            print("Wind Velocity:\t\t", windV[attrIndex])
            print("Air Temperature:\t", airTemp[attrIndex])
            print("Air Pressure:\t\t", airPres[attrIndex], "\n\n")
            map.plot(float(longitude[attrIndex]), float(latitude[attrIndex]), marker='D',color='m')
            print(float(longitude[attrIndex]), float(latitude[attrIndex]))
            flag = False
            if(prevLat!=latitude[attrIndex] or prevLong != longitude[attrIndex]):
                y_min = float(latitude[attrIndex]) - 0.01
                y_max = float(latitude[attrIndex]) + 0.01
                x_max = float(longitude[attrIndex]) + 0.01
                x_min = float(longitude[attrIndex]) - 0.01

                flag = True
            else:
                y_min = float(latitude[attrIndex]) - 5
                y_max = float(latitude[attrIndex]) + 5
                x_max = float(longitude[attrIndex]) + 8
                x_min = float(longitude[attrIndex]) - 8
                flag = False
            prevLat = latitude[attrIndex]
            prevLong = longitude[attrIndex]

            plt.axis([x_min, x_max, y_min, y_max])
            plt.show(block=False)
            if(flag== True):
                plt.pause(3)
            plt.pause(0.00000001)
