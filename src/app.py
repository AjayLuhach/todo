from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from controllers.todo_controler import todo_controller
from services.todo_service import TodoService
from infrastructure.database import db

app = Flask(__name__)
app.config.from_object('config')

db.init_app(app)

# Register the todo controller blueprint
app.register_blueprint(todo_controller, url_prefix='/')

# Initialize the TodoService with the database session
todo_service = TodoService(db.session)

if __name__ == "__main__":
    app.run(debug=True)
