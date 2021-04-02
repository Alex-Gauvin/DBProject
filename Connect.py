import psycopg2
from psycopg2 import Error


if __name__ == "__main__" :
    username = input("Enter username: ")
    password = input("Enter password: ")
    params = dict(user=username,
                                  password=password,
                                  host="web0.eecs.uottawa.ca",
                                  port="15432",
                                  database=username)
try:
    # Connect to an existing database
    connection = psycopg2.connect(**params)

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if (connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")

#SQL for admins
def admin_SQL(query):
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
def get_unbooked_rooms():
    """ query data from the vendors table """
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

