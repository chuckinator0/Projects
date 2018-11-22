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
from datetime import datetime, timedelta
import re
import sys

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

def convertdatetime(line):
    '''The convertdatetime function takes a line of data and returns its associated Python datetime object.'''
    lineSplit = line.split()
    return parseDateTime(lineSplit[3])

def parseDateTime(t):
    # [01/Jul/1995:00:00:59
    return datetime.strptime(t, "[%d/%b/%Y:%H:%M:%S")

def convertHours(time):
    '''The convertHours function converts a datetime object to the specified output format for hours.txt.'''
    return datetime.strftime(time, "%d/%b/%Y:%H:%M:%S")

def roundDown(dt):
    return dt.replace(minute=0, second=0)

def feature1(entry):
    '''This function produces a dictionary {hosts: number of accesses by host} (see hostDict)'''
    # if new host is already in the dictionary, add 1 to the number of accesses.
    if entry.host in hostDict:
        hostDict[entry.host] += 1
    # if new host is not in the dictionary yet, put it in the dictionary and set number of accesses to 1
    else:
        hostDict[entry.host] = 1

def feature2(entry):
    '''This function produces a dictionary {resource: data} (see resourceDict)'''
    if entry.resource in resourceDict:
        resourceDict[entry.resource] += entry.contentLength
    else:
        resourceDict[entry.resource] = entry.contentLength

def feature3(entry):
    # Calculate busiest hours
    roundedtime = roundDown(entry.timestamp)
    if roundedtime not in hoursDict:
        hoursDict[roundedtime] = 1
    else:
        hoursDict[roundedtime] += 1

def feature4(entry):
    '''This function blocks users who fail on login 3 times in 20 seconds and puts them on a 5 minute cooldown.'''
    if entry.resource == '/login':
        if entry.host in blocked:
            if entry.timestamp > blocked[entry.host]:
                del failed[entry.host]
                del blocked[entry.host]
            else:
                print(entry.line, file=blockedFile)
                return
        if entry.statusCode == '401':
            if entry.host in failed:
                failed[entry.host].append(entry.timestamp)
                if len(failed[entry.host]) > 3:
                    del failed[entry.host][0]
            else:
                failed[entry.host] = []
                failed[entry.host].append(entry.timestamp)
            if is_blocked(entry.host):
                cooldowntime = entry.timestamp + timedelta(minutes=5)
                blocked[entry.host] = cooldowntime
        elif entry.statusCode == '200':
            if entry.host in failed:
                del failed[host]
            if entry.host in blocked:
                del blocked[host]

def is_blocked(host):
    return len(failed[host]) >= 3 and failed[host][-1] - failed[host][-3] < timedelta(seconds=20)

'''Main Program'''

class LogEntry():
    LOG_FORMAT = re.compile('([\w\-\.]+) - - \[([^\]]+)\] "(\w+) ([^\s]+)[^"]*" (\d+) (-|\d+)')
    class ParseError(Exception):
        pass

    def __init__(self, line):
        self.line = line
        matches = LogEntry.LOG_FORMAT.match(line)
        if matches:
            self.host, self.timestamp, self.verb, self.resource, self.statusCode, self.contentLength = matches.groups()
            self.timestamp = datetime.strptime(self.timestamp, "%d/%b/%Y:%H:%M:%S %z")
            self.statusCode = int(self.statusCode)
            if self.contentLength == '-':
                self.contentLength = 0
            self.contentLength = int(self.contentLength)
        else:
            raise LogEntry.ParseError(line)

## Perform relevant computations, using functions as needed
def main():
    with open(logPath, 'r', errors='ignore') as logFile:
        for line in logFile:
            entry = LogEntry(line)
            feature1(entry)
            feature2(entry)
            feature3(entry)
            feature4(entry)

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

if __name__ == '__main__':
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

    main()

    '''Close output files'''
    hoursFile.close()
    hostsFile.close()
    blockedFile.close()
    resourcesFile.close()

