import datetime
from os.path import isfile

def connect_DB(database):
	if not isfile(database):
		f = open(database, 'w')
		f.write("Format of this log:\n" + "order/action\n" + "who did it\n" + "coresponding message\n" + "when took it place\n\n")
		f.close()
	
def add(database, order, who, message):
	f = open(database, 'a')
	f.write(order + "\n" + who + "\n" + message + "\n" + datetime.datetime.today().isoformat() + "\n")
	f.close()
	
def saw(database, person):
	f = open(database, 'r')
	lines = f.readlines()
	f.close()

	for i in xrange(len(lines)-3, 0, -4):
		if (lines[i][0:len(person)] == person):
			return lines[i+2]
			
	return "?"