import tkinter as tk
from tkinter import messagebox

# Function to add task
def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")


# Function to delete task
def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete")

# Function to mark task as completed
def mark_task():
    try:
        selected_task_index = listbox.curselection()[0]
        task = listbox.get(selected_task_index)
        listbox.delete(selected_task_index)
        listbox.insert(tk.END, f"{task} ✔️")
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as completed")

# Main application window
root = tk.Tk()
root.title("To-Do List Application")

# Frame for task entry and buttons
frame = tk.Frame(root)
frame.pack(pady=10)

# Task entry
task_entry = tk.Entry(frame, width=40)
task_entry.pack(side=tk.LEFT, padx=10)

# Add task button
add_button = tk.Button(frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=10)
listbox.pack(pady=10)

# Frame for delete and mark as completed buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Delete task button
delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=10)

# Mark task as completed button
mark_button = tk.Button(button_frame, text="Mark as Completed", command=mark_task)
mark_button.pack(side=tk.LEFT, padx=10)

# Run the application
root.mainloop()