from flask import Flask, render_template, request, redirect
import sqlalchemy
from typing import Optional
from sqlalchemy import Table, Column, Integer, String, select
from sqlalchemy.orm import Session, DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True)
    label: Mapped[str] = mapped_column(String(30))
    note: Mapped[Optional[str]]

    def __repr__(self):
        return f"Todo(id={self.id!r}, label={self.label!r}, note={self.note!r})"


engine = sqlalchemy.create_engine("sqlite:///todos.db")
db = engine.connect()

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todos.db"

# emit DDL to the database from ORM mappings to create tables
Base.metadata.create_all(engine)


@app.route("/")
def index():
    row_limit = 100
    with Session(engine) as session:
        stmt = select(Todo).limit(row_limit)
        if app.debug:
            print(stmt)
        todos = session.execute(stmt).scalars()
        return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    content = request.form["content"]
    with Session(engine) as session:
        new_todo = Todo(label=content)
        session.add(new_todo)
        session.commit()
    return redirect("/")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id):
    completed = request.form["completed"] == "True"
    todo = Todo.query.get(todo_id)
    todo.completed = completed
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
