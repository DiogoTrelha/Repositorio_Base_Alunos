# comando para encontra a posiçao x e y do mouse para uma automaçao

import pyautogui
import time

print('voce tem 5 segundos para posicionar o mouse sobre o botao escrever...')
time.sleep(5)
print('posiçao do mouse', pyautogui.position())