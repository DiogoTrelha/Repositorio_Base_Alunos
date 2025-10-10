import pyautogui
import time


pyautogui.PAUSE = 0.5


pyautogui.hotkey('win', 'r')
time.sleep(1)


pyautogui.write('calc')
pyautogui.press('enter')
time.sleep(2)  


pyautogui.press('8')
pyautogui.press('+')
pyautogui.press('2')
pyautogui.press('enter')