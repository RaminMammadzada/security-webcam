import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
 
def sendThroughEmail():
    fromaddr = "WRITE YOUR EMAIL HERE"
    toaddr = "WRITE THE EMAIL YOU WANT TO SEND TO"
    
    msg = MIMEMultipart()
    
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "ABNORMAL SITUATION"
    
    body = "Something unusual happened. You can check the shot from attachment."
    
    msg.attach(MIMEText(body, 'plain'))
    
    filename = "main_image.jpg"
    attachment = open("main_image.jpg", "rb")
    
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    
    msg.attach(part)
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "WRITE YOUR EMAIL'S PASSWORD HERE")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()