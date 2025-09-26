from sqlalchemy import *
from Task import Task

class TaskManager:
    def __init__(self, connection, tasks):
        self.tasks_list = {"To-Do": [], "Doing": [], "Done": []}
        self.connection = connection
        self.tasks = tasks

        self.index()

    def store(self, task):
        with self.connection.begin() as conn:
            stmt = insert(self.tasks).values({"title": task.title, "description": task.description, "priority": task.priority, "status": task.status})
            conn.execute(stmt)
        
        self.tasks_list[task.status].append(task)

        print("Hello")
        pass

    def index(self):
        with self.connection.begin() as conn:
            stmt = (
                select(
                    self.tasks.c.id,
                    self.tasks.c.title,
                    self.tasks.c.description,
                    self.tasks.c.priority,
                    self.tasks.c.status
                ).select_from(self.tasks)
            )
            result = conn.execute(stmt)

            for row in result:
                task = Task(row[0], row[1], row[2], row[3])
                self.tasks_list[row[4]].append(task)



    def delete(self, id):
        with self.connection.begin() as conn:
            stmt = delete(self.tasks).where(self.tasks.c.id == id)
            conn.execute(stmt)

            # add code to filter the list of tasks here !!!

    def update(self, id, new_status):
        with self.connection.begin() as conn:

            stmt = (
                update(self.tasks)
                .where(self.tasks.c.id == id)
                .values(status=new_status)
)
            conn.execute(stmt)