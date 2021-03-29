from settings import console, typer, app
from pathlib import PurePath, Path
from subprocess import check_output
import os

# - - - -  - - - -  - - - -  - - - -  - - - -  - - - - 
@app.command()
def new(
    repo:str = typer.Option(Path.cwd().parts[-1], prompt="Repo name")
):
    user = 'ab22375'
    pwd = os.environ['ENV_GTH']

    s = """
        curl -i -H """ + f"Authorization: token {pwd}" + """
        -d '{
            "name": "monthly_report",
            "auto_init": true,
            "private": true
        }' 
        https://api.github.com/{user}/repos
    """.format(pwd=pwd, user=user)
    
    console.print(s)
    # console.print(Path.cwd())
    if False:
        repo_name = dict(name=repo)
        cmds = []
        cmds.append('git init')
        cmds.append('curl -u \'' + usr + '\' https://api.github.com/user/repos -d \'{"name" : "' + repo + '"}\'')
        cmds.append(f'git remote add origin git@github.com:ab22375/{repo}.git')
        cmds.append('git add .')
        cmds.append('git commit -m "first commit"')
        cmds.append('git push --set-upstream origin master')
        for cmd in cmds:
            console.print(cmd)
            # check_output(cmd, shell=True, cwd=Path.cwd())

# - - - -  - - - -  - - - -  - - - -  - - - -  - - - - 
@app.command()
def add(
    comment: str = typer.Option('upd', prompt="Comment: ")
    ):

    cmds = []
    cmds.append("git add .")
    cmds.append(f'git commit -m "{comment}" ')
    cmds.append("git push")

    for cmd in cmds:
        typer.echo(cmd)
        try:
            check_output(cmd, shell=True, cwd="./") #, cwd=folder)
        except:
            console.print('-'*30, '\n\n   ==>> Error\n\n','-'*30)

    console.print('*** END ***')

# - - - - - - - - - - - - - - - - - - - - - - - - - - -
if __name__ == "__main__":
    app()
