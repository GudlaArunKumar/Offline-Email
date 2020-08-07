import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('G:/Python projects/EmailProject/venv/index.html').read_text())  # Here we will get whole html file as text and there is dollar sign

email = EmailMessage()
email['from'] = 'Dummy'
email['to'] = ['arunmsd02@gmail.com']
# ['soumya.sangote@gmail.com','arunmsd02@gmail.com','suprithatn@gmail.com']
email1 = EmailMessage()
email1['from'] = 'andrei@zerotomastery.io'
email1.get_content()


email['subject'] = 'You won 1 Lakh rupees!'

email.set_content(html.substitute(name = 'Enjoy'),'html')  # name will replaced in $ sign in html file


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('dummymailfromarun@gmail.com','dummy@1234')
    smtp.send_message(email)
    print(email1)
    print('Email Sent..Wow!')