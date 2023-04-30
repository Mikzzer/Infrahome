from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return f"Aktualna godzina: {current_time}"

if __name__ == '__main__':
    app.run()
