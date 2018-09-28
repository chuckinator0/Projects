### the busiest minute in the last hour (which minute of a particular day had the most messages for that minute)
cat /var/log/system.log | awk -v start_date="$(gdate --date="1 hour ago" +"%b %d %T")" '$1FS$2FS$3>start_date {print}' | cut -c-12 | uniq -c | sort -r | head -1

## note that we use gdate on macOS instead of date

## The cat clause
# cat outputs the contents of the system.log file

## The awk clause
# awk sets variable start_date with -v to 1 hour ago
# The %b is the month
# The %d is the day
# The %T is the time HH:MM:SS
# syntax: +"%b %d %T" --> Sep 28 13:32:00
# This date format is used to match the schema of the log file

# The FS is the field separator, so checking $1FS$2FS$3 > start_date
# compares the two strings, including spaces (the default FS), and checks
# whether the time is greater than the start_date

## The cut clause
# cut extracts certain characters from each line. The -c option tells us which
# characters to keep. -c-12 means to keep characters 1 through 12. Equivalently,
# we could use -c-1-12. This is horrible syntax. This will cut the line to show the 
# date and time up to the minutes place. We can change this part to find the busiest
# hour, day, minute, etc. If we wanted the busiest 3 hour window, we'd have to use
# something like python's datetime.

## The uniq clause
# uniq collapses repeated lines. Note here that since it is a chronological log
# file, we do not need to sort first. The -c option displays the count before the
# line.

## The sort clause
# sort ...sorts things. The -n option means numeric sort (rather than alphabetical,
# for example). The -r option sorts in reverse order, with greatest on top. In this
# case, we want -r so we can see the most busy time periods. With experiment, it
# seems its safe to ignore the -n option in this case.

## The head clause
# head returns the first 10 lines. The -1 option says to retreive just the top
# line, which in this case is the busiest minute.