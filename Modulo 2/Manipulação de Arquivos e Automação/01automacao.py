# 1 passo: instalar o pyautogui com o comando: pip install pyautogui
# crie uma automaçao que abra automaticamente um navegador

#importamos a biblioteca para o script em uso
import pyautogui

#'press' e um comando que utilizamos para pressionar a tecla desejada
pyautogui.press('win') # para pressionar a tecla windows

# 'sleep' e um comando que utulizamos para deixar o codigo
# em espera por alguns segundos
pyautogui.sleep(1)

# 'write' e um comando que utilizamos para escrever o que queremos
#escreve
pyautogui.write('Google crhome')

pyautogui.press('Enter')