from halo import Halo
import msvcrt

with Halo(text="Processing...", spinner="dots"):
    while True:
        # キーボードが押されたら終了
        try:
            if msvcrt.kbhit():
                break
        except:
            pass
    pass