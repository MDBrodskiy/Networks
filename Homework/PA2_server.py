"""
 * ===============================================================
 *
 *       Filename:  PA2_server.py
 *       Assignment: Computing Homework 2
 *       Title: Python TCP Server
 *
 *    Description:  Acts as a TCP server for provided client program
 *
 *        Version:  1.0
 *        Created:  10/30/2023
 *       Revision:  N/A
 *         Python:  Python 3.9.2
 *
 *         Author:  M.Brodskiy
 *
 * ===============================================================
""" 

# Indicate start of program
print("Started TCP Server Program")

# Import necessary socket utilities
from socket import *

# Establish address and port number
address = 'localhost'
port = 12005
identity = (address, port)

# Create server socket
server = socket(AF_INET, SOCK_STREAM)
server.bind(identity)
print("Server socket created at:", identity)

# List for at most 5 connections
server.listen(5)
print("Server listening for connections")

# Create a loop for persistent connection
persist = True
while persist:

    # Obtain new connections
    connection, client = server.accept()
    print("Created connection socket for client at:", client)

    # Get message from client
    message = connection.recv(2048)

    # Change the message to a string
    recv_string = message.decode()
    print("Received string:", recv_string)

    # Split the string using - as delimiter
    num_list = recv_string.split("-")
    sum_of_list = 0
    for i in num_list:
        sum_of_list += int(i)

    # Check for message to end loop
    if recv_string.lower() == "close":
        print("Closing Connection!")

        # Create string to send back
        sent_string = "Closed!"

        # End the connection
        persist = False

    else:
        # Change the string
        sent_string = recv_string.upper()

    # Send Result with summation
    sent_string = "RESULT:" + str(sum_of_list)

    # Encode to a message
    send_to_client = sent_string.encode()
    print("Sent string:", sent_string)

    # Send message to client
    connection.send(send_to_client)
    print("Server sent message to client at:", client)

    # Close the connection
    connection.close()

# Close the server socket
server.close()
print("Server closed")
