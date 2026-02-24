import pyperclip
import pyautogui
import time

previous_clipboard = pyperclip.paste()

snippet = 'spark.sql(f"""\nSELECT\n*\nFROM {}\n""").display()'
pyperclip.copy(snippet)
pyautogui.hotkey('ctrl', 'v')


time.sleep(0.2)
pyperclip.copy(previous_clipboard)
