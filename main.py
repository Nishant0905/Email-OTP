import random
import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)

server.starttls()

server.login('nishantsreekumar14@gmail.com',' dysz kbpo fzdc slgd ')

otp=''.join([str(random.randint(0,9)) for i in range(6)])
msg = 'Hello,Thank You for using our website, Your OTP is '+str(otp)
sender = 'nishantsreekumar14@gmail.com'
receiver = 'nishantsreekumar@gmail.com'

server.sendmail(sender, receiver, msg)
server.quit()
