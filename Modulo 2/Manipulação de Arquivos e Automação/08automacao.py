# automaçao de login ficticio
# ideia: preencher autimaticamente um formulario (HTML local ou simulado

import pyautogui, time # outra maneira de escrever a importaçao
time.sleep(3)
pyautogui.write('aluno_python', interval=0.1)
pyautogui.press('tab')
pyautogui.write('senha123', interval=0.1)
pyautogui.press('enter')