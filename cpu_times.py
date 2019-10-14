import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    ct = psutil.cpu_times()
    data = []
    for i in range(0, len(ct)):
        data.append([ct._fields[i], ct[i]])
    return render_template("cpu_times.html", data=data)

if __name__ == '__main__':
    app.run()
