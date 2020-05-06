from rich.console import Console
from rich.table import Column, Table
from rich.progress import Progress
import csv


def format_status(status):
    if status == "Not yet started":
        return f"[bold cyan]{status}[/bold cyan]"
    elif status == "started":
        return f"[bold green]{status}[/bold green]"
    elif status == "stopped":
        return f"[bold red]{status}[/bold red]"
    else:
        return status

def get_progress_string(start_progress:int,end_progress:int):
    # completed = "[bold red]▇[/bold red]"*start_progress
    # not_completed = "[bold white]▇[/bold white]"*end_progress
    new_started = int((start_progress/end_progress)*10)
    completed = "[bold red]▃[/bold red]"*new_started
    not_completed = "[bold white]▃[/bold white]"*(10-new_started)
    return f"{completed}{not_completed}"

def print_table(csv_reader):

    line_count = 0

    console = Console()
    table = Table(show_header=True, header_style="bold magenta")

    for row in csv_reader:

        # Ignore empty line
        if len(row) == 0:
            continue

        if line_count == 0:

            table.add_column(row[0], style="dim", width=12)
            table.add_column(row[1])
            table.add_column(row[2])
            table.add_column(row[3])

        else:

            progress = row[3].split('/')
            table.add_row(row[0], row[1], format_status(row[2]), get_progress_string(int(progress[0]),int(progress[1])))

        line_count += 1

    console.print(table)

def main():
    csv_file = open('progress_data.csv')
    csv_reader = csv.reader(csv_file, delimiter=',')
    print_table(csv_reader)

if __name__ == "__main__":
    main()

