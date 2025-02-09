import sqlite3
from _sqlite3 import Cursor, Connection
from typing import Any, Tuple, List

def connect_to_database(database: str) -> Connection:
    connection = sqlite3.connect(database)
    return connection


def commit_and_close(conn: Connection, cursor: Cursor) -> None:
    conn.commit()
    cursor.close


def create_table(conn: Connection, cursor: Cursor) -> None:
    create_table_query: str = """CREATE TABLE IF NOT EXISTS people (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age REAL
        )"""
        
    cursor.execute(create_table_query)
    conn.commit()
  
  
def is_table_empty(cursor: Cursor) -> bool:
    cursor.execute("SELECT * FROM people")
    return cursor.fetchone() is None
    
def add_people(conn: Connection, cursor: Cursor, people: Tuple | List[Tuple]) -> None:
    insert_query: str = "INSERT INTO people (name, age) VALUES (?, ?);"
    if len(people) > 2:
        cursor.executemany(insert_query, people)
        print("People added successfully")
    else:
        cursor.execute(insert_query, (people[0], people[1]))
        print("Person added successfully")
    conn.commit()

def delete_person_by_id(conn: Connection, cursor: Cursor, person_id: int) -> None:
    delete_query: str = "DELETE FROM people WHERE id=?"
    cursor.execute(delete_query, (person_id,))
    commit_and_close(conn, cursor)

def update_person(conn: Connection, cursor: Cursor, new_name: str, person_id: int) -> None:
    update_query: str = "UPDATE people SET name=? WHERE id=?"
    cursor.execute(update_query, (new_name, person_id))
    conn.commit()

def see_all_people(cursor: Cursor) -> None:
    select_all_query: str = "SELECT * FROM people"
    cursor.execute(select_all_query)
    rows: list = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"id: {row[0]}, name: {row[1]}, age: {int(row[2])}")
    else:
        print("No person added")

def select_person_by_name(cursor: Cursor, person_name: str) -> None:
    select_query: str = "SELECT * FROM people WHERE name=?"
    cursor.execute(select_query, (person_name,))
    person: Tuple | None = cursor.fetchone()
    if person:
        print(person)
    else:
        print("Person not found")

def delete_all_elements(conn: Connection, cursor: Cursor) -> None:    
    cursor.execute("DELETE FROM people")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='people'")
    print("All people deleted successfully")
    conn.commit()