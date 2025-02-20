from flask import Flask
import os
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Monish D"
    username = os.getenv("USER", "codespace")
    ist_time = datetime.now(pytz.timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S.%f')
    top_output = subprocess.getoutput("top -b -n 1")

    return f"""
    <pre>
    Name: {name}
    User: {username}
    Server Time (IST): {ist_time}
    TOP output:
    {top_output}
    </pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
