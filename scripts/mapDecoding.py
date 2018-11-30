"""
A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
You are an FBI agent and you need to determine the total number of ways that the message can be decoded.

Since the answer could be very large, take it modulo 109 + 7.
"""

def mapDecoding(message):
    
    if len(message) < 2:
        return 1
    
    a = 1
    b = 1

    
    for i in range(1,len(message)):
        
        digit = int(message[i])
        new_candidate = int(message[i-1:i+1])
        
        if 1 <= digit <= 9:
            if 10 <= new_candidate <= 26:
                a, b = b, b+a
            else:
                a = b

        elif digit == 0 and new_candidate not in [10,20]:
            return 0
    
    return b

print(mapDecoding('10122110'))