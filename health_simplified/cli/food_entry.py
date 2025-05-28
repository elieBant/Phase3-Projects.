import click
from datetime import datetime
from models import FoodEntry
from database import SessionLocal

@click.group()
def food_entry_cli():
    """Commands to manage food entries"""
    pass

@food_entry_cli.command("add")
@click.option('--user_id', prompt='User ID', type=int)
@click.option('--food', prompt='Food name')
@click.option('--calories', prompt='Calories', type=int)
@click.option('--date', prompt='Date (YYYY-MM-DD)')
def add_food_entry(user_id, food, calories, date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        click.echo("Error: Date must be in YYYY-MM-DD format")
        return
    
    session = SessionLocal()
    entry = FoodEntry(user_id=user_id, food=food, calories=calories, date=date_obj)
    session.add(entry)
    session.commit()
    session.close()
    click.echo("Entry added successfully!")

@food_entry_cli.command("update")
@click.option('--entry_id', prompt='ID of entry to update', type=int)
@click.option('--food', prompt='New food name')
@click.option('--calories', prompt='New calories', type=int)
@click.option('--date', prompt='New date (YYYY-MM-DD)')
def update_food_entry(entry_id, food, calories, date):
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
    except ValueError:
        click.echo("Error: Date must be in YYYY-MM-DD format")
        return
    
    session = SessionLocal()
    entry = session.query(FoodEntry).filter_by(id=entry_id).first()
    if entry:
        entry.food = food
        entry.calories = calories
        entry.date = date_obj
        session.commit()
        click.echo("Entry updated successfully!")
    else:
        click.echo("Entry not found.")
    session.close()

@food_entry_cli.command("delete")
@click.option('--entry_id', prompt='ID of entry to delete', type=int)
def delete_food_entry(entry_id):
    session = SessionLocal()
    entry = session.query(FoodEntry).filter_by(id=entry_id).first()
    if entry:
        session.delete(entry)
        session.commit()
        click.echo("Entry deleted successfully.")
    else:
        click.echo("Entry not found.")
    session.close()

@food_entry_cli.command("list")
def list_food_entries():
    session = SessionLocal()
    entries = session.query(FoodEntry).all()
    if entries:
        for entry in entries:
            click.echo(f"ID: {entry.id}, User ID: {entry.user_id}, Food: {entry.food}, Calories: {entry.calories}, Date: {entry.date}")
    else:
        click.echo("No food entries found.")
    session.close()
