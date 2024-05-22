import time
import datetime
import win32con
import win32api
import win32gui
import os
import json
import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from apscheduler.schedulers.background import BackgroundScheduler
from logging.handlers import TimedRotatingFileHandler

# # 카톡창 이름, (활성화 상태의 열려있는 창)
kakao_opentalk_name = 'test'
idx = 0



# # 채팅방에 메시지 전송
def kakao_sendtext(chatroom_name, noticeList):
    try:
         # # 핸들 _ 채팅방
        hwndMain = win32gui.FindWindow(None, chatroom_name)
        hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)

        check = len(noticeList)
        global idx

        if(idx < check):
            for i in range(idx, check):
                win32api.SendMessage(
                    hwndEdit, win32con.WM_SETTEXT, 0, noticeList[i])
                SendReturn(hwndEdit)
                botLogger = logging.getLogger()
                botLogger.debug(noticeList[i])
                time.sleep(3)
        idx = check
    except Exception as e:
        logging.exception("Failed to send text to Kakao chatroom")


# # 엔터
def SendReturn(hwnd):
    try:
        win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
        time.sleep(0.01)
        win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    except Exception as e:
        logging.exception("Failed to send return key")



# # 채팅방 열기
def open_chatroom(chatroom_name):
    # # # 채팅방 목록 검색하는 Edit (채팅방이 열려있지 않아도 전송 가능하기 위하여)
    try:
        hwndkakao = win32gui.FindWindow(None, "카카오톡")
        hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
        hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
        hwndkakao_edit2_2 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
        hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

         # # Edit에 검색 _ 입력되어있는 텍스트가 있어도 덮어쓰기됨
        win32api.SendMessage(
            hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
        time.sleep(1)
        SendReturn(hwndkakao_edit3)
        time.sleep(1)
    except Exception as e:
        logging.exception("Failed to open Kakao chatroom")
        

"""" -- 이전버전


# 공지사항 크롤링하기
def get_all_notices():
    # Chrome 드라이버 설정
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    today = datetime.date.today().strftime("%Y-%m-%d")

    # 원하는 URL 열기
    driver.get('https://www.daegu.ac.kr/article/DG159/list?pageIndex=1&')

    # 모든 공지사항 요소 가져오기
    notice_elements = driver.find_elements(By.CSS_SELECTOR, '#sub_contents > div > table > tbody > tr')
    
    # 공지사항을 담을 리스트 초기화
    all_notices = []

    # 각 공지사항 요소에서 제목과 링크 추출하여 리스트에 추가
    for idx, element in enumerate(notice_elements, start=1):
        if idx <= 12:  # 12번째 공지사항은 리스트에 추가하지 않음
            continue
        title_element = element.find_element(By.CSS_SELECTOR, 'td.list_left > a')
        date_element = element.find_element(By.CSS_SELECTOR, 'td:nth-child(5)')  # 공지사항의 날짜 요소 선택
        title = title_element.text.strip()
        date = date_element.text.strip()
        link = title_element.get_attribute('href')

        if date == today:
            all_notices.append({'date': date, 'title': title, 'link': link})    # 브라우저 닫기
    
    driver.quit()

    return all_notices
"""


# 공지사항 크롤링하기
def get_all_notices():
    driver = None
    try:
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        today = datetime.date.today().strftime("%Y-%m-%d")
        driver.get('https://www.daegu.ac.kr/article/DG159/list?pageIndex=1&')

        notice_elements = driver.find_elements(By.CSS_SELECTOR, '#sub_contents > div > table > tbody > tr')
        all_notices = []

        for idx, element in enumerate(notice_elements, start=1):
            if idx <= 12:
                continue
            title_element = element.find_element(By.CSS_SELECTOR, 'td.list_left > a')
            date_element = element.find_element(By.CSS_SELECTOR, 'td:nth-child(5)')
            title = title_element.text.strip()
            date = date_element.text.strip()
            link = title_element.get_attribute('href')

            if date == today:
                all_notices.append({'date': date, 'title': title, 'link': link})
    except Exception as e:
        logging.exception("Failed to get notices")
    finally:
        if driver:
            driver.quit()
    
    return all_notices


""" -- 이전버전
def save_notices_to_json(notices, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(notices, json_file, ensure_ascii=False, indent=4)
"""    

def save_notices_to_json(notices, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as json_file:
            json.dump(notices, json_file, ensure_ascii=False, indent=4)
    except Exception as e:
        logging.exception("Failed to save notices to JSON")


""" -- 이전버전
def load_notices_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []
"""
    

def load_notices_from_json(file_path):
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except Exception as e:
            logging.exception("Failed to load notices from JSON")
    return []


def filter_new_notices(new_notices, existing_notices):
    existing_titles = {notice['title'] for notice in existing_notices}
    filtered_notices = [
        notice for notice in new_notices if notice['title'] not in existing_titles]
    return filtered_notices

def job():
    file_path = os.path.join(current_dir, 'notices.json')
    existing_notices = load_notices_from_json(file_path)
    new_notices = get_all_notices()
    filtered_notices = filter_new_notices(new_notices, existing_notices)

    if filtered_notices:
        save_notices_to_json(existing_notices + filtered_notices, file_path)
        open_chatroom(kakao_opentalk_name)  # 채팅방 열기
        kakao_sendtext(kakao_opentalk_name, filtered_notices)


# # log 환경설정
def set_logger():
    botLogger = logging.getLogger()

    # setting log file level -> DEBUG
    botLogger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s",
                                  "%Y-%m-%d %H:%M:%S")

    # 일주일에 한번 월요일 자정에 로그 파일 새로 생성. 최대 5개까지 파일 관리.
    rotatingHandler = TimedRotatingFileHandler(
        filename='./noticebot_log/webCrawling.log', when='W0', encoding='utf-8', backupCount=5, atTime=datetime.time(0, 0, 0))
    rotatingHandler.setLevel(logging.DEBUG)
    rotatingHandler.setFormatter(formatter)

    # 파일 이름 suffix 설정 (webCrawling.log.yyyy-mm-dd-hh-mm 형식)
    rotatingHandler.suffix = datetime.datetime.today().strftime("%Y-%m-%d-%H-%M")
    botLogger.addHandler(rotatingHandler)


def main():
    global current_dir
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sched = BackgroundScheduler()
    sched.start()
    set_logger()

    # 15분마다 실행
    sched.add_job(job, 'interval', minutes=15)

    while True:
        botLogger = logging.getLogger()
        botLogger.debug("-------------실행 중-------------")
        time.sleep(900)


if __name__ == '__main__':
    main()
