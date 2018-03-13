
import os

TARGET_PATH = './jupyters/'
for n, x in enumerate(os.listdir(TARGET_PATH)):
    if x.split('.')[1] != 'ipynb':
        continue
    rx = x.replace(r' ', r'\ ')
    fileName = rx.split('.')[0]
    os.system('jupyter-nbconvert --to html ' + TARGET_PATH + rx)
    os.system('mv ' + fileName + '.html' + ' ./html/' + fileName + '.html')
