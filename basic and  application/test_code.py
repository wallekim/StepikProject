import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    pattern = r'\bcat\b'
    if re.match(pattern, line):
        print(line)
