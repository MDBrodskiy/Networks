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
		self.packet_id = packet_t[0]
		self.dest = packet_t[1]
		self.src = packet_t[2]
		self.data = packet_t[3]
		self.parity = packet_t[4]
	def check_parity(self, data, rcvd_parity):
		#add your code here 
		pass # Check if leftover modulo 2 matches parity
		if (str(data.count("1") % 2) == rcvd_parity):
		   self.ParityValid = True # Make true if correct
		   return True 
		self.ParityValid = False # False otherwise
		return False
	def parsed_packet(self):
		#add your code here 
		pass
		return "Received Packet Number {s1} from node {s2}. Parity Check returns {s3}".format(s1=self.packet_id, s2=self.src, s3=self.check_parity(self.data, self.parity)) # Print given values


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
	return sum(range(integer_to_sum_to + 1)) # Returns the sum from 0 to integer_to_sum_to

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
	if (type(list_of_lists) != list): # Checks for list input
		return None # Returns None if not list
	return [i[0:-1] + [i[-1] * 2] for i in list_of_lists] # Returns same list with doubled last column

# (Add your comments here)
def problem_nine( list_of_email_addresses ):
	pass
	# (Add your code here)
	if (type(list_of_email_addresses) != list): # Check for list input
		return None # Return None if not list
	return list(set([a.split("@")[1] for a in list_of_email_addresses if (".com" in a and "@" in a and not any(i.isdigit() for i in a.split("@")[1]))])) # Filters domains from valid addresses

def problem_ten( packet_t ):
	# add your code here 
	pass
	pkt_o = PacketClass(packet_t) # Create class instance
	pkt_o.check_parity(pkt_o.data,pkt_o.parity) # Check parity
	return pkt_o.parsed_packet() # Return message about parse

# Program entry point.
if __name__ == '__main__':
	pass
	# (Add your code here)
	print("\nProblem 1:")
	print(problem_one('Hello World!'))
	print("\nProblem 2:")
	print(problem_two(8, [1, 2, 3, 4, 5])) # Should be False
	print(problem_two(5, [1, 2, 3, 4, 5])) # Should be True
	print(problem_two(5, [])) # Should be False
	print(problem_two([1,2,3], 5)) # Should be None
	print("\nProblem 3:")
	print(problem_three(6)) # Should be 21
	print(problem_three("6")) # Should be None
	print("\nProblem 4:")
	print(problem_four([1, 2, 3], [2, 3, 4])) # Should be [1, 2, 3, 4]
	print(problem_four([], [2, 3, 4])) # Should be [2, 3, 4]
	print(problem_four(5, [2, 3, 4])) # Should be None
	print("\nProblem 5:")
	print(problem_five(3)) # Should be 28.27433388
	print(problem_five(3.0)) # Should be 28.27433388
	print(problem_five("3.0")) # Should be None
	print("\nProblem 6:")
	print(problem_six("MyData.csv")) # Should be [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
	print(problem_six(7)) # Should be None
	print(problem_six("FalseFile")) # Should be None
	print("\nProblem 7:")
	print(problem_seven('48656c6c6f20576f726c6421')) # Should be Hello World!
	print(problem_seven(None)) # Should be None
	print("\nProblem 8:")
	print(problem_eight([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) # Should be [[1, 2, 6], [4, 5, 12], [7, 8, 18]]
	print(problem_eight([[1, 2], [4, 5, 6], [7, 8, 9]])) # Should be [[1, 4], [4, 5, 12], [7, 8, 18]]
	print(problem_eight([[1, 2], [3, 4]])) # Should be [[1, 4], [3, 8]]
	print(problem_eight(None)) # Should be None
	print("\nProblem 9:")
	print(problem_nine(['cats@gmail.com','Hello World!','dogs@gmail.com','cows@yahoo.com'])) # Should be ['yahoo.com', 'gmail.com']
	print(problem_nine(['cats@g10mail.com','Hello World!','dogs@gma7il.com','cows@yahoo.com'])) # Should be ['yahoo.com']
	print(problem_nine(['None'])) # Should be []
	print(problem_nine(None)) # Should be []
	print("\nProblem 10:")
	print(problem_ten(("2","10", "5", "01100101011000101011001001110110", "0")))
