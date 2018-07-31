import psycopg2
import json
import credentials


conn = psycopg2.connect(host="ec2-54-243-129-189.compute-1.amazonaws.com", database="dbfncufnkimb1n", user=credentials.get_sql_username(), password=credentials.get_sql_password())
cursor = conn.cursor()
cursor.execute("SELECT vehicle_model FROM turodb WHERE vehicle_year = 2013")
for val in cursor.fetchall():
  print val[0]
conn.commit()
cursor.close()
