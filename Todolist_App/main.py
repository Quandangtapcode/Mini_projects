import requests
from datetime import datetime 

API_URL = "http://localhost:5000/api/tasks"

    
def get_tasks():
    response = requests.get(API_URL)
    tasks = response.json()
    print("\n===List tasks===")
    for task in tasks:
        print(f"[{task['id']}] {task['title']} - Deadline: {task['deadline']} - Status: {task['status']}")
        print("") 

def add_task():
    title = input("Enter the name task:")
    deadline = input("Enter deadline (YYYY-MM-DD):").strip()
    
    try:
        datetime.strptime(deadline, "%Y-%m-%d")
    except ValueError:
        print("Deadline must be in format YYYY-MM-DD")
        return
    
    response = requests.post(API_URL, json ={"title": title, "deadline": deadline})
    
    try:
        data = response.json()
        print(data.get("message") or data.get("error"))
    except ValueError:
        print("Error: Could not decode response.")    
    
    


def update_task_by_id():
    task_id = input("Enter ID task need to check: ")
    response = requests.get(API_URL)
    tasks = response.json()
    task_exists = any( task['id'] == int(task_id) for task in tasks)
    if not task_exists:
        print(f"Error: Task with ID {task_id} not found.")
        return
    
    response = requests.patch(f"{API_URL}/{task_id}")
    if response.status_code == 200:
        print(response.json().get("message"))
    else:
        print(f"Error: Task with ID {task_id} not found.")    
    
    
    
    
def delete_task_by_id():
    task_id = input("Enter ID task need to deleted:")
    response = requests.delete(f"{API_URL}/{task_id}")
    print(response.json()["message"])
    
    
    
def delete_all_tasks():
    confirm = input("Are you sure you want to delete all the tasks? (yes/no):")
    if confirm.lower() == 'yes':
        response = requests.delete(API_URL)
        print(response.json()["message"])
    else:
        print("Cancel manipulation.")            
        

def main():
    while True:
        print("""
======== TO-DO LIST APP =========
1. List tasks
2. Add task
3. Update task by id
4. Delete task by id
5. Delete all tasks
6. Exit
""")
        choice = input("Select : ")
        if choice == '1':
            get_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            update_task_by_id()    
        elif choice == '4':
            delete_task_by_id()
        elif choice == '5':
            delete_all_tasks()
        elif choice == '6':
            print("Exit.") 
            break
        else:
            print("Invalid select.")

if __name__ == "__main__":
    main()
