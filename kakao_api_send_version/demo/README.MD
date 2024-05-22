# 학교 공지 봇 만들기

<br>

> Developer 👩‍💻

- `ChanghyeonP` : 카카오API연동, 작업 알고리즘 구현, 크롤링 구현 로그파일 및 카카오 api json 자동생성 



<br>

> Tech Stack 🛠

- Language : Python
- Library : beautifulsoup4, requests, apscheduler
- Server : AWS EC2 (Free-tier)

<br>

> Process 💻

1. 카카오 API 사용하여 카카오톡 나와 채팅을 제어해 크롤링한 공지사항을 전송한다
2. [학교 공식 홈페이지 공지사항](https://daegu.ac.kr/article/DG159/list)을 크롤링하여 공지사항 리스트를 가져온 후, JSON 리스트 형태로 가공한다.
3. 알고리즘을 사용하여 실시간으로 받아온 공지 데이터가 이미 전송된 공지사항인지 체크한다.
4. 스케줄러를 사용해 공지사항 올라오는 주기를 고려하여 작업 시간을 설정한다.
5. 작업 시간마다 새롭게 올라온 공지사항을 메세지로 전송한다.


// 단톡방, 오픈채팅 전송 api가 없는 관계로 나와의 채팅과 연동시켰음
// 추후 챗봇을 이용하여 개발 예정

<br>



