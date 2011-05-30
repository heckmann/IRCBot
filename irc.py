import socket

def connect(cmd):
	IRC=socket.socket()
	IRC.connect((cmd.host, cmd.port))
	IRC.send("NICK %s\r\n" % cmd.nick)
	IRC.send("USER %s %s bla :%s\r\n" % (cmd.ident, cmd.host, cmd.rname))
	IRC.send("JOIN #%s\r\n" % cmd.channel)
	
	return IRC