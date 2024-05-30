import sys
import time

spin_chars = ['|', '/', '-', '\\']
i = 0
while True:
    sys.stdout.write(spin_chars[i % len(spin_chars)] + "\r")
    sys.stdout.flush()
    time.sleep(0.1)
    i += 1