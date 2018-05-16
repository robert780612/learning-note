
import os
import sys
import time
from os.path import join as pjoin

if len(sys.argv)>1:
    convert_all = sys.argv[1] == 'all'
else:
    convert_all = False

jupyter_dir = './jupyters/'
html_dir = './html/'
tmp_dir = './tmp/'
for n, ipy_fname in enumerate(os.listdir(jupyter_dir)):
    file_no_ext, ext = os.path.splitext(ipy_fname)
    if ext != '.ipynb':
        continue

    # Check modification time
    source_ipynb_path = pjoin(jupyter_dir, '{}'.format(ipy_fname))
    source_html_path = pjoin(jupyter_dir, '{}.html'.format(file_no_ext))
    target_html_path = pjoin(html_dir, '{}.html'.format(file_no_ext))
    if (not convert_all and 
        os.path.isfile(target_html_path) and 
        os.stat(source_ipynb_path).st_mtime < os.stat(target_html_path).st_mtime):
        # print('"{}" no update'.format(ipy_fname))
        continue # html is newer than ipynb
    if not os.path.isfile(target_html_path):
        print('A new jupyter notebook "{}", please add a hyper-link in the index.html'.format(ipy_fname))
    else:
        print('Renew "{}"'.format(ipy_fname))
    os.system('jupyter-nbconvert --to html "{}"'.format(pjoin(jupyter_dir, file_no_ext)))
    os.system('mv "{}" "{}"'.format(source_html_path, target_html_path))


# Remove renamed html file
ipy_list = [os.path.splitext(x)[0] for x in os.listdir(jupyter_dir) if os.path.splitext(x)[1]=='.ipynb']
for n, html_name in enumerate(os.listdir(html_dir)):
    name, ext = os.path.splitext(html_name)
    if ext != '.html':
        continue
    if name not in ipy_list:
        # Delete this html file, maybe rename
        print('Move {} to temp directory.'.format(name))
        os.system('mv {} {}'.format(pjoin(html_dir, html_name), tmp_dir))