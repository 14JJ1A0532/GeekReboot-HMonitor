import smtplib
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'chandanakandagatla1@gmail.com'
PASSWORD = 'XXXXXXXX'

def get_contacts(filename):
    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """
    
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails
	
def sendMail(mapString):
	print(mapString)
	names, emails = get_contacts('myContacts.txt') 
	
	# set up the SMTP server
	s = smtplib.SMTP(host='smtp.gmail.com', port=587)
	s.starttls()
	s.login(MY_ADDRESS, PASSWORD)

	# For each contact, send the email:
	for name, email in zip(names, emails):
		msg = MIMEMultipart()       # create a message

		# setup the parameters of the message
		msg['From']=MY_ADDRESS
		msg['To']=email
		msg['Subject']="URGENT: People Gathering Alert"

		# Create the body of the message (a plain-text and an HTML version).
		# link = '<a href="{0}">{1}</a>'.format(destination, description)
		html = """\
            <html>
              <head></head>
              <body>
                <p>Heyy!!!<br>
                   Here is the link <a href="{str1}">Open Map Link</a>
                </p>
              </body>
            </html>
            """.format(str1 = mapString)

        # Record the MIME types of both parts - text/plain and text/html.
		part1 = MIMEText(html, 'html')

        # Attach parts into message container.
        # According to RFC 2046, the last part of a multipart message, in this case
        # the HTML message, is best and preferred.
		msg.attach(part1)
        
        # send the message via the server set up earlier.
		s.send_message(msg)
		del msg
        
    # Terminate the SMTP session and close the connection
	s.quit()
