import click
from findpath import FindPath
from ignore import Ignore

follow = FindPath()
ignore = Ignore()


@click.group()
def main():
    ignore.find_ignore()


@click.command()
def start():
    pass


@click.command()
@click.option('-path', default='', help='Полный путь до папки')
def set_dir(path):
    print(follow.__dict__)


main.add_command(start)
main.add_command(set_dir)

if __name__ == '__main__':
    main()
