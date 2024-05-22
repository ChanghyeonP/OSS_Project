import requests
import datetime
import json
import os
import re
from bs4 import BeautifulSoup
from openai import OpenAI


def get_today_notices():
    today = datetime.date.today().strftime("%Y-%m-%d")
    
    url = 'https://www.daegu.ac.kr/article/DG159/list?pageIndex=1&'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    today_notices = []
    
    notice_elements = soup.select('#sub_contents > div > table > tbody > tr')

    for idx, element in enumerate(notice_elements, start=1):
        if idx <= 12:
            continue
        title_element = element.select_one('td.list_left > a')
        date_element = element.select_one('td:nth-child(5)')
        title = title_element.text.strip()
        title = re.sub(r'[\n\t\r]+', ' ', title)
        date = date_element.text.strip()
        onclick = title_element.get('onclick', "")
        onclick_number = re.sub(r'[^0-9]', '', onclick)
        link = f"https://www.daegu.ac.kr/article/DG159/detail/{onclick_number}"

        if today == date:
            notice_text = f"{title} - {link}"
            summary = get_summary(notice_text)
            today_notices.append({'date': date, 'title': title, 'link': link, 'summary': summary})
    
    today_notices.reverse()
    return today_notices


def get_summary(text):
    client = OpenAI(api_key="Your-Key")
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"다음 공지사항의 요약을 3줄 이내로 작성해줘: {text}"}
        ],
    )
    summary = response.choices[0].message.content.strip()
    return summary

def save_notices_to_json(notices, file_path):
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(notices, json_file, ensure_ascii=False, indent=4)

def load_notices_from_json(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as json_file:
            return json.load(json_file)
    return []

# Example usage
file_path = 'notices.json'
notices = get_today_notices()
save_notices_to_json(notices, file_path)
