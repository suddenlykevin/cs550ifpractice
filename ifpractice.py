# if practice
# Kevin Xie CS550 09/18/2018
# Determine grade (or return error) as efficiently as possible
# it may also be more efficient to use arrays, but we have yet to delve into that subject.

import sys

score = float(sys.argv[1]) #using command line argument

if 0<=score<=5: #range
	if score<1:
		print("F")
	elif score<1.5: # no need to repeat numbers if ascending
		print("D-")
	elif score<2:
		print("D")
	elif score<2.5:
		print("D+")
	elif score<2.85:
		print("C-")
	elif score<3.2:
		print("C")
	elif score<3.5:
		print("C+")
	elif score<3.85:
		print("B-")
	elif score<4.2:
		print("B")
	elif score<4.5:
		print("B+")
	elif score<4.7:
		print("A-")
	elif score<4.8:
		print("A")
	elif score<=5:
		print("A+")
else: #outside of range
	print("Your score should be between 0 and 5. Try again.")