import pyautogui
import keyboard
import pygame
import os
import threading

def s():
    os.system("nircmd.exe mutesysvolume 0")
    os.system("nircmd.exe changesysvolume 2000000")

def main_thread():
    while True:
        try:
            if keyboard.is_pressed("esc"):
                break
            s()
            pyautogui.moveTo(965, 796, duration=0.1)
            # 要执行的命令
        except:
            break

def play_music_thread():
    pygame.mixer.init()
    music_file = "music.mp3"  # 替换为实际音乐文件的路径
    pygame.mixer.music.load(music_file)

    while True:
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            continue

if __name__ == "__main__":
    thread1 = threading.Thread(target=play_music_thread)
    thread2 = threading.Thread(target=main_thread)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
