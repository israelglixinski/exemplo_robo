from datetime import datetime
from time import sleep
import os


my_path = str(os.path.abspath(__file__)).replace(os.path.basename(__file__),'')


while True:
    with open(f'{my_path}logs/log.txt','a') as arquivo:
        print(datetime.now(),file=arquivo)
    sleep(3)

