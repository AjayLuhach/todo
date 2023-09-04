# domain/todo_item.py

from infrastructure.database import db

class TodoItem(db.Model):
    __tablename__ = 'Todos1'
    
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000), nullable=True)
    __table_args__ = {'extend_existing': True}

