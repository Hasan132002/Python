import subprocess

s = subprocess.check_output(["echo", "Hello World!"])
print("s = " + s)