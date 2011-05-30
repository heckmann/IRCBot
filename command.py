# http://www.doughellmann.com/PyMOTW/argparse/
import argparse

def commands():
	parser = argparse.ArgumentParser()
#IRC
	parser.add_argument('--server', action='store', dest='host', help='the IRC server', default="irc.freenode.net")
	parser.add_argument('--port', action='store', dest='port', type=int, help='the IRC port', default=6667)
	parser.add_argument('--nick', action='store', dest='nick', help='the IRC nick', default="My_Bot")
	parser.add_argument('--ident', action='store', dest='ident', help='the IRC ident', default="mybot")
	parser.add_argument('--real', action='store', dest='rname', help='your IRC real name', default="My real Bot")
	parser.add_argument('--channel', action='store', dest='channel', help='the IRC channel', default="irclib")
#DAEMON
	parser.add_argument('-D', action='store_true', default=False, dest='deactivateDeamon', help='Deactivate deamon')
#MAIL
	parser.add_argument('--mhost', action='store', dest='mhost', help='your eMail host')
	parser.add_argument('--maddress', action='store', dest='maddress', help='your eMail address')
	parser.add_argument('--musername', action='store', dest='musername', help='your eMail username')
	parser.add_argument('--mpass', action='store', dest='mpassword', help='your eMail password')
	parser.add_argument('--msubject', action='store', dest='mail_subject', help='the eMail subject', default="Log from Chat")
#PLUGIN
	parser.add_argument('--plugin', action='store', dest='plugin', help='logging plugin', default="db")

	return parser.parse_args()