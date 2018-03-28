
import os
import sys
import time
from os.path import join as pjoin

convert_all = sys.argv[1] == 'all'

jupyter_dir = './jupyters/'
html_dir = './html/'
for n, ipy_fname in enumerate(os.listdir(jupyter_dir)):
    if ipy_fname.split('.')[1] != 'ipynb':
        continue
    file_no_ext = ipy_fname.split('.')[0]
    
    # Check modification time
    source_ipynb_path = pjoin(jupyter_dir, '{}'.format(ipy_fname))
    source_html_path = pjoin(jupyter_dir, '{}.html'.format(file_no_ext))
    target_html_path = pjoin(html_dir, '{}.html'.format(file_no_ext))
    if (not convert_all and 
        os.path.isfile(target_html_path) and 
        os.stat(source_ipynb_path).st_mtime < os.stat(target_html_path).st_mtime):
        # print('"{}" no update'.format(ipy_fname))
        continue # html is newer than ipynb
    print('Renew "{}"'.format(ipy_fname))
    os.system('jupyter-nbconvert --to html "{}"'.format(pjoin(jupyter_dir, file_no_ext)))
    os.system('mv "{}" "{}"'.format(source_html_path, target_html_path))
