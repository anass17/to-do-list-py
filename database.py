from sqlalchemy import *

connection = create_engine("postgresql://postgres:123456789@localhost:5432/todo_list")

metadata = MetaData()

tasks = Table(
    "tasks",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String),
    Column("description", Text),
    Column("priority", Enum('High', 'Low', 'Medium', name="priority_enum")),
    Column("status", Enum('To-Do', 'Doing', 'Done', name="status_enum")),
)

metadata.create_all(connection)