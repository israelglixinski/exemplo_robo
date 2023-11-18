from datetime import datetime
from time import sleep


while True:
    with open('./logs/log.txt','a') as arquivo:
        print(datetime.now(),file=arquivo)
    sleep(3)




