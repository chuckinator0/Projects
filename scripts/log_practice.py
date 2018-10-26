"""
Parse a log file! See log_practice.log.
The log is a schedule of classes on different days.

Each line has the form:
HH:MM Topic

Days are separated by blank lines.
"""


def hours(string):
    return int(string[0:2])


def minutes(string):
    return int(string[3:5])


def duration(string1, string2):
    minutes1 = 60 * hours(string1) + minutes(string1)
    minutes2 = 60 * hours(string2) + minutes(string2)
    difference = abs(minutes2 - minutes1)
    return difference


topic_dict = {} # {topic: duration of that topic}
total_duration = 0
last_event = []

with open("./log_practice.log", "r") as log_file:
    for line in log_file:
        # if we reach a blank line, it means we start a new day
        if line == "\n":
            print('\n')
            last_event = []
            continue
        # Turn the line into an event where index 0 is the stat time and
        # index 1 is the topic
        event = line.rstrip('\n').split(" ", 1)
        start = event[0]
        topic = event[1]
        # if this is the first event of the day, set the last_event variable
        if last_event == []:
            last_event = event
            continue
        dur = duration(last_event[0], start)
        # increase total duration
        total_duration += dur
        output = last_event[0] + '-' + start + " " + last_event[1]
        print(output)
        # update the topic dictionary
        if last_event[1] in topic_dict:
            topic_dict[last_event[1]] += dur
        else:
            topic_dict[last_event[1]] = dur
        last_event = event

for topic in topic_dict:
	print(topic + ' ' + str(topic_dict[topic]) + ' minutes' + ' ' + str(100*topic_dict[topic]/total_duration) + '%')

print(topic_dict)
