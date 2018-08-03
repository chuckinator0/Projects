'''
Introduction:

This program analyzes data and provides basic security for a NASA fan-site. There are 4 major features.

Feature 1: List the top 10 most active host/IP addresses that have accessed the site.

Feature 2: Identify the 10 resources that consume the most bandwidth on the site.

Feature 3: List the top 10 busiest (or most frequently visited) 60-minute periods.

Feature 4: Detect patterns of three failed login attempts from the same IP address over 20 seconds so that all further
attempts to the site can be blocked for 5 minutes. Log those possible security breaches.

The program is organized as follows:
1. Data and Initialization
2. Functions
3. Main Program
'''

'''Data and Initialization'''

## Import modules, data from files, and create variables and data structures that will be used in the main program.


# The datetime module allows for arithmetic with dates, which will prove useful for features 3 and 4.
import datetime

import sys

# Establish filepaths for the input (log.txt) an output files (hours.txt, hosts.txt, blocked.txt, and resources.txt).
logPath = sys.argv[1]
hostsPath = sys.argv[2]
hoursPath = sys.argv[3]
resourcesPath = sys.argv[4]
blockedPath = sys.argv[5]

# Open output files for writing in the main program.
hoursFile = open(hoursPath, 'w')
hostsFile = open(hostsPath, 'w')
blockedFile = open(blockedPath, 'w')
resourcesFile = open(resourcesPath, 'w')

# Data description:
# Each line of log.txt is one long string. After splitting a line, we obtain a list of strings. Here is what each
# position in the list represents in the data.

'''
Index 0: 'host'
Index 1: '-'
Index 2: '-'
Index 3: '[DD/Mon/YYYY:HH:MM:SS' (need to splice to get rid of leading bracket)
Index 4: '-0400]' (need to splice to get rid of ending bracket)
Index 5: '"POST' or '"GET'
Index 6: 'resource' (login, load site, etc)
Index 7: 'HTTP/1.0"' (this index is sometimes omitted and I'm not sure why)
Index 8: 'reply code'
Index 9: 'bytes' in reply (where '-' means 0)
'''


# Create host dictionary of the form {host : number of accesses by host} to be used in Feature 1.
hostDict = {}

# Create resource dictionary of the form {resource : bytes over network} to be used in Feature 2.
resourceDict = {}

# Create hours.txt dictionary of the form {starting time: number of accesses to the site in the following hour}, where
# starting time is a Python datetime object. This is for Feature 3.
hoursDict = {}

# The resolution (in seconds) is the precision with which the busiest hours are defined. Setting resolution = 1 second
# gives the full functionality intended for this feature, but is highly resource intensive. I recommend setting
# resource = 600 seconds (ten minutes) for a robust metric of busy time windows at a much greater efficiency. The code
# requires the resolution to divide 3600, but if a different resolution is given, then it will be increased until it
# divides 3600.
resolution = 600
while 3600 % resolution != 0:
    resolution += 1

# Create dictionary to track failed logins for possible future blocking. The dictionary has the form
# {host: [list of times of attempted logins] }. This feature assumes the logins are processed in chronological order.
#  This is for Feature 4.
failed = {}

# Create dictionary for hosts who have violated the condition of 3 failures in 20 seconds to indicate that they should
# be blocked for the next 5 minutes. This dictionary has the form {host: cooldown time}. All attempted logins by the
# host before the cooldown time will be printed to blocked.txt. This is for Feature 4.
blocked = {}

'''Functions'''

## Define any functions that the main program requires. Calculations that need to be repeated at different points of a
## program should be coded as functions.


def topTen(dictionary):
    '''The topTen function takes a {key : value} dictionary and produces a top ten list in descending order by value.
    Each element of the top ten list has the form [key, value].
    This function will be used in features 1, 2, 3.'''
    topTen = []
    for key in dictionary:
        value = dictionary[key]
        entry = [key, value]
        if len(topTen) < 10:
            topTen.append(entry)
            continue
        # sort topTen in increasing order of value
        topTen.sort(key=lambda x: x[1])
        # set minimum number of accesses in the topTen list
        minimum = topTen[0][1]
        # replace minimum element of topTen if a bigger accessCount comes along.
        if value > minimum:
            topTen[0] = entry
    # sort topTen one last time
    topTen.sort(key=lambda x: x[1])
    # reverse topTen to give the results in descending order
    topTen.reverse()
    return topTen

def monthNumber(abbrev):
    '''monthNumber function translates the 3-letter month abbreviation to the month number. 
    This will be used for Feature 4.'''
    return {
        'Jan': 1,
        'Feb': 2,
        'Mar': 3,
        'Apr': 4,
        'May': 5,
        'Jun': 6,
        'Jul': 7,
        'Aug': 8,
        'Sep': 9,
        'Oct': 10,
        'Nov': 11,
        'Dec': 12
    }[abbrev]


def monthAbbr(number):
    '''monthAbbr translates the month number to the 3-letter month abbreviation. This will be used for Feature 4.'''
    monthlist = [
        'Jan',
        'Feb',
        'Mar',
        'Apr',
        'May',
        'Jun',
        'Jul',
        'Aug',
        'Sep',
        'Oct',
        'Nov',
        'Dec'
    ]
    return monthlist[number - 1]


def convertdatetime(line):
    '''The convertdatetime function takes a line of data and returns its associated Python datetime object.'''
    lineSplit = line.split()
    # t is the time in the data
    t = lineSplit[3]
    # splice t to get the year, month, day, hour, minute, and second.
    return datetime.datetime(
        year=int(t[8:12]),
        month=monthNumber(t[4:7]),
        day=int(t[1:3]),
        hour=int(t[13:15]),
        minute=int(t[16:18]),
        second=int(t[19:21])
    )

def convertHours(time):
    '''The convertHours function converts a datetime object to the specified output format for hours.txt.'''
    timestr = str(time)
    year = timestr[0:4]
    month = monthAbbr(int(timestr[5:7]))
    day = timestr[8:10]
    hour = timestr[11:13]
    minute = timestr[14:16]
    second = timestr[17:19]
    return day + '/' + month + '/' + year + ':' + hour + ':' + minute + ':' + second

def roundDown(time, resolution):
    '''
    roundDown rounds a datetime down accoridng to the resolution. If the resolution is 1 second, there is no rounding.
    If the resolution is 600 seconds, the time is rounded down to the last multiple of 10 minutes. If the resolution 
    is 3600 seconds, the time is rounded down to the last hour.
    '''
    modtime = (int(time.minute) * 60 + int(time.second)) % resolution
    roundedtime = time - datetime.timedelta(seconds=modtime)
    return roundedtime

def feature1(line):
    '''This function produces a dictionary {hosts: number of accesses by host} (see hostDict)'''
    lineSplit = line.split()
    host = lineSplit[0]
    # if new host is already in the dictionary, add 1 to the number of accesses.
    if host in hostDict:
        hostDict[host] += 1
    # if new host is not in the dictionary yet, put it in the dictionary and set number of accesses to 1
    else:
        hostDict[host] = 1

def feature2(line):
    '''This function produces a dictionary {resource: data} (see resourceDict)'''
    lineSplit = line.split()
    # ignore 404 errors that give '-' for bytes
    if lineSplit[-1] != '-':
        resource = lineSplit[6]
        dataBytes = int(lineSplit[-1])
        if resource in resourceDict:
            resourceDict[resource] += dataBytes
        else:
            resourceDict[resource] = dataBytes

def feature3(line, resolution):
    '''
    The resolution (in seconds) is the precision with which the busiest hours are defined. Setting resolution = 1 second
    gives the full functionality intended for this feature, but is highly resource intensive. I recommend setting
    resource = 600 seconds (ten minutes) for a robust metric of busy time windows at a much greater efficiency. The code
    requires the resolution to divide 3600, but if a different resolution is given, then it will be increased until it 
    divides 3600.
    '''
    time = convertdatetime(line)
    roundedtime = roundDown(time, resolution)
    if roundedtime not in hoursDict:
        hoursDict[roundedtime] = 1
    else:
        hoursDict[roundedtime] += 1
    x = roundedtime - datetime.timedelta(seconds=resolution)
    while x > time - datetime.timedelta(hours=1):
        if x in hoursDict:
            hoursDict[x] += 1
        x = x - datetime.timedelta(seconds=resolution)

def feature4(line):
    '''This function blocks users who fail on login 3 times in 20 seconds and puts them on a 5 minute cooldown.'''
    lineSplit = line.split()
    resource = lineSplit[6]
    if resource == '/login':
        host = lineSplit[0]
        time = convertdatetime(line)
        replyCode = lineSplit[-2]
        if host in blocked:
            if time > blocked[host]:
                del failed[host]
                del blocked[host]
            else:
                print(line, file=blockedFile)
                return
        if replyCode == '401':
            if host in failed:
                failed[host].append(time)
                if len(failed[host]) > 3:
                    del failed[host][0]
            else:
                failed[host] = []
                failed[host].append(time)
            if len(failed[host]) >= 3 and failed[host][-1] - failed[host][-3] < datetime.timedelta(seconds=20):
                cooldowntime = time + datetime.timedelta(minutes=5)
                blocked[host] = cooldowntime
        elif replyCode == '200':
            if host in failed:
                del failed[host]
            if host in blocked:
                del blocked[host]


'''Main Program'''

## Perform relevant computations, using functions as needed

with open(logPath, 'r', errors='ignore') as logFile:
    for line in logFile:
        feature1(line)
        feature2(line)
        feature3(line, resolution)
        feature4(line)

# create a topTen list of hosts in descending order by number of accesses
topHosts = topTen(hostDict)
# output to hosts.txt
for x in topHosts:
    print(x[0] + ',' + str(x[1]), file=hostsFile)

# Create a topTen list of resources in descending order by bytes.
topResources = topTen(resourceDict)
# Output to resources.txt
for x in topResources:
    print(x[0], file=resourcesFile)

# Make topTen list of busiest 1-hour windows
topHours = topTen(hoursDict)
# Output to hours.txt
for i in topHours:
    print(convertHours(i[0]) + ' -0400,' + str(i[1]), file=hoursFile)

'''Close output files'''
hoursFile.close()
hostsFile.close()
blockedFile.close()
resourcesFile.close()
