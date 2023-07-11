from flask import Flask, request
from folderbase import *
app = Flask(__name__)


@app.route('/')
def index():
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    print(request.environ['REMOTE_ADDR'])
    return request.environ['REMOTE_ADDR']
  else:
    print(request.environ['HTTP_X_FORWARDED_FOR'])  # if behind a proxy
    return request.environ['HTTP_X_FORWARDED_FOR']
@app.route('/shareco')
def indexa():
	f = open('shareco.html')
	r = f.read()
	f.close()
	return r

@app.route('/set.<con>')
def set(con):
  ip = ""
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    print(request.environ['REMOTE_ADDR'])
    ip = request.environ['REMOTE_ADDR']
  else:
    print(request.environ['HTTP_X_FORWARDED_FOR'])
    ip = request.environ['HTTP_X_FORWARDED_FOR']
  write(ip, con)
  return "OK"


@app.route('/get')
def get():
  ip = ""
  if request.environ.get('HTTP_X_FORWARDED_FOR') is None:
    print(request.environ['REMOTE_ADDR'])
    ip = request.environ['REMOTE_ADDR']
  else:
    print(request.environ['HTTP_X_FORWARDED_FOR'])
    ip = request.environ['HTTP_X_FORWARDED_FOR']
  if ishere(ip):
    return read(ip)
  else:
    return "Don't set this as you snip!"


@app.route('/ipg.<ip>')
def ipg(ip):
  if ishere(ip):
    return read(ip)
  else:
    return "Don't set this as you snip!"

@app.route('/ad')
def ad():
  return "<iframe data-aa='2196628' src='//ad.a-ads.com/2196628?size=200x200' style='width:200px; height:200px; border:0px; padding:0; overflow:hidden; background-color: transparent;'></iframe>"


app.run(host='0.0.0.0', port=1234)
