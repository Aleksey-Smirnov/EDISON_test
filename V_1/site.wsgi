import os, sys
activate_this = '/home/a0556931/python3.8/bin/activate_this.py'
with open(activate_this) as f:
  exec(f.read(), {'__file__': activate_this})
sys.path.insert(0, os.path.join('/home/a0556931/domains/a0556931.xsph.ru/public_html/'))
from index import app as application
if __name__ == "__main__":
    application.run() 