import datetime
from web import message_send_logger
from utils import web_utils, config


while True:
    # get current time
    curr_time = datetime.datetime.now()
    
    # run origato bot
    if curr_time.hour == 16 and curr_time.minute == 00:
        exec(open("main.py").read())

