"""
 * ===============================================================
 *
 *       Filename:  EECE2540_002937644_Proj.py
 *       Assignment: Computing Homework 3
 *       Title: Python TCP Client, Mathematical Evaluator
 *
 *    Description:  Acts as a TCP client that calculates messages 
 *    of a certain format
 *
 *        Version:  1.0
 *        Created:  11/29/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy (Michael Brodskiy)
 *           NUID:  002937644
 *
 * ===============================================================
""" 

# Indicate start of program
print("Started TCP Client Program")

# Import necessary socket utilities
from socket import *

# Establish address and port number
address = '129.10.131.26'
port = 12005
identity = (address, port)

# Create server socket
server = socket(AF_INET, SOCK_STREAM)
print("Client Socket Established")
server.connect(identity)
print("Socket Connected")

# Send Greeting Message
msg = "EECE2540 INTR 002937644".encode()
server.send(msg)
print("Sent greeting message to:", identity)

server_message = server.recv(4096) # Receive server message (buffer size = 4096)
decoded_message = server_message.decode() # Decode message
print("Message Received:", decoded_message) # Show received message

# Create a loop until failure or success flag received
while "FAIL" not in decoded_message and "SUCC" not in decoded_message:

    # Tokenize message
    msg_tokens = decoded_message.split(" ")

    # Perform indicated operation
    result = 0
    if msg_tokens[3] == "+":
        result = int(msg_tokens[2]) + int(msg_tokens[4])
    elif msg_tokens[3] == "-":
        result = int(msg_tokens[2]) - int(msg_tokens[4])
    elif msg_tokens[3] == "*":
        result = int(msg_tokens[2]) * int(msg_tokens[4])
    elif msg_tokens[3] == "/":
        result = int(msg_tokens[2]) / int(msg_tokens[4])
    else:
        print("Invalid Operation")

    # Send result to server and print to view
    msg = "EECE2540 RSLT " +  str(result)
    print("Calculated result:", msg)
    server.send(msg.encode())

    server_message = server.recv(4096) # Receive server message (buffer size = 4096)
    decoded_message = server_message.decode() # Decode message
    print("Message Received:", decoded_message) # Show received message

if "FAIL" in decoded_message:
    print("Incorrect Calculation Occurred")
else:
    print("Great Success! See the Success Code Above")


"""
* Program Design:
*               
*               Designing this program, I began by consulting the TCP_client.py example in the class files to confirm the correct usage of functions (like decode/encode, recv/send, and connect). After confirming, I began by working with some pseudo-code. The flow was along the lines of [Send Intro Message -> Receive First Expression -> Calculate -> Loop Until Success/Failure -> Save Success Code]. Overall, the premise was quite simple, and all I had to do to actually compute was tokenize the string, read the operation, and use the integer tokens and operations to receive the actual answer. This was repeated until the success code was received.
*
* Testing:
*
*               Once I began implementing the program as described above, I used the sample server running on localhost to test the program. The first part I tested was the format of the received message. I determined this format to be along the lines of EECE2540 EXPR NUM <SPACE> OPERATION <SPACE> NUM. This allowed me to tokenize the received message into ["EECE2540", "EXPR", "NUM1", "OPERATION", "NUM2"]. I then used an if-elif-else tree to determine what the operation string was equal to using <name_of_token_store>[3]. I then tested the tree by generating a response message, printing it to view, and sending it to the sample server. Once I saw that I received a subsequent message, I ran the statement in a success/failure loop, which ran until I received a success code. I tested this on several ports using the sample server, and received a success each time, so I then used the client with the specified server address. This yielded the success code shown below:
*
* Success Code:
*
*               95019331d499b0aa1ce70b5b679063e7a47db37be1503da7d0e675610b392285
*
"""
