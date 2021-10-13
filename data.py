import csv

time, altitude, vertV, vertA, totalV, totalA, lateralV, lateralA = [], [], [], [], [], [], [], []
latitude, longitude, rollRate, pitchRate, yawRate, mass, thrust = [], [], [], [], [], [], []
dragForce, windV, airTemp, airPres, comment, commentTimes = [], [], [], [], [], []


def parse_data(filename):

    with open(filename, mode='r') as file:
        # Reading the file
        csvFile = csv.reader(file)
        lineNum=csvFile.line_num
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