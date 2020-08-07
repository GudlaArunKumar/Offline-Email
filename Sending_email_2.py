import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('G:/Python projects/EmailProject/venv/index.html').read_text())  # Here we will get whole html file as text and there is dollar sign

email = EmailMessage()
email['from'] = 'Dummy'
email['to'] = ['email1','email2','email3'] # Here we can add any number of emails to list or text file with list of emails can be given


email['subject'] = 'You won 1 Lakh rupees!'

email.set_content(html.substitute(name = 'Enjoy'),'html')  # name will replaced in $ sign in html file


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:  #using gmail as host server through port 587
    smtp.ehlo()
    smtp.starttls()
    smtp.login('user email id,'user password')
    smtp.send_message(email)
    print('Email Sent..Wow!')
