from base64 import urlsafe_b64decode as ub64d, urlsafe_b64encode as ub64e
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return "Hello world!"

@app.route('/do/<urlb64>/get.<ext>')
def download(urlb64, ext):
	return ub64d(urlb64)

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80)
