import tkinter as tk
from tkinter import font
from database import connection, tasks
from TaskManager import TaskManager
from Task import Task
from helpers import *

task_manager = TaskManager(connection, tasks)
selected_tasks = []

root = tk.Tk()
root.title("To-Do List") 
# root.geometry("800x600")
root.state('zoomed')

# Define fonts
default_font = font.Font(family="Arial", size=9)
strike_font = font.Font(family="Arial", size=9, overstrike=True)
subtitle_font = font.Font(family="Arial", size=10, weight="bold")

# Title Frame

title_frame = tk.Frame(root, pady=20)
title_frame.pack()

tk.Label(title_frame, text="To-Do List", font=("Arial", 14, "bold")).pack()

###

frame0 = tk.LabelFrame(root, pady=10, padx=10, text="Add New Task")
frame0.pack(fill="x", padx=10, pady=10)

frame1 = tk.Frame(frame0)
frame1.pack(fill="x")

# Title Input Group

title_input_group = tk.Frame(frame1)
title_input_group.pack(side="left", fill="x", expand=True, padx=5)

tk.Label(title_input_group, text="Task Title", anchor="w").pack(pady=10, expand=True, fill="x")

titleInput = tk.Entry(title_input_group)
titleInput.pack(fill="x", ipady=5)

# Description Input Group

description_input_group = tk.Frame(frame1)
description_input_group.pack(side="left", fill="x", expand=True, padx=5)

tk.Label(description_input_group, text="Task Description", anchor="w").pack(pady=10, expand=True, fill="x")

descriptionInput = tk.Entry(description_input_group)
descriptionInput.pack(fill="x", ipady=5)

# Priority Select Group

priority_select_group = tk.Frame(frame1)
priority_select_group.pack(side="right", fill="x", expand=True, padx=5)

tk.Label(priority_select_group, text="Task Priority", anchor="w").pack(pady=10, expand=True, fill="x")

options = ["High", "Medium", "Low"]
selected_priority = tk.StringVar(value=options[0])
dropdown = tk.OptionMenu(priority_select_group, selected_priority, *options)
dropdown.pack(ipady=1, fill="x")

# Frame for the button

frame2 = tk.Frame(frame0, pady=15)
frame2.pack(fill="x")

add_task_button = tk.Button(frame2, text="Add Task", bg="dodgerblue", borderwidth=1, fg="white", font=("Arial", 10, "bold"))
add_task_button.pack(side="left", padx=7, ipadx=10, ipady=3)

# Frame 3

frame3 = tk.Frame(root, pady=15, padx=10)
frame3.pack(fill="both", expand=True)

# Tasks List: To Do

to_do_tasks_container = tk.Frame(frame3, bd=1, relief="ridge")
to_do_tasks_container.pack(fill="both", side="left", expand=True, padx=5, pady=5)

to_do_tasks_label = tk.Label(to_do_tasks_container, text="To Do", fg="red", font=("Arial", 12, "bold"), pady=10)
to_do_tasks_label.pack()

to_do_tasks = tk.Frame(to_do_tasks_container, bg="white")
to_do_tasks.pack(fill="both", expand=True)

display_tasks(tk, to_do_tasks, task_manager.tasks_list['To-Do'], selected_tasks)

### Buttons

left_buttons_frame = tk.Frame(frame3)
left_buttons_frame.pack(side="left", padx=5, pady=5)

move_to_doing_btn1 = tk.Button(left_buttons_frame, borderwidth=1, text="=>")
move_to_doing_btn1.pack(pady=5)
tk.Button(left_buttons_frame, borderwidth=1, text="<=").pack(pady=5)

# Tasks List: Doing

doing_tasks_container = tk.Frame(frame3, bd=1, relief="ridge")
doing_tasks_container.pack(fill="both", side="left", expand=True, padx=5, pady=5)

doing_tasks_label = tk.Label(doing_tasks_container, text="Doing", fg="orangered", font=("Arial", 12, "bold"), pady=10)
doing_tasks_label.pack()

doing_tasks = tk.Frame(doing_tasks_container, bg="white")
doing_tasks.pack(fill="both", expand=True)

display_tasks(tk, doing_tasks, task_manager.tasks_list['Doing'], selected_tasks)

# Buttons

right_buttons_frame = tk.Frame(frame3)
right_buttons_frame.pack(side="left", padx=5, pady=5)

tk.Button(right_buttons_frame, borderwidth=1, text="=>").pack(pady=5)
tk.Button(right_buttons_frame, borderwidth=1, text="<=").pack(pady=5)

# Tasks List: Done

done_tasks_container = tk.Frame(frame3, bd=1, relief="ridge")
done_tasks_container.pack(fill="both", side="left", expand=True, padx=5, pady=5)

done_tasks_label = tk.Label(done_tasks_container, text="Done", fg="green", font=("Arial", 12, "bold"), pady=10)
done_tasks_label.pack()

done_tasks = tk.Frame(done_tasks_container, bg="white")
done_tasks.pack(fill="both", expand=True)


display_tasks(tk, done_tasks, task_manager.tasks_list['Done'], selected_tasks)

# Action Buttons

frame4 = tk.Frame(root)
frame4.pack(fill="x", side="left", padx=15, pady=15)

delete_tasks_button = tk.Button(frame4, text="Delete Task(s)", padx=10, pady=5, bd=1, relief="ridge", background="red", fg="white", font=("Arial", 10, "bold"), command=lambda: delete_tasks(selected_tasks, task_manager))
delete_tasks_button.pack(side="left")

modify_tasks_button = tk.Button(frame4, text="Modify Task", padx=10, pady=5, bd=1, relief="ridge", background="dodgerblue", fg="white", font=("Arial", 10, "bold"))
modify_tasks_button.pack(side="left", padx=10)


# Tasks List

tasks = []
selected_task = None

# Adding Events

def unselect_tasks():
    for task in tasks:
        task.config(bg="white")
        for child in task.winfo_children():
            child.config(bg="white")


def add_task(_):
    title = titleInput.get()
    description = descriptionInput.get()
    if (title.strip() != "" and description.strip() != ""):
       
        # Task Content

        task = Task(0, title, description, selected_priority.get())
        task_manager.store(task)

        create_task(tk, to_do_tasks, 0, title, description, selected_priority.get(), selected_tasks)

        # new_task.bind("<Button-1>", lambda _: select_task(new_task))
        # new_task_title.bind("<Button-1>", lambda _: select_task(new_task))
        # new_task_description.bind("<Button-1>", lambda _: select_task(new_task))

        titleInput.delete(0, len(title))
        descriptionInput.delete(0, len(description))


def mark_as_done(task):
    for child in task.winfo_children():
        child.config(text="Yo")

add_task_button.bind("<Button-1>", add_task)

move_to_doing_btn1.bind('<Button-1>', lambda _: move_task(tk, selected_tasks, doing_tasks_container, task_manager, "Doing"))
# move_to_doing_btn2.bind('<Button-1>', lambda _: move_task(tk, selected_tasks, doing_tasks_container, task_manager, "Doing"))
# move_to_to_do.bind('<Button-1>', lambda _: move_task(tk, selected_tasks, doing_tasks_container, task_manager, "Doing"))
# move_to_done.bind('<Button-1>', lambda _: move_task(tk, selected_tasks, doing_tasks_container, task_manager, "Doing"))

root.bind('<Escape>', lambda _: unselect_all(selected_tasks))

root.mainloop()