# Print counts of the occurences of mark, tim, allen, all case insensitive

awk -v count_mark=0 -v count_tim=0 -v count_allen=0
'{
for(i = 1; i <= NF; i++) { 
    {if(tolower($i)=="mark") count_mark++}
    {if(tolower($i)=="tim") count_tim++}
    {if(tolower($i)=="allen") count_allen++} }
} 
END{
print count_mark," mark";
print count_tim," tim";
print count_allen," allen"
}'
parsePractice1