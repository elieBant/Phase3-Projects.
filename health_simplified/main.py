from cli.user import user_cli
from cli.food_entry import food_entry_cli
import click

@click.group()
def cli():
    pass

cli.add_command(user_cli, name="user")
cli.add_command(food_entry_cli, name="food")

if __name__ == '__main__':
    cli()







