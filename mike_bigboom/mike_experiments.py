#! /usr/bin/env/python3

import cmath
import math
import csv
from functions import steps_to_ea, create_complex_number_list_from_csv, complex_divide

#figure out process for setting comp1 & 2 from csv values

#THESE VALUES TOOK WAAAAAAAAAAAY TOO LONG TO COMPUTE, EVEN COMMENTING OUT THE PRINT STATEMENTS 
#Think about printing the text of activity that isn't a result to a log file instead, it'll clog the console
#if it writes to it every time
#complex_1 = complex(155, 34)
#complex_2 = complex(135, -14)


# parsing csv data and creating a list with sub-lists for each complex number pairing

#paths to csv files
basepath = '/Users/mike/repos/geekout_main/mike_bigboom/'
#datapath = 'NormTermOrder251000.csv'
#datapath = 'NormTermOrder10000.csv'
filepath = 'test.csv'
full_filepath = basepath + filepath

complex_number_list = create_complex_number_list_from_csv(full_filepath)

#I now have a Py list of complex numbers in NormTerm order
#in order to keep the index of the CSV consistent with the python array index, I inserted a dummy complex number 0+0j at position 0
#now using complex_number_list[1] will actually return the first number in the CSV

complex_1 = complex_number_list[1]
complex_2 = complex_number_list[2]

#here is the main step-finding logic

print(steps_to_ea(complex_1,complex_2))





#comes to (135 - 34i)/(144 + 14i) = 1.11 + 0.37i (approximately)
#a1 = complex(155 + 34i) #will be complex_1
#a2 = complex(135 - 14i) #will be complex_2
#is_remainder = bool #needed?


#PROCESS:
#define complex 1 & 2 -> read row from csv into complex 1,2?  a function?
#define var for division result and perform division to it

#round real element of result
#round imaginary element of result

#use these to extract the parts of a complex number
#z.real
#z.imag


####################
#ALERT!!
#I was using this to round, but it doesn't handle complex/float well,
#and it was starting to get dirty
#round(x[, n])	
#definition: x rounded to n digits, rounding ties away from zero. If n is omitted, it defaults to 0.

