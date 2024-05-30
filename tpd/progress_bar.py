from tqdm import tqdm
import time

# 簡単なプログレスバー
for i in tqdm(range(100), desc="Processing"):
    time.sleep(0.05)

# カスタマイズしたプログレスバー    
pbar = tqdm(total=100, bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [elapsed: {elapsed}, remaining: {remaining}]')
for i in range(100):
    pbar.update(1)
    time.sleep(0.05)
pbar.close()