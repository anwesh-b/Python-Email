import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def email_list(filename):
  names = []
  emails = []
  with open(filename, mode="r", encoding="utf-8") as receiver_list:
    for receiver in receiver_list:
      names.append(receiver.split()[0])
      emails.append(receiver.split()[1])
  #Return the name and email of the receiver
  return names,emails

def message_content(filename):
  #Donot use this method as it returns a string
  # content = open(filename,mode="r",encoding="utf-8").read()
  # return content
  
  with open(filename, 'r', encoding='utf-8') as template_file:
    template_file_content = template_file.read()
  #Return the message contents as an object
  return Template(template_file_content)

def main():
  #Read the message and receiver list
  names, emails = email_list('receivers.txt')
  message_text = message_content('message.html')

  #Adding the credentials
  gmail_user = <your_email_id>
  gmail_password = <your_email_password>

  #Setup SMTP client
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(gmail_user, gmail_password)

  for name, email in zip(names, emails):
    #Create empty message
    msg = MIMEMultipart()

    #Add different parameters to the message
    msg['From']=<your_name>
    msg['To']=email
    msg['Subject']="Testing emails using python"

    #Replace the Name of receiver in the message and add it to message
    message = message_text.substitute(PERSON_NAME=name.title())
    msg.attach(MIMEText(message,'html'))

    #Add an image as an attatchment
    image = MIMEImage(open('ok.jpg', 'rb').read(), name='Attachment_image.jpg')
    msg.attach(image)  
    
    #Send the message
    server.send_message(msg)

    #Free up the message variable
    del msg
    
    print("Message sent to " + name)
  #End the SMTP connection
  server.quit()

if __name__ == '__main__':
  main()