#!/bin/bash

# Word Frequency
# Here, we read a text file and give a list each word and its count in
# descending order.

cat word_frequency.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'

# `cat` prints the file to standard output. Then we pipe it into `tr`. The `tr` command
# translates one string into another. Here, we are translating the space character ' '
# into a newline character. So, each word will be printed on a separate line. However,
# there may be multiple spaces in a row, so the `-s` option of `tr` squeezes those spaces
# together into one space.

# Next, `sort` rearranges the words so that they are repeated together. Then `uniq -c`
# groups each unique word. The `-c` option ensures that each word is counted. The next
# `sort -r` sorts this new list in descending order by its count. Then `awk` prints the
# second column (the word) followed by the first column (the count).
