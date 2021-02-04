import os
import re
import sys
path=os.getcwd()
argv=''
for s in sys.argv[1:]:
    argv+=s+' '
if not os.path.exists(path+'/out'):
    os.mkdir("out")
list=os.listdir(path)
for name in list:
    if not str(name).endswith(('.bmp', '.png', '.jpg', '.jpeg','tiff')):
        continue
    pfname = os.path.splitext(name)[0]
    os.system("cwebp %s %s -o out/%s.webp" %(name,argv,pfname))