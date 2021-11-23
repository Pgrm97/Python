import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'xyz name'
email['to'] = 'pgrm97@gmail.com'
email['subject'] = 'Important Message'
email.set_content("This is a message for Pedro Guillermo's email")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls() #Send data between server and client
    smtp.login("pedro@gmail.com", "Password")
    smtp.send_message(email)
    print("email sent")