def create_task(tk, tasks_container, id, title, description, priority, selected_tasks = []):
    new_task = tk.Frame(tasks_container, bg="white", padx=10, pady=7)
    new_task.pack(fill="x")

    # ID

    tk.Label(new_task, text=id)

    # Frame for details

    new_task_details = tk.Frame(new_task)
    new_task_details.pack(side="left", fill="x")

    # Title

    new_task_title = tk.Label(new_task_details, text=title, fg="dodgerblue", pady=0, bg="white", anchor="w", font=("Arial", 10, "bold"))
    new_task_title.pack(fill="x")

    # Description

    new_task_description = tk.Label(new_task_details, text=description, pady=0, bg="white", anchor="w", font=("Arial", 8))
    new_task_description.pack(fill="x")

    # Priority Color

    color = "red" if priority == "High" else ("orangered" if priority == "Medium" else "green")

    # Priority

    new_task_priority = tk.Label(new_task, text=priority, pady=0, fg=color, bg="white", anchor="w", font=("Arial", 8))
    new_task_priority.pack(fill="y", side="right")

    # Bind Click Event

    new_task.bind('<Button-1>', lambda _: select_task(new_task, selected_tasks))

def display_tasks(tk, tasks_container, tasks, selected_tasks = []):
    for task in tasks:
        create_task(tk, tasks_container, task.id, task.title, task.description, task.priority, selected_tasks)

# Select a Task

def select_task(task, selected_tasks):
    highlight_task(task)
    selected_tasks.append(task)

def highlight_task(element):
    element.config(bg="#DDD")
    for child in element.winfo_children():
        highlight_task(child)
    

# Delete a Task

def delete_tasks(tasks, task_manager):
    for task in tasks:
        id = task.winfo_children()[0].cget("text")
        task_manager.delete(id)
        task.destroy()


# Unselect all tasks

def unselect_all(tasks):
    unmark_task(tasks)
    tasks.clear()

def unmark_task(tasks):
    for task in tasks:
        task.config(bg="white")
        unmark_task(task.winfo_children())

# Move Task

def move_task(tk, tasks, new_container, task_manager, new_status):
    for task in tasks:
        id = task.winfo_children()[0].cget("text")
        
        t = list(filter(lambda x: x.id == id, task_manager.tasks_list['To-Do']))

        if (not len(t)):
            t = list(filter(lambda x: x.id == id, task_manager.tasks_list['Doing']))

        if (not len(t)):
            t = list(filter(lambda x: x.id == id, task_manager.tasks_list['Done']))

        t = t[0]

        task_manager.update(id, new_status)

        create_task(tk, new_container, t.id, t.title, t.description, t.priority)

        task.destroy()

        tasks.clear()