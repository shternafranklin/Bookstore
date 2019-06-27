'''
A program that stores this book information:
Title, Author, Year and ISBM

User Can:
View all records
Search
Add Entry
Update entry
Delete
Close
'''


from tkinter import *
import backend


'''
Place your backend functions
'''

def get_selected_row(event):

    try:
        #you need to declare select_tuple variable as global so other functions can access it
        global select_tuple
        #because it returns a tuple, you need to select just the first element
        index=list1.curselection()[0]
        #to get all the valus of the rows of that element 
        select_tuple=list1.get(index)


        e1.delete(0, END)
        e1.insert(END,select_tuple[1])

        e2.delete(0, END)
        e2.insert(END,select_tuple[2])

        e3.delete(0, END)
        e3.insert(END,select_tuple[3])

        e4.delete(0, END)
        e4.insert(END,select_tuple[4])

    except IndexError:
        pass
        print("list1.curselection()[0] is Empty, add values.")


def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row) #new row will be put in the end

#place paramenters from the Entry position
#use .get() method to get a simple string
def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))


def update_command():
    backend.update(select_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def delete_command():
    backend.delete(select_tuple[0])
    view_command()


#close


'''
END of functions
'''

window = Tk()

#title
window.wm_title("Bookstore")

l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)


title_text=StringVar()
e1=Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text=StringVar()
e2=Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text=StringVar()
e3=Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text=StringVar()
e4=Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

#Have a listbox + scroll bar
list1=Listbox(window, height=7, width=27)
list1.grid(row=2, column=0, rowspan=7, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

#Need to add a configuration method to scrollbar and listbox
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

#define bind method (event type + function())
list1.bind('<<ListboxSelect>>', get_selected_row)


#Add the right side buttons
viewall = Button(window, text="View All", width=12, command=view_command)
viewall.grid(row=2, column=3)

Search = Button(window, text="Search Entry", width=12,command=search_command)
Search.grid(row=3, column=3)

Add = Button(window, text="Add Entry", width=12, command=add_command)
Add.grid(row=4, column=3)

Update = Button(window, text="Update Entry", width=12, command=update_command)
Update.grid(row=5, column=3)

Delete = Button(window, text="Delete Entry", width=12, command=delete_command)
Delete.grid(row=6, column=3)

Close = Button(window, text="Close", width=12, command=window.destroy)
Close.grid(row=7, column=3)


window.mainloop()
