#!/usr/bin/env python

import sys
import array

# check the number of arguments
if (len(sys.argv)!=4):
   # wrong number of arguments, print small help
   print("Usage : %s filename delta_t step" % sys.argv[0])
   print("with step=1,2,...")
   # exit program
   sys.exit(0)

# get command line arguments
filename=sys.argv[1]
delta_t=float(sys.argv[2])
step=int(sys.argv[3])

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

# now we look at the time differences of the signals
# signal i to signal i+step
# and we count how often these time differences are between
# 0 and delta_t , delta_t and 2*delta_t , 2*delta_t and 3*delta_t , ...
# and we put these numbers in an array 'histogram'
histogram=array.array("i")
i=0
while (i<len(data)-step):
   t=data[i+step]-data[i]
   k=int(t/delta_t)
   while (len(histogram)<=k):
      histogram.append(0)
   histogram[k]=histogram[k]+1
   i=i+1

# now we print out the second (the binned) histogram
i=0
while (i<len(histogram)):
   print("%d %d" % (i,histogram[i]))
   i=i+1

