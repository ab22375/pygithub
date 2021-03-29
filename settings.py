# from pathlib import Path, PurePath
# from subprocess import check_output

from rich.console import Console
console = Console(color_system="auto")

import typer
app = typer.Typer()

# - - - -  - - - -  - - - -  - - - -  - - - -  - - - - 
# @app.command()
# def here(
#     projfolder:str=typer.Option('new-project', prompt="Input project folder name"),
#     packages:str=typer.Option('', prompt="list of packages separated by space")
# ):
#     pass


# - - - -  - - - -  - - - -  - - - -  - - - -  - - - - 
# @app.command()
# def there(
#     basedir:Path=typer.Option('/Users/z/dev/test', prompt="Input base dir"),
#     projfolder:str=typer.Option('new-project', prompt="Input project folder name"),
#     packages:str=typer.Option('', prompt="list of packages separated by space")
#     ):
#     pass 
