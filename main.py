from _sqlite3 import Cursor, Connection
import querys


def main() -> None:
    db_name: str = "people.db"
    conn: Connection = querys.connect_to_database(db_name)
    cursor: Cursor = conn.cursor()
    querys.create_table(conn, cursor)
    
    
    show_menu: str = """1. Add people
2. Delete person by id
3. Update person
4. See all people
5. Select person by name
6. Delete all people
7. Exit
"""
    
    while True:
        print(show_menu)
        option: int = int(input("Choose an option: "))
        
        if option == 1: # add people
            new_person: str = input("Enter the name of the person: ")
            new_age: int = int(input("Enter the age of the person: "))
            querys.add_people(conn, cursor, (new_person, new_age))
            querys.see_all_people(cursor)
            break
        
        elif option == 2: # delete person by id
            if querys.is_table_empty(cursor):
                print("There are no people to delete")
                break
            
            person_id: int = int(input("Enter the id of the person to delete: "))
            querys.delete_person_by_id(conn, cursor, person_id)
            break
        
        elif option == 3: # update person
            if querys.is_table_empty(cursor):
                print("There are no people to update")
                break
            person_id: int = int(input("Enter the id of the person to update: "))
            new_name: str = input("Enter the new name: ")
            querys.update_person(conn, cursor, new_name, person_id)
            querys.see_all_people(cursor)
            break
        
        elif option == 4: # see all people
            querys.see_all_people(cursor)
            break
        
        elif option == 5: # select person by name
            if querys.is_table_empty(cursor):
                print("There are no people to select")
                break
    
            person_name: str = input("Enter the name of the person to select: ")
            querys.select_person_by_name(cursor, person_name)
            break
        
        elif option == 6: # delete all people
            if input("Are you sure you want to delete all people? (y/n): ") == "y":
                querys.delete_all_elements(conn, cursor)
            break
        
        elif option == 7:
            print("Goodbye")
            break
        
        else:
            print("Invalid option")
    
    querys.commit_and_close(conn, cursor)
    conn.close()
    
    

if __name__ == "__main__":
    main()