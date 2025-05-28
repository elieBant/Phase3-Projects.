import click
from models import User
from database import SessionLocal

@click.group()
def user_cli():
    """Commands to manage users"""
    pass

@user_cli.command("create")
@click.option('--name', prompt='User name')
def create_user(name):
    session = SessionLocal()
    user = User(name=name)
    session.add(user)
    session.commit()
    session.close()
    click.echo(f"User {name} created successfully.")

@user_cli.command("update")
@click.option('--user_id', prompt='User ID to update', type=int)
@click.option('--new_name', prompt='New name')
def update_user(user_id, new_name):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        user.name = new_name
        session.commit()
        click.echo(f"User updated successfully: {new_name}")
    else:
        click.echo("User not found.")
    session.close()

@user_cli.command("delete")
@click.option('--user_id', prompt='User ID to delete', type=int)
def delete_user(user_id):
    session = SessionLocal()
    user = session.query(User).filter_by(id=user_id).first()
    if user:
        session.delete(user)
        session.commit()
        click.echo("User deleted successfully.")
    else:
        click.echo("User not found.")
    session.close()

# --- Added list command ---
@user_cli.command("list")
def list_users():
    session = SessionLocal()
    users = session.query(User).all()
    if users:
        for user in users:
            click.echo(f"ID: {user.id}, Name: {user.name}")
    else:
        click.echo("No users found.")
    session.close()






