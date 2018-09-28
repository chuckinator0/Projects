 #!/bin/bash

# Valid Phone Numbers

# Given a text file file.txt that contains list of phone numbers (one per line), write a one liner bash script to print all valid phone numbers.

# You may assume that a valid phone number must appear in one of the following two formats: (xxx) xxx-xxxx or xxx-xxx-xxxx. (x means a digit)

# You may also assume each line in the text file must not contain leading or trailing white spaces.

# Example:

# Assume that file.txt has the following content:

# 987-123-4567
# 123 456 7890
# (123) 456-7890

# Your script should output the following valid phone numbers:
# 987-123-4567
# (123) 456-7890

####################################################

#### Three solutions. Let's explain every last detail

### Solution 1:

# egrep '^(\([0-9]{3}\)\s[0-9]{3}-[0-9]{4}|[0-9]{3}-[0-9]{3}-[0-9]{4})$' $1

## We use egrep. The 'e' in egrep stands for extended regular expression. What this means is that the special characters
## '}', '?', etc will be treated as special characters. Paradoxically, regular old grep doesn't treat these as special
## and requires \ to turn them into special characters (usually \ is used to turn a special character into a plain character)

## The '^' is the 'start character' it specifies that the expression we are looking for must start with our regular
## expression. The '[0-9]' means any digit. The '{n}' means repeating exactly n times. Look at
## (<expression1> | <expression2>). This means we found a match if either expression1 or expression2 is found.
## The \s means space. The $ means the expression must end at that point. The $1 means we are applying egrep to the first
## argument in the terminal. In terminal, we run `./valid_phone_numbers.sh valid_phone.txt`, so the .txt file is
## argument 1.

### Solution 2:

# egrep '^(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$' $1

## Same as before, but use \d for digit.

### Solution 3
egrep '^(\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}$' $1

## This time, we do 'xxx- or (xxx) ' followed by xxx-xxxx. We also used \s to signifiy the space after the parentheses.
## Keep in mind that the spacing and exact placement of the characters matter with regular expressions, which
## makes them very hard to read.


