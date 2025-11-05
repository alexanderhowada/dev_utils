import pyperclip, pyautogui


pyperclip.copy('spark.sql(f"""\nSELECT\n*\nFROM {}\n""").display()')
pyautogui.hotkey('ctrl', 'v')
