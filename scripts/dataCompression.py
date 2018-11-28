'''
In its effort to push the limits of file compression, Dropbox recently developed a lossless compression algorithm for H.264 and JPEG files. Since you are thinking about applying for a job at Dropbox, you decided to experiment with simple lossless compression as part of your interview prep.

One of the most widely known approaches in the field of compression algorithms is sliding window compression. It works as follows:

Consider characters one by one. Let the current character index be i.
Take the last width characters before the current one (i.e. s[i - width, i - 1], where s[i, j] means the substring of s from index i to index j, both inclusive), and call it the window. If there are less than width characters before the current one, then you should use s[0, i - 1] as the window.
Find such startIndex and length that s[i, i + length - 1] = s[startIndex, startIndex + length - 1] and s[startIndex, startIndex + length - 1] is contained within the window. If there are several such pairs, choose the one with the largest length. If there still remains more than one option, choose the one with the smallest startIndex.
If the search was successful, append "(startIndex,length)" to the result and move to the index i + length.
Otherwise, append the current character to the result and move on to the next one.
Given a string, apply sliding window compression to it.

Example

For inputString = "abacabadabacaba" and width = 7, the output should be
losslessDataCompression(inputString, width) = "ab(0,1)c(0,3)d(4,3)c(8,3)".

Step 1: i = 0, inputString[i] = 'a', window = "". 'a' is not contained within the window, so it is appended to the result.
Step 2: i = 1, inputString[i] = 'b', window = "a". 'b' is not contained within the window, so it is appended to the result.
Step 3: i = 2, inputString[i] = 'a', window = "ab". 'a' can be found in the window. 'a' in the window corresponds to the inputString[0], so (0,1) representing the substring "a" is appended to the result.
Step 4: i = 3, inputString[i] = 'c', window = "aba". The same situation as in the first two steps.
Step 5: i = 4, inputString[i] = 'a', window = "abac". Consider startIndex = 0, length = 3. inputString[startIndex, startIndex + length - 1] = "aba" and it is contained within the window, inputString[i, i + length - 1] = "aba". Therefore, "(0,3)" should be added to the result. i += length.

Step 6: i = 7, inputString[i] = 'd', window = inputString[0, 6] = "abacaba". The same situation as in the first two steps.
Step 7: i = 8, inputString[i] = 'a', window = inputString[1, 7] = "bacabad". Consider length = 3 again. inputString[i, i + b - 1] = "aba", window[3, 5] = "aba", and it corresponds to inputString[4, 6] since inputString[0, 2] is no longer within the window. So, "(4,3)" should be appended. i += length.
Step 8: i = 11, inputString[i] = 'c', window = "abadaba". The same situation as at the first two steps.
Step 9: i = 12, inputString[i] = 'a', window = "badabac". length = 3, inputString[i, i + length - 1] = "aba", window[3, 5] = "aba", and it corresponds to inputString[8, 10]. So, "(8,3)" should be appended. i += length.


'''

from heapq import heapify, heappush, heappop

def losslessDataCompression(inputString, width):
    # Keep a running result string that we append to
    result = ''
    
    current_index = 0
    while current_index < len(inputString):
        # The start index begins `width` units back, but we might hit the beginning of inputString
        start_index = max(current_index - width, 0)
        length = 0 # length of a subword in the window that matches a subword after the window
        
        # There might be multiple matches, so we want to keep a max heap and pick the largest length
        matching_lengths = []
        heapify(matching_lengths)
        # There also might be multiple matches of the same length, so we will keep a dictionary
        # and maintain the smallest start_index associated with length
        length_dict = {} # {length: smallest start_index associated with length}
        

        # Let's skip through all the characters that don't match the current character
        while inputString[start_index] != inputString[current_index] and start_index < current_index:
            start_index += 1
        # If we went through the entire window without matching the current character,
        # then we haven't found anything to compress. Append the current character and
        # slide the window a unit to the right.
        if start_index == current_index:
            result += inputString[current_index]
            current_index += 1
            continue

        # At this point, we have found a character in the window that matches our current character.
        # We want to find the longest subword in the window.
        
        
        
        while start_index + length < current_index:
            
            # We will keep checking whether longer and longer substrings match. We also want to make sure that
            # we keep the left substring in the window.
            while inputString[start_index : start_index + length] == inputString[current_index : current_index + length]:
                # We don't want to leave the window. If we would leave the window, we instead break and
                # record the length of the matching subwords up to that point
                if start_index + length > current_index:
                    break
                else:
                    length += 1
        
            # Push the length of the matching subword onto the max heap.
            # Note Python uses negatives to implement max heap from a min heap.
            length -= 1
            heappush(matching_lengths,-length)
            
            # Here, we ensure each length is associated with the smallest start_index by 
            # not updating the start_index if the same length is found again
            if length not in length_dict:
                length_dict[length] = start_index
            
            # There might be other subwords we haven't checked yet, so we increase the
            # start index and try matching subwords again
            start_index = start_index + length + 1
            
        # At this point, we have a dictionary of lengths and start_index of subwords in the window
        # that match subwords after the window.
        # We want the longest length of matching subwords and the associated start_index for that length.
        # We will append that information to the result.
        max_length = -heappop(matching_lengths)
        max_length_start_index = length_dict[max_length]
        # Append '(max_length_start_index,max_length)' to the result
        result += f"({max_length_start_index},{max_length})"
        
        # Increase the current index past the maximum matching subword
        current_index += max_length
    
    # Now we have processed the whole inputString, keeping a running result along the way.
    # Time to return the result.
    return result

print(losslessDataCompression('abacabadabacaba',7))