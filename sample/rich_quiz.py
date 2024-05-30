import sys
from rich import print
from rich.prompt import Prompt
from halo import Halo
from tqdm import tqdm

def run_quiz(player_name):
    questions = [
        {"question": "Pythonの作者は誰ですか？", "answer": "Guido van Rossum"},
        {"question": "Pythonのリストで要素を追加するメソッドは？", "answer": "append"},
        {"question": "Pythonのディクショナリで値を取得するメソッドは？", "answer": "get"}
    ]

    score = 0
    with tqdm(total=len(questions), desc='クイズ進行中') as pbar:
        for question in questions:
            print(f"\n[bold blue]{question['question']}[/bold blue]")
            with Halo(text='考え中...', spinner='dots'):
                answer = Prompt.ask("答えを入力してください")
            if answer.lower() == question['answer'].lower():
                score += 1
                print("[bold green]正解！[/bold green]")
            else:
                print("[bold red]不正解！[/bold red]")
            pbar.update(1)

    print(f"\n[bold magenta]{player_name}の最終スコア: {score}/{len(questions)}[/bold magenta]")

def display_help():
    help_text = """
    使用方法: python script_name.py [player_name]

    引数:
    - player_name: プレイヤーの名前を指定します

    説明:
    このスクリプトは、Pythonに関する簡単なクイズゲームです。プレイヤーは質問に答え、最終的なスコアが表示されます。

    例:
    - python script_name.py Alice
    - python script_name.py Bob
    """
    print(help_text)

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] == "--help" or sys.argv[1] == "-h" or sys.argv[1] == "help":
        display_help()
    else:
        player_name = sys.argv[1]
        run_quiz(player_name)