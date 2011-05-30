import os
import daemon
import command


#http://www.python.org/dev/peps/pep-3143/
with daemon.DaemonContext:
	do_main_program()