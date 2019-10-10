# CPU Times Doc

This repo has been made available under [MIT license](https://github.com/nick3499/psutil_cpu_times/blob/master/LICENSE).

![screen capture](screen_capture.png)

## cpu_times.sh

```bash
#!/bin/bash

export FLASK_APP=cpu_times.py
export FLASK_ENV=development
flask run
```

`FLASK_APP` environment variable specifies which app to load.

`FLASK_ENV` environment variable specifies which environment the Flask app runs in. In this case, `development` indicates that the `flask run` command will enable _debug mode_, _interactive debugger_ and _reloader_.

In a Unix-like terminal emulator, run the Bash script:

`$ sudo bash cpu_times.sh`

Something close to the following will print to terminal:

```
 * Serving Flask app "cpu_times.py" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with inotify reloader
 * Debugger is active!
 * Debugger PIN: XXX-XXX-XXX
```

Open `http://127.0.0.1:5000/` in a browser. Since no port was specified, Flask defaults to port `5000`. If a different port number is required, the `FLASK_RUN_PORT` environment variable is available.

## cpu_times.py

```python
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
    app.run(debug=True)
```

[psutil.cpu_times()](https://psutil.readthedocs.io/en/latest/#psutil.cpu_times) method returns system CPU times as a named tuple. For example:

`scputimes(user=1233.68, nice=14.35, system=424.85, idle=9685.94, iowait=219.69, irq=0.0, softirq=7.82, steal=0.0, guest=0.0, guest_nice=0.0)`

Key/value pairs extracted from `scputimes` are appended to the `data` variable.

[render_template](https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template) method receives the template's filename, and the `data` variable which is passed to the template engine.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

The code block above indicates that the Python interpreter will execute `cpu_times.py` as the _main_ program file which may also be referred to as the _source file_. Notice also that `debug` value is set to `True` when the app runs.

## cpu_times.html

[cpu_times.html](https://jinja.palletsprojects.com/en/2.10.x/templates/) is a Jinja template _which contains variables and/or expressions, which get replaced with values when a template is rendered; and tags, which control the logic of the template._

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <title>CPU Times [PSUtil]</title>
  <style>
    h3 { color: #4CBB17; }
    table { border-collapse: collapse; }
    td {
      border: 1px solid #B4EEB4;
      padding: 5px;
      text-align: left;
    }
  </style>
</head>
<body>
  <h3>CPU Times</h3>
  <table>
  {%- for j in data %}
    <tr>
      <td>{{ j[0] }}</td>
      <td>{{ j[1] }}</td>
    <tr>
  {%- endfor %}
  </table>
</body>
</html>
```

`{%- for j in data %}` indicates that the template will loop through the list of key/value pairs in `data`, known as a `for` loop.
