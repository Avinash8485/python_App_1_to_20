import smtplib as sp
import imghdr # type: ignore
from email.message import EmailMessage


username = "avinashvel8485@gmail.com"
password = os.getenv("PASSWORD")

def send_email(image_with_object):
    email_mess = EmailMessage()
    email_mess["Subject"] = "New customer showed up!"
    email_mess.set_content("hey ,we saw a new customer")

    with open(image_with_object,"rb") as file: #reading binary mode(rb)
        context = file.read()

    email_mess.add_attachment(context,maintype ="image",subtype =imghdr.what(None,context))
     
    gmail = sp.SMTP("smpt.gamil.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(username,password)
    gmail.sendmail(username,username,email_mess.as_string())#first parameter is sender and second is receiver
    gmail.quit()

if __name__ == "__main__":
    send_email(image_with_object="images/20.png")