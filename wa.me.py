import urllib.parse
import subprocess
import threading

number = input("Numara: ")
text = input("Mesaj: ")
url_text = urllib.parse.quote(text)

from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def redirect_to_link():
    return redirect(f'https://wa.me/{number}?text={url_text}')

def run():
    app.run()

def serveo():
    command = "ssh -R 80:localhost:5000 serveo.net"
    subprocess.run(command, shell=True)

def thread():
    t1 = threading.Thread(target=run)
    t2 = threading.Thread(target=serveo)

    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    thread()
