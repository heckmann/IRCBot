import os
import daemon
import command
import irc
import db

def main_loop(cmd):
	# connect to irc channel
	IRC = connect(cmd)
	DB = connect_DB("path")
	
if __name__ == "__main__":
	cmd = commands()

	if not cmd.deactivateDeamon:
		#http://www.python.org/dev/peps/pep-3143/
		with daemon.DaemonContext:
			print "main as deamon"
			main_loop(cmd)
	else:
		print "main"
		main_loop(cmd)