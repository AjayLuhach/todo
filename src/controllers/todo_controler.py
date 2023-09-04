from flask import Blueprint, request, jsonify
from infrastructure.database import db
from services.todo_service import TodoService

# Create a Blueprint for the todo controller
todo_controller = Blueprint('todo_controller', __name__)

# Initialize the TodoService
todo_service = TodoService(db.session)

@todo_controller.route('/')
def home():
    return "Welcome to the Todo App!"
#curl -X POST -H "Content-Type: application/json" -d '{"name":"ajay","title": "programming", "description": "lets do the progrmaingi"}' http://localhost:5000/create
@todo_controller.route('/create', methods=['POST'])
def create_todo():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    name = data.get('name')

    # Create a Todo item using the TodoService
    todo_item = todo_service.create_todo(title, description, name)

    return f"Created todo: {todo_item.title}"

@todo_controller.route('/list')
def list_todos():
    # Get the list of TodoItem objects from the TodoService
    todos = todo_service.list_todos()

    # Convert TodoItem objects to a list of dictionaries
    todo_list = [{"id": todo.id, "title": todo.title, "description": todo.description, "name": todo.name} for todo in todos]

    return jsonify(todo_list)
#curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Title", "description": "Updated Description", "name": "Updated Name"}' http://localhost:5000/update/2

@todo_controller.route('/update/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.json
    title = data.get('title')
    description = data.get('description')
    name = data.get('name')

    # Update the Todo item using the TodoService
    updated_todo = todo_service.update_todo(todo_id, title, description, name)

    if updated_todo:
        return f"Updated todo: {updated_todo.title}"
    else:
        return "Todo not found", 404


#curl command to delete curl -X DELETE http://localhost:5000/delete/1

@todo_controller.route('/delete/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    success = todo_service.delete_todo(todo_id)

    if success:
        return "Todo deleted"
    else:
        return "Todo not found", 404
