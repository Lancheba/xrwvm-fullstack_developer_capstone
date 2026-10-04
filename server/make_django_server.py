"""Run the Django dev server briefly, hit the home page once, and save the
terminal output to a file named django_server (UTF-8).

Usage (from the capstone 'server' folder, venv active, server NOT already running):
    python make_django_server.py
"""
import os
import subprocess
import sys
import time
import urllib.request

env = dict(os.environ, PYTHONUNBUFFERED="1", PYTHONIOENCODING="utf-8")

proc = subprocess.Popen(
    [sys.executable, "manage.py", "runserver", "--noreload"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding="utf-8",
    errors="replace",
    env=env,
)

time.sleep(6)  # let the server start

try:
    urllib.request.urlopen("http://127.0.0.1:8000/", timeout=10).read()
except Exception as exc:  # still save whatever the server printed
    print("Request failed:", exc)

time.sleep(1)
proc.terminate()
try:
    output = proc.communicate(timeout=10)[0]
except subprocess.TimeoutExpired:
    proc.kill()
    output = proc.communicate()[0]

with open("django_server", "w", encoding="utf-8", newline="\n") as f:
    f.write(output)

print("----- saved to django_server -----")
print(output)
