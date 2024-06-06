import keyboard
import pyautogui

while True:
	if keyboard.is_pressed('w'):
		pyautogui.scroll(65)
	if keyboard.is_pressed('s'):
		pyautogui.scroll(-65)
	if keyboard.is_pressed('esc'):
		break