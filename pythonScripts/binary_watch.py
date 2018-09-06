'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent
the minutes (0-59).

Given a non-negative integer n which represents the number of LEDs that are currently on, return all
possible times the watch could represent.
'''

def readBinaryWatch(n):
	'''
	This function goes through each time, decides how many LEDs are on, and if
	the number of LEDs for a time matches the target number of LEDs n, then we append to our output of
	possible times with n LEDs.
	'''
	output = []

	for h in range(0,12):
		for m in range(0,60):
			# count the LEDs that are on in the hours part by looking at the 1's in its binary representation
			hLEDS = bin(h).count('1')
			# count the LEDs that are on in the minutes part by looking at the 1's in its binary representation
			mLEDS = bin(m).count('1')
			if mLEDS + hLEDS == n:
				output.append('{hour}:{minute:02}'.format(hour=h, minute=m))
	return output

print(readBinaryWatch(3))