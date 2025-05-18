from flask import Flask, request, jsonify
from db import get_connection
from datetime import datetime 

app = Flask(__name__)

# check task exists 
def task_exists(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM tasks WHERE id = %s", (task_id,))
    result = cursor.fetchone()
    conn.close()
    return result is not None
    
# get all tasks
@app.route("/api/tasks", methods = ["GET"])
def get_tasks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tasks ORDER BY deadline")
    tasks = cursor.fetchall()
    conn.close()
    return jsonify(tasks)   
 
 
 
# add task
@app.route("/api/tasks", methods = ["POST"])
def add_task():
    data = request.json
    print("Received JSON:", data)
    title = data.get("title")
    deadline = data.get("deadline")
    
    if not title:
        return jsonify({"error": "Title is required."})
    
    try:
        deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
    except (ValueError, TypeError):
        return jsonify({"error": "Deadline must be in format YYYY-MM-DD"})
    
    
    today = datetime.today().date()
    if deadline < today:
        return jsonify({"error": "Deadline can not be in the past."})
            
   
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks(title, deadline) VALUES (%s, %s)", (title, deadline))
    task_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({"message": f"Added task with id {task_id}"})



# update task by id 
@app.route("/api/tasks/<int:task_id>", methods = ["PATCH"])
def update_task_by_id(task_id):
    data = request.json
    new_title = data.get("title")
    new_deadline = data.get("deadline")
    new_status = data.get("status")
    
    if not task_exists(task_id):
        return jsonify({"Error": "Task not found"})
    
    valid_statuses = ["pending", "processing", "cancelled", "done"]
    if new_status is not None and new_status not in valid_statuses:
        return jsonify({"Error": "Invalid status"})
    
    
    conn = get_connection()
    cursor = conn.cursor()
    if new_title is not None:
        cursor.execute("UPDATE tasks SET title = %s WHERE id = %s ", (new_title, task_id))
    if new_deadline is not None:    
        cursor.execute("UPDATE tasks SET deadline = %s WHERE id = %s ", (new_deadline, task_id))
    if new_status is not None:
        cursor.execute("UPDATE tasks SET status = %s WHERE id = %s ", (new_status, task_id))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Update task with id {task_id} complete ."})

# delete task by id
@app.route("/api/tasks/<int:task_id>", methods = ["DELETE"])
def delete_task_by_id(task_id):
    
    if not task_exists(task_id):
        return jsonify({"Error": "Task not found"})
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
    conn.commit()
    conn.close()
    return jsonify({"message": f"Delete task with id {task_id} complete."})

# delete all tasks
@app.route("/api/tasks", methods = ["DELETE"])
def delete_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    cursor.execute("ALTER TABLE tasks AUTO_INCREMENT = 1")
    conn.commit()
    conn.close()
    return jsonify({"message": "Deleted all tasks"})

if __name__ == '__main__':
    app.run(debug=True)
    
 
    