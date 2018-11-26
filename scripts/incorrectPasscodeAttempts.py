'''
One Very Important User (VIU) has a Very Confidential Document (VCD) stored on his Dropbox account. He doesn't let anyone see the VCD, especially his roommates who often have access to his devices.

Opening the Dropbox mobile app on the VIU's tablet requires a four-digit passcode. To ensure the confidentiality of the stored information, the device is locked out of Dropbox after 10 consecutive failed passcode attempts. We need to implement a function that given an array of attempts made throughout the day and the correct passcode checks to see if the device should be locked, i.e. 10 or more consecutive failed passcode attempts were made.

Example

For
passcode = "1111" and

attempts = ["1111", "4444",
            "9999", "3333",
            "8888", "2222",
            "7777", "0000",
            "6666", "7285",
            "5555", "1111"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = true.

The first attempt is correct, so the user must have successfully logged in. However, the next 10 consecutive attempts are incorrect, so the device should be locked. Thus, the output should be true.

For
passcode = "1234" and

attempts = ["9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "9999",
            "9999", "1234",
            "9999", "9999"]
the output should be
incorrectPasscodeAttempts(passcode, attempts) = false.

There are only 9 consecutive incorrect attempts, so there's no need to lock the device.
'''


def incorrectPasscodeAttempts(passcode, attempts):
    # count the number of consecutive failed attempts
    count = 0
    for attempt in attempts:
        if attempt != passcode and count >= 9:
            # A count of 9 means failure was recorded for count=0,1,2,..,9, so 10 failures
            return True
        elif attempt != passcode:
            count += 1
        elif attempt == passcode:
            count = 0 # reset the failed attempt count
    return False