import pyautogui
import webbrowser
import time

# passo 1: Abri o youtube com uma musica especifica
url = 'https://www.youtube.com/watch?v=gqt0BC2bkJY&list=RDgqt0BC2bkJY&start_radio=1'
webbrowser.open(url)

# Passo2: aguardar o carregamento da pagina 
time.sleep(5) # ajustar de acordo com a velocidade da internet utilizada

# passo 3: garantir que o video comece (aperte o espaço para ' play')
pyautogui.press('space') # toca ou pausa o video