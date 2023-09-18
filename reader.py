filepath = "/Users/henryham/Desktop/Coding Projects/TimbyTips/timbytips.txt"

totalMade = 0
numEntries = 0

ratingSum = 0

wkdaySums = [0]*7
wkdayCounts = [0]*7
wkdayKey = {"sun":0, "mon":1, "tue":2, "wed":3, "thu":4, "fri":5, "sat":6}
revWkdayKey = {0:"sun", 1:"mon", 2:"tue", 3:"wed", 4:"thu", 5:"fri", 6:"sat"}

sumAm = 0
countAm = 0
sumPm = 0
countPm = 0

with open(filepath, "r") as file:
    for line in file:
        values = line.split(",")

        if (values[3] == 'am'):
            sumAm += int(values[2])
            countAm += 1
        elif (values[3] == 'pm'):
            sumPm += int(values[2])
            countPm += 1

        day = wkdayKey[values[1]]
        wkdaySums[day] += int(values[2])
        wkdayCounts[day] += 1
        
        totalMade = totalMade + int(values[2])
        numEntries += 1

        ratingSum = ratingSum + int(values[4])
    print(totalMade, "made in", numEntries, "shifts\n")
    avgShift = (totalMade/numEntries).__round__(2)
    avgAm = (sumAm/countAm).__round__(2)
    avgPm = (sumPm/countPm).__round__(2)
    print("averaging...\n", avgShift, "per shift\n", avgAm, "per am shift\n", avgPm, "per pm shift\n")
    for i in range(7):
        print(revWkdayKey[i]+":", (wkdaySums[i]/wkdayCounts[i]).__round__(2), wkdayCounts[i])
    
    avgRating = (ratingSum/numEntries).__round__(1)
    print("\navg rating:", avgRating)
