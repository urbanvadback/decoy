import random
import string
import subprocess

ALTERNATIVES = string.ascii_letters + "0123456789"

prev = "dirt.txt"

for i in range(2000):
    if i % 50 == 0:
        print(i)

    current = ""
    for _ in range(5):
        current += random.choice(ALTERNATIVES)
    
    args = ["zip", "-q", "--password", current, f"{current}.zip", f"{prev}{'.zip' if prev != 'dirt.txt' else ''}"]

    subprocess.run(args)

    if prev == "dirt.txt":
        prev = current
        continue
    subprocess.run(["rm", f"{prev}.zip"])
    prev = current

args = ["zip", "-q", "--password", "password", f"password.zip", f"{prev}.zip"]

subprocess.run(args)
subprocess.run(["rm", f"{prev}.zip"])
