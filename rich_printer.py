from rich.console import Console
from rich.table import Table

def rich_print_album(album):
  console = Console(soft_wrap=True)
  table = Table(title="1001 Albums You Must Hear Before You Die")
  table.add_column("Album title")
  table.add_column("Artist")
  table.add_column("Year")
  table.add_row(
    album.title,
    album.artist,
    str(album.year)
  )
  
  console.print(table)