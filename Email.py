import smtplib
import email
import email.mime.multipart
import email.mime.text
import email.mime.base
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


print("\n")
print("{:^80}".format("AGUARDE, NAO FECHE ESTA JANELA!!!"))
print("")
print("{:^70}".format("               .-.-.-._."))
print("{:^70}".format("                .~\ /~\_/ \_."))
print("{:^70}".format("              .~\_/~\_/ \_/~\_."))
print("{:^70}".format("               .~\_/ \_/ \_/ \_/~\."))
print("{:^70}".format("   .----.      /\_/ \_/ \_/ \_/ \_/\."))
print("{:^70}".format("   /(o)(o)`\__ /_/ \_/ \_/ \_/ \_/ \_\."))
print("{:^70}".format("  |           \_/ \_/ \_/ \_/ \_/ \\. \."))
print("{:^70}".format("        \ \__/      |\_/ \_/ \_/ \_/ \_/ \_/~\...'"))
print("{:^70}".format("           `----´`----\/_\-/-\_/-\-/ \_/-\_.-/''''"))
print("{:^70}".format("              /~/===| |=====| |==\~\ "))
print("{:^70}".format("            _/ /   _| |    _| |   \ \ "))
print("{:^70}".format("           (___|  (___|   (___|  (___|"))
print("\n\n")
print("{:^80}".format("ENVIANDO E-MAIL COM ALERTA DE INATIVIDADE NA PASTA"))
print("{:^80}".format("DO SERVIDOR DE IMAGENS DO DIRETÓRIO I:/"))
 
# create message object instance
msg = MIMEMultipart()
 
 
message = "Thank you"
 
# setup the parameters of the message
password = "gleci@gl3c1"
msg['From'] = "administrador@gleci.com.br"
msg['To'] = "administrador@gleci.com.br"
msg['Subject'] = "teste"
 
# add in the message body
msg.attach(MIMEText(message, 'plain'))
 
#create server
server = smtplib.SMTP('mail.gleci.com.br: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())

 
server.quit()

 
print("\t   E-mail enviado com sucesso para", msg['To'])
