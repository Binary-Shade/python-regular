import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass

def send_email(sender_email, sender_passwd, receiver_email, subject, message): #function for sender and receiver details
    msg = MIMEMultipart() #used for to initialize the multipart of the creds
    msg['From']=sender_email
    msg['To']=receiver_email
    msg['Subject']=subject

    body = MIMEText(message, 'plain') #which converts the msg into plain
    msg.attach(body) #attach the plain into body

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587) #the smtp send mail through the domain and the port 587
        server.starttls() #provides the secure connection via transport layer security
        server.login(sender_email,sender_passwd) #login into your acccount
        server.send_message(msg) #send the mail
        print("e-mail sent successfully")
    except Exception as e:
        print("error occured while sending the e-mail"+str(e)) #catch the exception and return as a string
    finally:
        server.quit()

sender_email=input("Enter your G-mail :") #change your email
sender_passwd=getpass.getpass("Enter your app-password :") #two step verification must be enables get it from account/app-password
receiver_email=input("Enter receiver E-mail :") #change receiver email
subject=input("Enter the Subject :")
message=input("Enter the message :")
send_email(sender_email,sender_passwd,receiver_email,subject,message)
    

