# importamos a biblioteca pyautogui
# crie uma automacao que faça o mouse se mover na forma de um quadrado
import pyautogui

for i in range(10):
    # a funçao .moveTo e uma funçao para movimentos de mouse
    #pyautogui.moveTo(x,y,duration=em segundos)
    pyautogui.moveTo(100 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 100 + 10 * i, duration=0.25)
    pyautogui.moveTo(200 + 10 * i, 200 + 10 * i, duration=0.25)
    pyautogui.moveTo(100 + 10 * i, 200 + 10 * i, duration=0.25)
    
    