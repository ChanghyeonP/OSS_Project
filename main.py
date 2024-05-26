import time
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from crawling import get_today_notices, save_notices_to_json, load_notices_from_json
from kakao_open import open_chatroom, kakao_sendtext
from logging_config import set_logger

kakao_opentalk_name = 'test'

def job():
    open_chatroom(kakao_opentalk_name)
    noticeList = get_today_notices()
    save_notices_to_json(noticeList, 'notices.json')
    loaded_notices = load_notices_from_json('notices.json')
    kakao_sendtext(kakao_opentalk_name, loaded_notices)

def main():
    set_logger()
    sched = BackgroundScheduler()
    sched.start()
    sched.add_job(job, 'interval', minutes=15)
    botLogger = logging.getLogger()

    while True:
        botLogger.debug("-------------실행 중-------------")
        time.sleep(900)

if __name__ == '__main__':
    main()
