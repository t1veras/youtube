#Thiago Veras 05/04/2023

#https://www.twilio.com/

#thiago.zrx@outlook.com.br
#y*Yy8D&CP^nzSv3123

#sudo apt --fix-broken install

#sudo apt install python3
#sudo apt install python3-pip
#pip3 install twilio

from twilio.rest import Client

SID = 'ACab52d9534ed75d09187f7f04f29d9a03'
Auth_Token = 'c1e6c716f001dc249daaaaf4fe53a7ef'

cl = Client(SID, Auth_Token)

cl.messages.create(body='oi', from_='+15153258211', to='+5511992174289')