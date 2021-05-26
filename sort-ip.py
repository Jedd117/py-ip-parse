
from os import write
import sys
import re

# Resource for this base script: https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/

# variable for file to read
file = sys.argv[1]
 
# opening and reading the file
with open(file) as fh:
   fstring = fh.readlines()
 
# decalring the regex pattern for IP addresses
pattern = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
 
# initializing the list object
lst=[]
 
# extracting the IP addresses
for line in fstring:
   lst.append(pattern.search(line)[0])

# file_name will name the dump file as the name of the imported file + '-report.txt'
file_name = file.split('.txt')[0] + "-report.txt"

# Creating new file to dump output
# w+ creates a file if one is not in use. 
with open(file_name, 'w+') as new_file:
    for line in lst:
        new_file.write(line + "\n")