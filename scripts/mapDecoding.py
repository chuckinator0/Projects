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
    # The main idea is that we wil build up the number of combinations by adding
    # one character at a time. Whenever we add a digit to the message, we are
    # either adding a 1 digit letter to all the combinations we had in the last step,
    # or we are adding a 2-digit letter to all the combinations we had two steps ago.
    # In this way, it's a lot like fibonacci, except we don't always add the previous 
    # two steps. We only add the result from two steps ago if the 2-digit candidate actually
    # corresponds to a letter. If it doesn't, then the number of combinations is just
    # the same as in the last step (no update to the number of combinations).
    # There's also a complication when we add 0. Adding 0 might mean
    # there are no meaningful encodings (e.g. any encoding that ends in 90 is impossible).
    # If we add a 0 and the 2-digit candidate is not 10 or 20, then there are no valid
    # encodings. If the 2-digit candidate is 10 or 20, then the combinations are the same
    # as 2 steps ago with a J or T appended.
    
    if len(message) < 2:
        return int('0' not in message)
    
    previous = 1 # only one way to encode empty string (we are at index 0)
    current = 1 # only one way to encode message with 1 character (we are at index 1)

    
    for i in range(1,len(message)):
        
        digit = int(message[i])
        new_candidate = int(message[i-1:i+1]) # possible 2-digit encoding
        
        if 1 <= digit <= 9:
            if 10 <= new_candidate <= 26:
                # update is the same as fibonacci
                previous, current = current, current + previous
            else:
                # current doesn't get updated, but we still shift previous forward
                previous = current

        if digit == 0:
            if new_candidate in [10,20]:
                # current is the same as two steps ago
                current = previous
            else:
                return 0
    
    return current

print(mapDecoding('10122110'))