import psycopg2
conn = psycopg2.connect(database="information_retrieval", user="postgres", password="admin", host="127.0.0.1", port="5432")
cur = conn.cursor()
print("connected successfully")
