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
from backend import Database #import Database class from backend

#create object from Database class
#sesnd the db instance to the init function
database = Database("books.db")
#this will enable us to reference database, instead of backend


'''
Place your backend functions
'''


class Window(object):

    def __init__(self, window):

        self.window = window

        self.window.wm_title("Bookstore")

        #window = Tk()


        l1 = Label(window, text="Title")
        l1.grid(row=0, column=0)

        l2 = Label(window, text="Author")
        l2.grid(row=0, column=2)

        l3 = Label(window, text="Year")
        l3.grid(row=1, column=0)

        l4 = Label(window, text="ISBN")
        l4.grid(row=1, column=2)


        self.title_text=StringVar()
        self.e1=Entry(window, textvariable=self.title_text)
        self.e1.grid(row=0, column=1)

        self.author_text=StringVar()
        self.e2=Entry(window, textvariable=self.author_text)
        self.e2.grid(row=0, column=3)

        self.year_text=StringVar()
        self.e3=Entry(window, textvariable=self.year_text)
        self.e3.grid(row=1, column=1)

        self.isbn_text=StringVar()
        self.e4=Entry(window, textvariable=self.isbn_text)
        self.e4.grid(row=1, column=3)

        #Have a listbox + scroll bar
        self.list1=Listbox(window, height=7, width=27)
        self.list1.grid(row=2, column=0, rowspan=7, columnspan=2)

        sb1=Scrollbar(window)
        sb1.grid(row=2, column=2, rowspan=6)

        #Need to add a configuration method to scrollbar and listbox
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        #define bind method (event type + function())
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)


        #Add the right side buttons
        viewall = Button(window, text="View All", width=12, command=self.view_command)
        viewall.grid(row=2, column=3)

        Search = Button(window, text="Search Entry", width=12,command=self.search_command)
        Search.grid(row=3, column=3)

        Add = Button(window, text="Add Entry", width=12, command=self.add_command)
        Add.grid(row=4, column=3)

        Update = Button(window, text="Update Entry", width=12, command=self.update_command)
        Update.grid(row=5, column=3)

        Delete = Button(window, text="Delete Entry", width=12, command=self.delete_command)
        Delete.grid(row=6, column=3)

        Close = Button(window, text="Close", width=12, command=window.destroy)
        Close.grid(row=7, column=3)



    def get_selected_row(self, event):

        try:
            #you need to declare select_tuple variable as global so other functions can access it
            #global select_tuple
            #because it returns a tuple, you need to select just the first element
            index=self.list1.curselection()[0]
            #to get all the valus of the rows of that element 
            self.select_tuple=self.list1.get(index)


            self.e1.delete(0, END)
            self.e1.insert(END,self.select_tuple[1])

            self.e2.delete(0, END)
            self.e2.insert(END,self.select_tuple[2])

            self.e3.delete(0, END)
            self.e3.insert(END,self.select_tuple[3])

            self.e4.delete(0, END)
            self.e4.insert(END,self.select_tuple[4])

        except IndexError:
            pass
            print("list1.curselection()[0] is Empty, add values.")

    def view_command(self):
        self.list1.delete(0, END) 
        for row in database.view():
            self.list1.insert(END, row) #new row will be put in the end

    #place paramenters from the Entry position
    #use .get() method to get a simple string
    def search_command(self):

        self.list1.delete(0, END)
        for row in database.search(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()):
            self.list1.insert(END, row)

    def add_command(self):
        database.insert(self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get()))


    def update_command(self):
        database.update(self.select_tuple[0], self.title_text.get(), self.author_text.get(), self.year_text.get(), self.isbn_text.get())
        self.view_command()

    def delete_command():
        database.delete(self.select_tuple[0])
        self.view_command()

'''
END of functions
'''

window=Tk()
Window(window)
window.mainloop()
