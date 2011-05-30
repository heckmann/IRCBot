import socket
import string
import mail

def connect(cmd):
	IRC=socket.socket()
	IRC.connect((cmd.host, cmd.port))
	IRC.send("NICK %s\r\n" % cmd.nick)
	IRC.send("USER %s %s bla :%s\r\n" % (cmd.ident, cmd.host, cmd.rname))
	IRC.send("JOIN #%s\r\n" % cmd.channel)
	
	return IRC
	
def loop(IRC, LOG, DB_path, cmd):
	read=""
	
	while 1:
		read=read + IRC.recv(1024)
		puffer=string.split(read, "\n")
		read=puffer.pop()
		
		for message in puffer:
			message=string.rstrip(message)
			message=string.split(message)
			
			if(message[0]=="PING"):
				IRC.send("PONG %s\r\n" % message[1])
			
			elif ((message[1] == "PART") | (message[1] == "JOIN")):
				LOG.add(DB_path, message[1], message[0].split("!")[0][1:], message[2])

			elif ((message[1] == "PRIVMSG") & (message[2] == cmd.nick)):
				LOG.add(DB_path, message[1], message[0].split("!")[0][1:], " ".join(message[3:]))
				
				if (message[3][1:] == "mail"):
					if cmd.mhost:
						if cmd.maddress:
							send(cmd, message[4], DB_path)

				elif (message[3][1:] == "stalk"):
					if len(message) > 4:
						seen = LOG.saw(DB_path, message[4])
						IRC.send("PRIVMSG %s :%s\r\n" % (message[0].split("!")[0][1:], seen))