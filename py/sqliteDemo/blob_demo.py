"""
SQLite supports a BLOB data type for raw binary data, which we can use to store
images, text documents, and other files.

I stole this code. Resources:
- https://www.twilio.com/en-us/blog/intro-multimedia-file-upload-python-sqlite3-database
- https://stackoverflow.com/questions/7905859/is-there-auto-increment-in-sqlite
- https://sqlite.org/datatype3.html
"""

import os
import sqlite3
from sqlite3 import Error

def create_db():
  try:
    conn = sqlite3.connect('blob_demo.db')
    conn.text_factory = str
    print("[INFO] : Successful connection!")
    cur = conn.cursor()

    cur.execute("""
      CREATE TABLE IF NOT EXISTS uploads (
        id integer PRIMARY KEY,
        file_name text NOT NULL,
        file_blob blob NOT NULL
      );
    """)
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "Oh shucks, something is wrong here."

def insert_into_database(file_path_name, file_name_blob):
  try:
    conn = sqlite3.connect('blob_demo.db')
    conn.text_factory = str
    print("[INFO] : Successful connection!")
    cur = conn.cursor()
    insert_file = '''INSERT INTO uploads(file_name, file_blob)
      VALUES(?, ?)'''
    cur = conn.cursor()
    cur.execute(insert_file, (file_path_name, file_name_blob, ))
    conn.commit()
    print("[INFO] : The blob for ", file_path_name, " is in the database.")

    # Return row ID of the record that was just inserted.
    return cur.lastrowid
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "Oh shucks, something is wrong here."

def convert_into_binary(file_path):
  print("[INFO] : converting into binary data rn")
  with open(file_path, 'rb') as file:
    binary = file.read()
  return binary

def read_blob_data(entryID):
  try:
    conn = sqlite3.connect('blob_demo.db')
    conn.text_factory = str
    cur = conn.cursor()
    print("[INFO] : Connected to SQLite to read_blob_data")
    sql_fetch_blob_query = """SELECT * from uploads where id = ?"""
    cur.execute(sql_fetch_blob_query, (entryID,))
    record = cur.fetchall()
    for row in record:
      converted_file_name = row[1]
      photo_binarycode  = row[2]
      # parse out the file name from converted_file_name
      last_slash_index = converted_file_name.rfind(os.path.sep) + 1
      png_index = converted_file_name.find('.png')
      final_file_name = converted_file_name[last_slash_index:]
      write_to_file(photo_binarycode, final_file_name)
      print("[DATA] : File successfully stored on disk. Check the project directory. \n")
    cur.close()
  except sqlite3.Error as error:
    print("[INFO] : Failed to read blob data from sqlite table", error)
  finally:
    if conn:
        conn.close()

def write_to_file(binary_data, file_name):
  with open(file_name, 'wb') as file:
    file.write(binary_data)
  print("[DATA] : The following file has been written to file: ", file_name)

def retrieve_file(entryID):
  try:
    conn = sqlite3.connect('blob_demo.db')
    conn.text_factory = str   # added in to get rid of "u must not use 8 bit blah blah"
    print("[INFO] : Successful connection!")
    cur = conn.cursor()
    sql_retrieve_file_query = """SELECT * FROM uploads WHERE id = ?"""
    cur.execute(sql_retrieve_file_query, (entryID,))
    record = cur.fetchone()
    record_blob = record[2]
    read_blob_data(entryID)
  except Error as e:
    print(e)
  finally:
    if conn:
      conn.close()
    else:
      error = "how tf did u get here."

def main():
  create_db()
  file_path_name = input("Enter full file path:\n")
  file_name_blob = convert_into_binary(file_path_name)
  print("[INFO] : the last 100 characters of blob = ", file_name_blob[:100])
  i = insert_into_database(file_path_name, file_name_blob)
  retrieve_file(i)

if __name__ == "__main__":
  main()