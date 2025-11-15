import json
import os
import argparse
from datetime import datetime

TASK_FILE  = 'task-traker.json'
VALID_STATUS = ['to-do','in-progress','done']

def current_time():
    return datetime.now().strftime('%d %b %Y, %I %M %p')


def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE,"r") as file:
            return json.load(file)
    return {"last_id":0,"tasks":[]}

def save_tasks(data):
    with open(TASK_FILE,"w") as file:
        json.dump(data,file,indent=4)    


def add_task(description):
    data = load_tasks()
    data["last_id"] += 1
    task_id = data["last_id"]
    now = current_time()
    data['tasks'].append({
        'id':task_id,
        'description': description,
        'status': 'to-do',
        'created_at': now,
        'updated_at': now
    })
    save_tasks(data)
    print(f"Task success added (ID: {task_id}, status: to-do)")


def list_task():
    data = load_tasks()
    if not data['tasks']:
        print('No tasks yet.')
        return
    for task in data ['tasks']:
        status_icon ={
            'to-do': '⏳',
            'in-progress': '📝',
            'done': '✅'
        }.get(task['status'], '?')
        print(f"{[status_icon]} {task['id']}: {task['description']} ({task['status']}")
        print(f"  Created: {task['created_at']}")
        print(f"  Updated: {task['updated_at']}")
        
def update_status(task_id,new_status):
    if new_status not in VALID_STATUS:
        print(f"Invalid status, Use on of: {', '.join(VALID_STATUS)}")
        return 
    data = load_tasks()
    for task in data['tasks']:
        if task['id'] == task_id:
            task['status'] = new_status
            task['updated_at']  = current_time()
            save_tasks(data)
            print(f"Task {task_id} status update to '{new_status}'.")
            return 
        print(f"No task found with ID {task_id}.")
        
def delete_task(task_id):
    data = load_tasks()
    for task in data['tasks']:
        data['tasks'].remove(task)
        save_tasks(data)
        print(f"Task {task_id} deleted.")
        return
    print(f"No task found with ID {task_id}.")
    
def main():
    parser = argparse.ArgumentParser(description='Simple Task Tracker Using CLI')
    subparsers = parser.add_subparsers(dest='command')

    # add command
    add_parser = subparsers.add_parser('add', help='Add new task')
    add_parser.add_argument('description', type=str, help='Task description')

    # list command
    subparsers.add_parser('list', help='List all tasks')

    # Update status
    status_parser = subparsers.add_parser('status', help='Update task status')
    status_parser.add_argument('id', type=int, help='Task ID')
    status_parser.add_argument('status', type=str, help='New status')

    # delete tasks
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='Task ID')

    args = parser.parse_args()
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'list':
        list_task()
    elif args.command == 'status':
        update_status(args.id, args.status)
    elif args.command == 'delete':
        delete_task(args.id)
    else:
        parser.print_help()

# example CLI usage

if __name__ == '__main__':
    main()
    