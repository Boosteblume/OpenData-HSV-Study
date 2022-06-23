import random
import sys
from datetime import datetime, timedelta
import psycopg2
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator


def data_test():

    host = Variable.get("host")
    db_name = Variable.get("db_name")
    username = Variable.get("username")
    password = Variable.get("password")
    sslmode = Variable.get("sslmode")
    conn_string = f"host={host} user={username} dbname={db_name} password={password} sslmode={sslmode}"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()
    # Drop previous table of same name if one exists
    cursor.execute("DROP TABLE IF EXISTS inventory;")
    print("Finished dropping table (if existed)")
    # Create a table
    cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
    print("Finished creating table")
    # Insert some data into the table
    b = random.randint(0, 200)
    o = random.randint(0, 200)
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", b))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", o))
    cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
    print("Inserted 3 rows of data")

    # Clean up
    conn.commit()
    cursor.close()
    conn.close()

data_test()