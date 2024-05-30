import platform
import psutil
import sys
from rich import print
from rich.console import Console
from rich.table import Table
from halo import Halo
from tqdm import tqdm

def display_system_info(info_type):
    table = Table(title="システム情報")
    table.add_column("項目", style="cyan")
    table.add_column("値", style="magenta")

    with Halo(text='システム情報取得中...', spinner='dots'):
        if info_type == "os" or info_type == "all":
            table.add_row("OSの種類", platform.system())
            table.add_row("OSのバージョン", platform.version())
        if info_type == "cpu" or info_type == "all":
            table.add_row("CPUの種類", platform.processor())
            table.add_row("物理コア数", str(psutil.cpu_count(logical=False)))
            table.add_row("論理コア数", str(psutil.cpu_count(logical=True)))
        if info_type == "memory" or info_type == "all":
            memory = psutil.virtual_memory()
            table.add_row("総メモリ", str(memory.total))
            table.add_row("使用中のメモリ", str(memory.used))
            table.add_row("空きメモリ", str(memory.available))

    console = Console()
    with tqdm(total=1, desc='情報表示中') as pbar:
        console.print(table)
        pbar.update(1)

def display_help():
    help_text = """
    使用方法: python script_name.py [info_type]

    info_type:
    - os: OSの情報を表示します
    - cpu: CPUの情報を表示します
    - memory: メモリの情報を表示します
    - all: すべてのシステム情報を表示します
    - help: このヘルプメッセージを表示します

    例:
    - python script_name.py os
    - python script_name.py cpu
    - python script_name.py memory
    - python script_name.py all
    - python script_name.py help
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "help":
        display_help()
    else:
        info_type = sys.argv[1]
        display_system_info(info_type)