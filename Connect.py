import click
import psycopg2
from psycopg2 import Error

params = None

@click.group()
def cli():
    """
    Welcome to our hotel interface
    """
    pass

def main():
    value = click.prompt('Select a command to run', type=click.Choice(list(cli.commands.keys()) + ['exit']))
    while value != 'exit':
        cli.commands[value]()

#SQL for admins
@cli.command()
@click.argument('query')
def SQL(query):
    """- enter SQL querys"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(query)
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

#returns unbooked rooms
@cli.command()
def get_unbooked_rooms():
    """- search for unbooked rooms"""
    conn = None
    try:
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute("SELECT vendor_id, vendor_name FROM vendors ORDER BY vendor_name") #fix sql
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

if __name__ == "__main__":

    username = input("Enter username: ")
    password = input("Enter password: ")
    params = dict(user=username,
                  password=password,
                  host="web0.eecs.uottawa.ca",
                  port="15432",
                  database=username)
    main()

