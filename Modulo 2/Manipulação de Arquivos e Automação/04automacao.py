# crie uma automaçao que escreva um texto automaticamente
import pyautogui
import time


# observaçao: abra um bloco de notas vazio
# aguarde 5 segundos para voce abrir o bloco de notas
time.sleep(5)

# escreva o texto
pyautogui.write('eu nao tenho inimigos', interval=0.1)