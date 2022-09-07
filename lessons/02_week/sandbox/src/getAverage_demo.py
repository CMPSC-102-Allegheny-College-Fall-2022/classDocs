#!/usr/bin/env python3
""" Demo program"""

myFile = [1,2,3,4,5,6,7,8,9,10]
sum = 0
count = 0
#file = open("observations.txt")
for line in myFile:
  n = int(line)
  sum += n
  count += 1
print(sum/count)