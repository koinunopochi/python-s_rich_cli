from halo import Halo
import time

# 単純なスピナー
with Halo(spinner='dots'):
    time.sleep(3)

# カスタムスピナー
spinner = Halo(text="Processing...", spinner={
    "interval": 120,
    "frames": [
        "⠋",
        "⠙",
        "⠹",
        "⠸",
        "⠼",
        "⠴",
        "⠦",
        "⠧",
        "⠇",
        "⠏"
    ]})
spinner.start()
time.sleep(3)
spinner.stop()