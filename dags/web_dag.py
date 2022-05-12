import sys
from datetime import datetime, timedelta
import psycopg2
from airflow import DAG
from airflow.models import Variable
from airflow.operators.python import PythonOperator
import random
from webscraping import ScrapingScores

def data_test():

    host = Variable.get("host")
    db_name = Variable.get("db_name")
    username = Variable.get("username")
    password = Variable.get("password")
    sslmode = Variable.get("sslmode")
    conn_string = f"host={host} user={username} dbname={db_name} password={password} sslmode={sslmode}"
    conn = psycopg2.connect(conn_string)

    cursor = conn.cursor()

    # for index, row in new_df.iterrows():
    #       cursor.execute("INSERT INTO footballdata (Div, Date, HomeTeam, AwayTeam, FTHG, FTAG,FTR,HTHG,HTAG,HTR,HS,ASAS,HST,AST,HF,AF,HC,AC,HY,AY,HR,AR) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);", (row['Div'], row['Date'], row['HomeTeam'], row['AwayTeam'], row['FTHG'], row['FTAG'], row['FTR'], row['HTHG'], row['HTAG'], row['HTR'], row['HS'], row['ASAS'], row['HST'], row['AST'], row['HF'], row['AF'], row['HC'], row['AC'], row['HY'], row['AY'], row['HR'], row['AR']))


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

sys.path.append('/home/max/airflow')

default_args = {
    'owner': 'max',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 26),
    'email': ['maxblum94@yahoo.de'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=10)
}

dag = DAG('test_dag', default_args=default_args, schedule_interval="*/5 * * * *")

process_dag = PythonOperator(
    task_id='test_dag',
    python_callable=data_test,
    dag=dag
)