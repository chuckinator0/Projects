import datetime

stamp = "Sep 18 03:06:03"
stamp_list = stamp.split()
time = datetime.datetime.strptime(stamp[0:15], "%b %d %H:%M:%S" )

delta = datetime.datetime(2018,8,24,7,36) - datetime.datetime(2018,8,24,6,36)

print(delta)