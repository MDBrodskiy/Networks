"""
Please fill in the functions below
- DO NOT change the function signatures
- Be sure that you have the correct return type listed in the assignment
"""

# Author: Michael Brodskiy

class PacketClass:
	def __init__(self, packet_t):
		#add initialization code here 
		self.ParityValid = -1
	def check_parity(self, data, rcvd_parity):
		#add your code here 
		pass
	def parsed_packet(self):
		#add your code here 
		pass


# (Add your comments here)
# Checks for string input and reverses if it is a string, otherwise None
def problem_one( string_to_be_reversed ): 
	pass 
	# (Add your code here) 
	if (type(string_to_be_reversed) != str):
		return None # Checks that input is string, returns None if not
	return string_to_be_reversed[::-1] # Returns the reverse of string, [::-1] reverses

# (Add your comments here)
# If a number and list are entered, returns whether number is in list, otherwise None
def problem_two( number_to_find , list_to_check ):
	pass
	# (Add your code here)
	if (type(number_to_find) != int or type(list_to_check) != list):
		return None # Checks for correct input type, and returns None if wrong type
	return (number_to_find in list_to_check) # Returns whether number is found in list

# (Add your comments here)
# If number entered is greater then 0, returns sum from 0 to num, otherwise None
def problem_three( integer_to_sum_to ):
	pass
	# (Add your code here)
	if (type(integer_to_sum_to) != int or integer_to_sum_to < 0):
		return None # Checks for correct inputs, returns None if wrong
	return sum(range(integer_to_sum_to)) # Returns the sum from 0 to integer_to_sum_to

# (Add your comments here)
# Returns a list of a single copy of each item in a list if both inputs are lists, otherwise None
def problem_four( left_list , right_list ):
	pass
	# (Add your code here)
	if (type(left_list) != list or type(right_list) != list):
		return None # If either input is not a list returns None
	return list(set(left_list + right_list)) # Returns single copy of each value

# (Add your comments here)
# Returns area of a circle with inputted radius if int or float, otherwise None
def problem_five( radius ):
	pass
	# (Add your code here)
	if (type(radius) != float and type(radius) != int):
		return None # Checks radius is int or float type
	return "{:.8f}".format(3.1415926535 * radius * radius) # Returns area formatted to 8 decimal points

# (Add your comments here)
# Checks if a file exists and returns a matrix of integer values from it, otherwise None
def problem_six( filename ):
	pass
	# (Add your code here)
	from os.path import exists # import 'exists' to check file existence
	if (type(filename) != str or not exists(filename)):
		return None # Verify input is string and real file
	return [list(map(int, line.rstrip().split(","))) for line in open(filename)] # map each value split from a line of the file to int

# (Add your comments here)
# Checks if hex string is passed and decodes to ascii, otherwise None
def problem_seven( hex_string ):
	pass
	# (Add your code here)
	if (type(hex_string) != str): # Checks for string input
		return None # Returns None if not string
	return bytearray.fromhex(hex_string).decode() # Decodes otherwise

# (Add your comments here)
def problem_eight( list_of_lists ):
	pass
	# (Add your code here)

# (Add your comments here)
def problem_nine( list_of_email_addresses ):
	pass
	# (Add your code here)

def problem_ten( packet_t ):
	# add your code here 
	pass

# Program entry point.
if __name__ == '__main__':
	pass
	# (Add your code here)

print(problem_eight([[1,2,3], [4,5,6], [7,8,9]]))
