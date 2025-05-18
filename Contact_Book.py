import sqlite3 

def init_db():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contacts(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(255),
            phone_number VARCHAR(255),   
            email  VARCHAR(255), 
            address VARCHAR(255)
        )                       
    """)
    conn.commit()
    return
    
def add_contact():
    name = input("Name: ")
    phone_number = input("Phone number: ")
    email = input("Email: ")
    address = input("Address: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO contacts(name, phone_number, email, address) VALUES (?, ?, ?, ?)", (name, phone_number, email, address,))  
    conn.commit()
    conn.close()
    print("Added contact.")
    
def view_contact():
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone_number, email, address FROM contacts")
    rows = cursor.fetchall()
    if not rows:
        print("There is no contact.")
    else:
        print("\n===Contact Book===")
        for row in rows:
            print(f"ID: {row[0]} Name: {row[1]}, Phone number: {row[2]}, Email: {row[3]}, Address: {row[4]}")
        print("----------")    
                          
                          
def search_contact():
    name = input("Enter the name to find: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone_number, email, address FROM contacts WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    if rows:
        for row in rows:
            print(f"ID: {row[0]} Name: {row[1]}, Phone number: {row[2]}, Email: {row[3]}, Address: {row[4]}")     
    else:
        print("Can't find contact.")
        
def delete_contact():
    id = input("Enter the id to delete: ")
    conn = sqlite3.connect("contacts.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM contacts WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print(f"Deleted contact with id: {id}.")
    
    
def main():
    while True:
        print("\n===Contact Book===")    
        print("1. View contact.")
        print("2. Add contact.")
        print("3. Search contact.")
        print("4. Delete contact.")
        print("5. Exit.")
        
        choice = input("Select: ")
        if choice == '1':
            view_contact()
        elif choice == '2':
            add_contact()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exit.")
            break
        else:
            print("Invalid select. Please try again.")
            
if __name__=="__main__":
    main()            
                     
                                         