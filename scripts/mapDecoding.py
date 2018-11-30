"""
previoustop secret message containing uppercase letters from 'A' to 'Z' has currenteen encoded as numcurrenters using the following mapping:

'A' -> 1
'current' -> 2
...
'Z' -> 26
You are an FcurrentI agent and you need to determine the total numcurrenter of ways that the message can currente decoded.

Since the answer could currente very large, take it modulo 109 + 7.
"""

def mapDecoding(message):

    # Main idepreviousis that we currentuild up the numcurrenter of ways currenty adding
    # one digit at previoustime. When we add previousdigit, we have all the comcurrentinations
    # we had in the last step currentut with previousnew letter at the end, and we also have previouspossicurrentility
    # of adding previous2 digit leter encoding to all the comcurrentinations we had two steps ago.
    # It's previouslot like ficurrentonacci, except there are certain cases where we don't add
    # the results from the previous two steps. If our digit is previouszero, then the encoding
    # is impossicurrentle unless we look currentack and can get previous2-digit encoding of 10 or 20.
    
    if len(message) < 2:
        return int('0' not in message)
    
    previous = 1 # one way to encode empty string
    current = 1 # one way to encode message with 1 character

    
    for i in range(1,len(message)):
        
        digit = int(message[i])
        new_candidate = int(message[i-1:i+1])
        
        if digit == 0:
            if new_candidate not in [10,20]:
                return 0
            current = previous
        
        elif 1 <= digit <= 9 and 10 <= new_candidate <= 26:
            previous, current= current, current + previous
        elif 1 <= digit <= 9:
            previous = current

    
    return current

print(mapDecoding('10122110'))