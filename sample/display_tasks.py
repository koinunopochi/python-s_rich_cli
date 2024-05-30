from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from halo import Halo

tasks = []

def display_tasks():
    table = Table(title="タスク一覧")
    table.add_column("ID", style="cyan")
    table.add_column("タスク名", style="magenta")
    table.add_column("優先度", style="green")

    for i, task in enumerate(tasks, start=1):
        priority = "高" if task["priority"] == "high" else "中" if task["priority"] == "medium" else "低"
        table.add_row(str(i), task["name"], priority)

    console = Console()
    console.print(table)

def add_task(console):
    name = Prompt.ask("タスク名を入力してください")
    priority = Prompt.ask("優先度を入力してください", choices=["high", "medium", "low"])
    with console.status("[bold green]タスクを追加中..."):
        tasks.append({"name": name, "priority": priority})
    print("[bold green]タスクが追加されました[/bold green]")

def delete_task(console):
    task_id = Prompt.ask("削除するタスクのIDを入力してください", default="0")
    with console.status("[bold green]タスクを削除中..."):
        if task_id.isdigit() and 1 <= int(task_id) <= len(tasks):
            tasks.pop(int(task_id) - 1)
            print("[bold green]タスクが削除されました[/bold green]")
        else:
            print("[bold red]無効なタスクIDです[/bold red]")

def display_help():
    help_text = """
    タスク管理ツール - 使い方

    このツールでは、以下のアクションが可能です:
    1. タスクを追加: 新しいタスクを追加します。タスク名と優先度を入力してください。
    2. タスクを削除: 既存のタスクを削除します。削除するタスクのIDを入力してください。
    3. 終了: ツールを終了します。

    アクション番号を入力し、Enterキーを押してください。
    """
    print(help_text)

def main():
    console = Console()

    while True:
        display_tasks()
        print("\n[bold blue]アクション:[/bold blue]")
        print("1. タスクを追加")
        print("2. タスクを削除")
        print("3. 終了")
        print("4. ヘルプ")

        def prompt_with_spinner():
            spinner = Halo(text="\nアクション番号を選択してください", spinner={
                "interval": 120,
                "frames": [
                    "⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"
                ]
            })
            spinner.start()
            action = ""
            while action not in ["1", "2", "3", "4"]:
                action = input()
                print(action)  # 入力文字をエコーバックする
            spinner.stop()
            return action

        action = prompt_with_spinner()

        if action == "1":
            add_task(console=console)
        elif action == "2":
            delete_task(console=console)
        elif action == "3":
            print("[bold green]タスク管理ツールを終了します[/bold green]")
            break
        elif action == "4":
            display_help()

if __name__ == "__main__":
    main()