<<<<<<< HEAD
import time
import win32con
import win32api
import win32gui
import logging

idx = 0

def kakao_sendtext(chatroom_name, noticeList):
    hwndMain = win32gui.FindWindow(None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)

    global idx
    check = len(noticeList)

    if idx < check:
        for i in range(idx, check):
            notice_text = f"{noticeList[i]['title']} - {noticeList[i]['link']}"
            win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, notice_text)
            SendReturn(hwndEdit)
            logging.debug(notice_text)
            time.sleep(3)
        idx = check

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def open_chatroom(chatroom_name):
    hwndkakao = win32gui.FindWindow(None, "카카오톡")

    hwnd_chat = win32gui.FindWindow(None, chatroom_name)
    if hwnd_chat == 0:
        hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
        hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
        hwndkakao_edit2_2 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
        hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

        win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
        time.sleep(1)
        SendReturn(hwndkakao_edit3)
        time.sleep(1)
        hwnd_chat = win32gui.FindWindow(None, chatroom_name)
=======
import time
import win32con
import win32api
import win32gui
import logging

idx = 0

def kakao_sendtext(chatroom_name, noticeList):
    hwndMain = win32gui.FindWindow(None, chatroom_name)
    hwndEdit = win32gui.FindWindowEx(hwndMain, None, "RICHEDIT50W", None)

    global idx
    check = len(noticeList)

    if idx < check:
        for i in range(idx, check):
            notice_text = f"{noticeList[i]['title']} - {noticeList[i]['link']}"
            win32api.SendMessage(hwndEdit, win32con.WM_SETTEXT, 0, notice_text)
            SendReturn(hwndEdit)
            logging.debug(notice_text)
            time.sleep(3)
        idx = check

def SendReturn(hwnd):
    win32api.PostMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.01)
    win32api.PostMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

def open_chatroom(chatroom_name):
    hwndkakao = win32gui.FindWindow(None, "카카오톡")

    hwnd_chat = win32gui.FindWindow(None, chatroom_name)
    if hwnd_chat == 0:
        hwndkakao_edit1 = win32gui.FindWindowEx(hwndkakao, None, "EVA_ChildWindow", None)
        hwndkakao_edit2_1 = win32gui.FindWindowEx(hwndkakao_edit1, None, "EVA_Window", None)
        hwndkakao_edit2_2 = win32gui.FindWindowEx(hwndkakao_edit1, hwndkakao_edit2_1, "EVA_Window", None)
        hwndkakao_edit3 = win32gui.FindWindowEx(hwndkakao_edit2_2, None, "Edit", None)

        win32api.SendMessage(hwndkakao_edit3, win32con.WM_SETTEXT, 0, chatroom_name)
        time.sleep(1)
        SendReturn(hwndkakao_edit3)
        time.sleep(1)
        hwnd_chat = win32gui.FindWindow(None, chatroom_name)
>>>>>>> 797cf543147b74e777a450c47937e100f11d4061
