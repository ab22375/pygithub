from settings import console, typer, app
from pathlib import Path
# - - - - - - - - - - - - - - - - - - - - - - - - 
# - - - -  - - - -  - - - -  - - - -  - - - -  - - - - 
@app.command()
def new(
    repo:str = typer.Option('new-project', prompt="Repository name"),
    packages:str=typer.Option('', prompt="list of packages separated by space")
):
    console.print(Path.parent)
    pass

# - - - - - - - - - - - - - - - - - - - - - - - - 
if __name__ == "__main__":
    typer.run(main)
    # app()


# function gitnew(){
#     usr = 'ab22375'
# 	pwd = '57a361e49a3a8d12a7a73c6d8d79cf70c3da0425'
    
#     cmds = []
#     cmds.append('git init')
#     cmds.append('git init')
    
#     curl -u f'{usr}:{pwd}' https://api.github.com/user/repos -d f'{"name":"{repo}"}'
#     git remote add origin "git@github.com:ab22375/${1}.git"
#     git add .
#     git commit -m "first commit"
#     git push --set-upstream origin master
# }