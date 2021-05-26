
from os import write
import sys
import re

# Resource for this base script: https://www.geeksforgeeks.org/extract-ip-address-from-file-using-python/

# variable for file to read
file = sys.argv[1]

# Adding stdout
var = sys.stdout

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
# Per instructions, writing to stdout
sys.stdout = open(file_name, 'w+')

with sys.stdout as new_file:
    for line in lst:
        print(line)
sys.stdout.close()
