import psycopg2
from psycopg2 import Error
from getpass import getpass

if __name__ == "__main__" :
    username = input("Enter username: ")
    password = input("Enter password: ")
    


try:
    # Connect to an existing database
    connection = psycopg2.connect(user=username,
                                  password=password,
                                  host="web0.eecs.uottawa.ca",
                                  port="15432",
                                  database=username)

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


