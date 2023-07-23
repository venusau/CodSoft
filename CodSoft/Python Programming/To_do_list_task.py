from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('insert into tasks values (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        selected_item = task_listbox.curselection()
        if selected_item:
            the_value = task_listbox.get(selected_item)
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('delete from tasks where title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    tasks.clear()
    the_cursor.execute('delete from tasks')
    list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()

def retrieve_database():
    tasks.clear()
    for row in the_cursor.execute('select title from tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.configure(bg="#F2F2F2")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('create table if not exists tasks (title text)')
    tasks = []

    header_frame = Frame(guiWindow, bg="#4287f5", pady=20)
    header_frame.pack(fill="x")

    header_label = Label(header_frame, text="To Do List", font=("Arial", 32, "bold"), bg="#4287f5", fg="white")
    header_label.pack()

    button_frame = Frame(guiWindow, bg="#F2F2F2")
    button_frame.pack(side="left", padx=20, pady=20)

    task_label = Label(button_frame, text="Enter the Task:", font=("Arial", "16", "bold"), bg="#F2F2F2", fg="#000000")
    task_label.grid(row=0, column=0, pady=10, sticky="w")

    task_field = Entry(button_frame, font=("Arial", "14"), width=30, foreground="#000000", bg="#FFFFFF")
    task_field.grid(row=1, column=0, pady=10)

    add_button = Button(button_frame, text="Add Task", width=15, font=("Arial", "14", "bold"), bg='#56B27D', fg="white", command=add_task)
    add_button.grid(row=2, column=0, pady=10)

    del_button = Button(button_frame, text="Delete Task", width=15, font=("Arial", "14", "bold"), bg='#E74C3C', fg="white", command=delete_task)
    del_button.grid(row=3, column=0, pady=10)

    del_all_button = Button(button_frame, text="Delete All Tasks", width=15, font=("Arial", "14", "bold"), bg='#A6ACAF', fg="white", command=delete_all_tasks)
    del_all_button.grid(row=4, column=0, pady=10)

    display_frame = Frame(guiWindow, bg="#F2F2F2")
    display_frame.pack(side="right", padx=20, pady=20)

    task_listbox = Listbox(display_frame, width=40, height=13, font=("Arial", "14"), selectmode='SINGLE', bg="#FFFFFF", fg="#000000",
                           selectbackground="#E74C3C", selectforeground="#FFFFFF")
    task_listbox.pack(expand=True, fill="both")

    retrieve_database()
    list_update()

    guiWindow.mainloop()

    the_connection.commit()
    the_cursor.close()
