import os
#http://pypi.python.org/pypi/python-daemon/
import daemon
import command
import irc
import imp
import sys

def plugin(name, path):
	try:
		return sys.modules[name]
	except KeyError:
		pass

	file, path_name, description = imp.find_module(name, [path])#[os.path.join(head, "plugins")])
	
	try:
		return imp.load_module(name, file, path_name, description)
	finally:
		if file:
			file.close()

def main_loop(cmd):
	# connect to irc channel
	IRC = irc.connect(cmd)
	
	LOG = plugin(cmd.plugin, os.path.dirname(cmd.path))
	DB_path = os.path.join(os.path.dirname(cmd.path), "db." + cmd.plugin)
	
	LOG.connect_DB(DB_path)
	
	irc.loop(IRC, LOG, DB_path, cmd)
	
	
if __name__ == "__main__":
	cmd = command.commands()
	cmd.path = os.path.abspath(sys.argv[0])
	
	if not cmd.deactivateDeamon:
		#http://www.python.org/dev/peps/pep-3143/
		with daemon.DaemonContext():
			print "main as deamon"
			main_loop(cmd)
	else:
		print "main"
		main_loop(cmd)