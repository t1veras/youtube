#Thiago Veras 05/04/2023

#gmail.com

#t1veras.office@gmail.com
#qeovdner149t6R.

#rdhydkahwvzectcc

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip

#security->two-step verification((11) 94561-1023)
#two-step verification->app passwords(other)

import smtplib, ssl

sender = 't1veras.office@gmail.com'
password = 'rdhydkahwvzectcc'
receiver = 'thiago.web.w@gmail.com'

body_msg = '''test'''

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, body_msg)