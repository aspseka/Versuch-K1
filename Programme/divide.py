#!/usr/bin/env python

import sys
import array

# check number of arguments
if (len(sys.argv)!=3):
   # wrong number of arguments, print small help
   print("Usage : %s filename delta_t" % sys.argv[0])
   # exit program
   sys.exit(0)

# get arguments
filename=sys.argv[1]
delta_t=float(sys.argv[2])

# read in the whole file, create a list 'data'
infile=open(filename)
data=infile.read().split("\n")
infile.close()

# delete the last element of the list (it's an empty line)
data.pop()

# convert the list of strings to a list of floats
i=0
while i<len(data):
   data[i]=float(data[i])
   i=i+1

# now count the number of signals in the first time interval, the second
# time interval and so on and put these numbers in an array 'counts'
counts=array.array("i")
for x in data:
   i=int(x/delta_t)
   while (len(counts)<=i):
      counts.append(0)
   counts[i]=counts[i]+1
# delete the last number (the last time interval was only partly measured)
counts.pop()

# now we print out the number of signals in the time intervals
i=0
while (i<len(counts)):
   print("%d %d" % (i,counts[i]))
   i=i+1

