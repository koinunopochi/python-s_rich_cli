from tqdm import tqdm
import msvcrt

for i in tqdm(range(100)):
    # キー入力まで待機
    while True:
        try:
            if msvcrt.kbhit():
                break
        except:
          print("error")
    pass