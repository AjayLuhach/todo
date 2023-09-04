from domain.todo_item import TodoItem
from infrastructure.database import db

class TodoRepository:
    def __init__(self, session):
        self.session = session

    def create_todo(self, title, description, name):
        todo_item = TodoItem(title=title, description=description, name=name)
        self.session.add(todo_item)
        self.session.commit()
        return todo_item

    def list_todos(self):
        return self.session.query(TodoItem).all()

    def get_by_id(self, todo_id):
        return self.session.query(TodoItem).filter_by(id=todo_id).first()

    def update(self, todo_item):
        self.session.commit()

    def delete(self, todo_item):
        self.session.delete(todo_item)
        self.session.commit()
