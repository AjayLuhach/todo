from infrastructure.todo_repository import TodoRepository
from domain.todo_item import TodoItem
from infrastructure.database import db

class TodoService:
    def __init__(self, session):
        self.repository = TodoRepository(session)  # Initialize the repository

    def create_todo(self, title, description, name):
        todo_item = TodoItem(title=title, description=description, name=name)
        return self.repository.create_todo(title, description, name)

    def list_todos(self):
        return self.repository.list_todos()

    def get_todo_by_id(self, todo_id):
        return self.repository.get_by_id(todo_id)

    def update_todo(self, todo_id, title, description, name):
        todo_item = self.get_todo_by_id(todo_id)
        
        if todo_item:
            todo_item.title = title
            todo_item.description = description
            todo_item.name = name
            self.repository.update(todo_item)
        
        return todo_item

    def delete_todo(self, todo_id):
        todo_item = self.get_todo_by_id(todo_id)
        
        if todo_item:
            self.repository.delete(todo_item)
            return True
        
        return False
