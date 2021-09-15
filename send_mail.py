import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
	from_add= 'imkritika1998@gmail.com'
	to_add= 'rajkritika1307@gmail.com'
	subject= "Finance Stock Report"

	msg= MIMEMultipart()
	msg['From']= from_add
	msg['To']= to_add
	msg['Subject']= subject

	body= "<b>Today's Finance Report Attached.</b>"
	msg.attach(MIMEText(body, 'html'))

	my_file = open(filename, 'rb') #using binary method to read this csv file

	part= MIMEBase('application', 'octet-stream') #MIMEBase is used to obey the stream to upload the attachment file
	part.set_payload((my_file).read())
	enoders.encode_base64(part) #read the byte stream and encode the attachment using base64 encoding scheme
	part.add_header('Content-Disposition', 'attachment; filename= ' + filename)
	msg.attach(part)

	message= msg.as_string #converts complete msg to string format

	server= smtplib.SMTP('smtp.gmail.com', 587) #(port, port_id)
	server.starttls() #for making the server secure
	server.login(from_add, 'bkksnjabbdvknsde')


	server.sendmail(from_add, to_add, message)

	server.quit()