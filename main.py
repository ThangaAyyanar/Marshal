from rich.console import Console
from rich.table import Column, Table
import csv

csv_file = open('progress_data.csv')
csv_reader = csv.reader(csv_file, delimiter=',')
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

    else:

        table.add_row(row[0], row[1], row[2])

    line_count += 1

console.print(table)
