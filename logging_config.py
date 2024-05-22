<<<<<<< HEAD
import logging
import os
import datetime
from logging.handlers import TimedRotatingFileHandler

def set_logger():
    botLogger = logging.getLogger()
    botLogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

    log_dir = os.path.abspath('./noticebot_log')
    os.makedirs(log_dir, exist_ok=True)

    rotatingHandler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, 'webCrawling.log'), when='W0', encoding='utf-8', backupCount=5, atTime=datetime.time(0, 0, 0))
    rotatingHandler.setLevel(logging.DEBUG)
    rotatingHandler.setFormatter(formatter)
    rotatingHandler.suffix = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
    botLogger.addHandler(rotatingHandler)
=======
import logging
import os
import datetime
from logging.handlers import TimedRotatingFileHandler

def set_logger():
    botLogger = logging.getLogger()
    botLogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", "%Y-%m-%d %H:%M:%S")

    log_dir = os.path.abspath('./noticebot_log')
    os.makedirs(log_dir, exist_ok=True)

    rotatingHandler = TimedRotatingFileHandler(
        filename=os.path.join(log_dir, 'webCrawling.log'), when='W0', encoding='utf-8', backupCount=5, atTime=datetime.time(0, 0, 0))
    rotatingHandler.setLevel(logging.DEBUG)
    rotatingHandler.setFormatter(formatter)
    rotatingHandler.suffix = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
    botLogger.addHandler(rotatingHandler)
>>>>>>> 797cf543147b74e777a450c47937e100f11d4061
