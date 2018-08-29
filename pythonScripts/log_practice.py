"""
Parse a log file!
"""


def hours(string):
    return int(string[0:2])


def min(string):
    return int(string[3:5])


def duration(string1, string2):
    minutes1 = 60 * hours(string1) + min(string1)
    minutes2 = 60 * hours(string2) + min(string2)
    difference = abs(minutes2 - minutes1)
    return difference


log_file = open("./log_practice.log", "r")
topic_dict = {}
total_duration = 0
last_event = []

for line in log_file:
    if line == "\n":
        print('\n')
        last_event = []
        continue
    event = line.rstrip('\n').split(" ", 1)
    start = event[0]
    topic = event[1]
    if last_event == []:
        last_event = event
        continue
    dur = duration(last_event[0], start)
    total_duration += dur
    output = last_event[0] + '-' + start + " " + last_event[1]
    print(output)
    if last_event[1] in topic_dict:
        topic_dict[last_event[1]] += dur
    else:
        topic_dict[last_event[1]] = dur
    last_event = event

for topic in topic_dict:
	print(topic + ' ' + str(topic_dict[topic]) + ' minutes' + ' ' + str(100*topic_dict[topic]/total_duration) + '%')

print(topic_dict)
