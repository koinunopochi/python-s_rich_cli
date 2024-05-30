import os
import sys
from rich import print
from rich.console import Console
from rich.table import Table
from halo import Halo
from tqdm import tqdm

def process_files(directory):
    files = os.listdir(directory)
    table = Table(title="ファイル処理結果")
    table.add_column("ファイル名", style="cyan")
    table.add_column("サイズ", style="magenta")

    with Halo(text='ファイル処理中...', spinner='dots'):
        for file in tqdm(files, desc='処理中'):
            file_path = os.path.join(directory, file)
            size = os.path.getsize(file_path)
            table.add_row(file, str(size) + " bytes")

    console = Console()
    console.print(table)

def display_help():
    help_text = """
    使用方法: python script_name.py [directory]

    引数:
    - directory: 処理対象のディレクトリのパスを指定します

    説明:
    このスクリプトは、指定されたディレクトリ内のファイルを処理し、各ファイルの名前とサイズを表示します。

    例:
    - python script_name.py /path/to/directory
    - python script_name.py ./sample_directory
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[1] == "help":
        display_help()
    else:
        directory = sys.argv[1]
        process_files(directory)