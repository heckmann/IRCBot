import os
import smtplib
 
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.Utils import formatdate

# source: http://www.blog.pythonlibrary.org/2010/05/14/how-to-send-email-with-python/
 
def send(cmd, target, filePath):
	mail = MIMEMultipart()
	mail["From"] = cmd.maddress
	mail["To"] = target
	mail["Subject"] = cmd.msubject
	mail['Date'] = formatdate(localtime=True)
 
	part = MIMEBase('application', "octet-stream")
	part.set_payload( open(filePath,"rb").read() )
	Encoders.encode_base64(part)
	part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(filePath))
	mail.attach(part)
 
	server = smtplib.SMTP(cmd.mhost)
	if ((cmd.musername) & (cmd.mpassword)):
		server.login(cmd.musername, cmd.mpassword)

	try:
		failed = server.sendmail(cmd.maddress, target, mail.as_string())
		server.close()
	except Exception, e:
		errorMsg = "Could not send your email. Error: %s" % str(e)