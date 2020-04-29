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
  return names,emails

def message_content(filename):
  # content = open(filename,mode="r",encoding="utf-8").read()
  # return content
  with open(filename, 'r', encoding='utf-8') as template_file:
    template_file_content = template_file.read()
  return Template(template_file_content)

from string import Template

def main():
  names, emails = email_list('receivers.txt')
  message_text = message_content('message.html')

  gmail_user = <your_email_id>
  gmail_password = <your_email_password>

  server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
  server.login(gmail_user, gmail_password)

  for name, email in zip(names, emails):
    msg = MIMEMultipart()

    msg['From']=<your_name>
    msg['To']=email
    msg['Subject']="Testing emails using python"

    message = message_text.substitute(PERSON_NAME=name.title())
    msg.attach(MIMEText(message,'html'))

    image = MIMEImage(open('ok.jpg', 'rb').read(), name='Attachment_image.jpg')
    msg.attach(image)  
    
    server.send_message(msg)

    del msg
    
    print("Message sent to " + name)
  server.quit()

if __name__ == '__main__':
  main()