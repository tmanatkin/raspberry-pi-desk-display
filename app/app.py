from datetime import datetime
from flask import Flask, render_template
import webview
import threading

app = Flask(__name__)

def time():
    now = datetime.now()
    return {
        'date': now.strftime('%Y-%m-%d'),
        'timestamp': now.strftime('%H:%M:%S'),
    }

@app.route('/')
def home():
    return render_template('home.html', time=time())

def run_flask():
    app.run(debug=True, use_reloader=False)

def create_webview():
    window = webview.create_window('Raspberry Pi Desk Display', 'http://127.0.0.1:5000', fullscreen=True)
    webview.start()

if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    create_webview()
