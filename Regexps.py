import re

s = "\n" \
    "This is a string jjj to taest different regular expression formats u t using re.ssearch() 23456cabZDAFF"

m = re.search('.',s)

print(re.search('.',s))
print(re.search('\.',s))
print(re.search('[z]',s))
print(re.search('[scba]',s))
print(re.search('[^sabc]',s))
print(re.search('[0,1]',s))
print(re.search('[F|K]',s))
print(re.search('a?e', s))
print(re.search('F$', s))
print(re.search('u*u', s))
print(re.search('j+', s))
print(re.search('j{1,10}', s))