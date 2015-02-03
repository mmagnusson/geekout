#python3
import math
import csv

#REWRITE THIS PIECE OF SHIT CODE.
#oh my god this is disgusting.
def float_complex_to_rounded_complex_number(complex_to_change):
	if complex_to_change.real < 1:
		if complex_to_change.real >= .5:
			real = 1
		else:
			real = 0
	else:
		real = math.trunc(complex_to_change.real + 0.5 )
	######
	if complex_to_change.imag < 1:
		if complex_to_change.imag >= .5:
			imaginary = 1
		else:
			imaginary = 0
	else:	
		imaginary = math.trunc(complex_to_change.imag + 0.5 )
	return complex(real, imaginary)


def complex_divide(complex_1, complex_2):
	return (complex_1 / complex_2)


def complex_remainder(complex_1, complex_2):
	return 0

#################

def create_complex_number_list_from_csv(full_filepath):
	f = open(full_filepath)
	complex_csv = csv.reader(f)
	complex_number_list = []
	for row in complex_csv:
		complex_number = complex(int(row[0]), int(row[1]))
		complex_number_list.append(complex_number)
	#in order to keep the index of the CSV consistent with the python array index, I inserted a dummy complex number 0+0j at position 0
	#now using complex_number_list[1] will actually return the first number in the CSV	
	#complex_number_list.insert(0, complex(0,0))	
	return complex_number_list

#main function for steps
def steps_to_ea(complex_1, complex_2):
	count = 0
	remainder = None

	while remainder != 0:
		print("%%%%%%%%%%%%%%")
		print("Iteration number is " + str(int(count + 1)))
		print("Current remainder (first iteration it should be nil)" + str(remainder))
		print("Current 1st number is " + str(complex_1))
		print("Current 2nd number is " + str(complex_2))
		print("All math/assignment for this iteration will now happen")
		print("$$$$$$$$$$$$$$$$")


		divided = complex_divide(complex_1, complex_2)
		remainder = complex_1 - (float_complex_to_rounded_complex_number(divided))*complex_2

		print(divided.real)
		print(divided.imag)
		print(complex(divided.real, divided.imag))

		#remainder = complex_1 - complex(divided.real, divided.imag) * complex_2 

		complex_1=complex_2
		complex_2=remainder

		count+=1

	print("The method has identified the remainder as 0. The number of steps is:" + str(count))


