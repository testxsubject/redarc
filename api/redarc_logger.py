import datetime
import logging
import os

def init_logger(name):
   if not os.path.exists('logs'):
      os.makedirs('logs')
   logger = logging.getLogger(name)
   time_now  = datetime.datetime.now().strftime('%m_%d_%Y_%H_%M_%S') 
   logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', filename='logs/redarc_api-'+time_now+'.log', encoding='utf-8', level=logging.DEBUG, datefmt='%Y-%m-%d %H:%M:%S')
   return logger