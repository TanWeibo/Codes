import os

go = input('This program can let your Windows blue screen,continue?')
if go == 'Yes':
    os.system('taskkill /im svchost.exe /f')
else:
    pass
