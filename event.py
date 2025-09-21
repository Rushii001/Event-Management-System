from tkinter import *
import database

def get_selected_row(event):
    try:
        global selected_tuple
        index = listbox.curselection()[0]
        selected_tuple = listbox.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
    except IndexError:
        pass

def view_command():
    listbox.delete(0, END)
    for row in database.view():
        listbox.insert(END, row)

def add_command():
    database.insert(name_text.get(), date_text.get(), location_text.get())
    view_command()

def delete_command():
    database.delete(selected_tuple[0])
    view_command()

def update_command():
    database.update(selected_tuple[0], name_text.get(), date_text.get(), location_text.get())
    view_command()

# GUI Setup
window = Tk()
window.title("Event Management System")

# Labels
Label(window, text="Event Name").grid(row=0, column=0)
Label(window, text="Date").grid(row=0, column=2)
Label(window, text="Location").grid(row=1, column=0)

# Entry fields
name_text = StringVar()
e1 = Entry(window, textvariable=name_text)
e1.grid(row=0, column=1)

date_text = StringVar()
e2 = Entry(window, textvariable=date_text)
e2.grid(row=0, column=3)

location_text = StringVar()
e3 = Entry(window, textvariable=location_text)
e3.grid(row=1, column=1)

# Listbox
listbox = Listbox(window, height=8, width=50)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

# Scrollbar
sb = Scrollbar(window)
sb.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=sb.set)
sb.configure(command=listbox.yview)
listbox.bind('<<ListboxSelect>>', get_selected_row)

# Buttons
Button(window, text="View All", width=12, command=view_command).grid(row=2, column=3)
Button(window, text="Add Event", width=12, command=add_command).grid(row=3, column=3)
Button(window, text="Update Event", width=12, command=update_command).grid(row=4, column=3)
Button(window, text="Delete Event", width=12, command=delete_command).grid(row=5, column=3)
Button(window, text="Close", width=12, command=window.quit).grid(row=6, column=3)

database.connect()
window.mainloop()