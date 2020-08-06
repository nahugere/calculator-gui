from tkinter import *
from tkinter import ttk
from history import DataBase

db = DataBase('db.db')

class Calc:

    first_val = ''
    valid_char = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '=', '√', '*', '/']
    ops = ['+', '-', '=', '√', '*', '/']

    def __init__(self):
        self.master = Tk()
        self.master.geometry('365x537')
        self.master.title("PyCalculator")
        self.set_up_gui()
        self.master.mainloop()

    def del_click(self, event):
        val = self.entry.get()
        if val[0]=="=" or val=="Error!":
            self.entry.delete(0, END)
        if self.entry["fg"]=="grey":
            self.entry["fg"]="black"
            self.entry.delete(0, END)

    def del_last(self):
        val = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, val[:-1])

    def insert_char(self, char):
        to_be_inserted = str(self.entry.get())+char
        a = to_be_inserted[0]=='='
        if a:
            self.entry.delete(0, END)
            to_be_inserted = to_be_inserted[-1]
        if self.entry["fg"]=="grey":
            self.entry["fg"]="black"
            self.entry.delete(0, END)
            self.entry.insert(0, char)
        else:
            self.entry.delete(0, END)
            self.entry.insert(0, to_be_inserted)

    def add_func(self):
        val = self.entry.get()
        self.first_val = val
        print(self.first_val)

    def list_it(self):
        self.lst.delete(0, END)
        vals = db.get_all()
        for i in vals:
            text = i[1]+i[2]
            self.lst.insert(0, text)
            self.lst.insert(0, '')

    def equal_func(self):
        try:
            qt = str(self.entry.get())
            equation = eval(self.entry.get())
            self.entry.delete(0, END)
            last_ans = str(equation)
            self.entry.insert(4, last_ans)
            ans = "="+str(equation)
            db.add_to_history(qt, ans)
        except Exception:
            self.entry.delete(0, END)
            self.entry.insert(0, 'Error!')
        try:
            self.list_it()
        except AttributeError:
            pass

    def clear_func(self):
        self.entry.delete(0, END)
        self.entry.config(fg="grey")
        self.entry.insert(0, 0)

    def sqrt_func(self):
        self.insert_char("//")

    def history_func(self, val):
        if val==1:
            self.frame6 = Frame(self.master, bg="white")
            self.master.geometry("670x537")
            self.lst = Listbox(self.frame6, font=("roboto", 15), border=0)
            self.lst.pack(fill=BOTH, side=LEFT,expand=1)
            self.list_it()
            self.frame6.pack(side=LEFT, fill=BOTH, expand=1, ipadx=0)
            self.history.config(command=lambda: self.history_func(0))
        elif val==0:
            self.master.geometry('365x537')
            self.frame6.forget()
            self.history.config(command=lambda: self.history_func(1))

    def set_up_gui(self):
        # creating frames
        self.frame1 = Frame(self.master, bg="white")
        self.frame2 = Frame(self.master, bg="white")
        self.frame3 = Frame(self.master, bg="white")
        self.frame4 = Frame(self.master, bg="white")
        self.frame5 = Frame(self.master, bg="white")

        # creating the entry  #e6e3da
        self.history = Button(self.frame1, border=0, relief="flat", width=4, text="H", fg="#a28631", bg="white", font=("roboto", 15), command=lambda: self.history_func(1))
        self.entry = Entry(self.frame1, border=0, insertbackground="#b9b8b5", bg="white", fg="grey", font=("arial", 38))
        self.entry.insert(0, 0)
        self.entry.bind("<Button-1>", self.del_click)
        self.entry.bind("<KeyPress>", self.del_click)

        # creating other elements
        self.zero = Button(self.frame2, text="0", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("0"))
        self.one = Button(self.frame2, text="1", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("1"))
        self.four = Button(self.frame2, text="4", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("4"))
        self.seven = Button(self.frame2, text="7", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("7"))
        self.clear = Button(self.frame2, text="C", font=("roboto", 15), bg="#e6e3da", border=0, fg="red", command=lambda: self.clear_func())

        self.dot = Button(self.frame3, text=".", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("."))
        self.two = Button(self.frame3, text="2", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("2"))
        self.five = Button(self.frame3, text="5", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("5"))
        self.eight = Button(self.frame3, text="8", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("8"))
        self.mod = Button(self.frame3, text="%", font=("roboto", 15), bg="#e6e3da", border=0, fg="#a28631", command=lambda: self.insert_char("%"))

        self.plus = Button(self.frame4, text="+", fg="#a28631", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("+"))
        self.three = Button(self.frame4, text="3", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("3"))
        self.six = Button(self.frame4, text="6", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("6"))
        self.nine = Button(self.frame4, text="9", fg="black", bg="white", font=("roboto", 15), border=0, command=lambda: self.insert_char("9"))
        self.sqrt = Button(self.frame4, text="//", font=("roboto", 15), bg="#e6e3da", border=0, fg="#a28631", command=lambda: self.sqrt_func())

        self.equal = Button(self.frame5, text="=", fg="#e600ce", bg="#e6e3da", font=("roboto", 15), border=0, command=lambda: self.equal_func())
        self.minus = Button(self.frame5, text="-", fg="#a28631", bg="#e6e3da", font=("roboto", 15), border=0, command=lambda: self.insert_char("-"))
        self.times = Button(self.frame5, text="*", fg="#a28631", bg="#e6e3da", font=("roboto", 15), border=0, command=lambda: self.insert_char("*"))
        self.div = Button(self.frame5, text="/", fg="#a28631", bg="#e6e3da", font=("roboto", 15), border=0, command=lambda: self.insert_char("/"))
        self.back = Button(self.frame5, text="←", font=("roboto", 15), bg="#e6e3da", border=0, fg="#a28631", command=lambda: self.del_last())

        # putting frames on the screen
        self.frame1.pack(fill=X, side=TOP)
        self.frame2.pack(expand=1, fill=BOTH, side=LEFT, anchor=W)
        self.frame3.pack(expand=1, fill=BOTH, side=LEFT, anchor=E)
        self.frame4.pack(expand=1, fill=BOTH, side=LEFT, anchor=W)
        self.frame5.pack(expand=1, fill=BOTH, side=LEFT, anchor=E)

        #putting the entry on the screen
        self.history.pack(fill=BOTH, side=RIGHT)
        self.entry.pack(fill=BOTH, expand=1, ipady=30, padx=(40, 2), pady=(40, 1))

        #putting the numbers on the screen
        self.zero.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.one.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.four.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.seven.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.clear.pack(fill=BOTH, expand=1, side=BOTTOM)

        self.dot.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.two.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.five.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.eight.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.mod.pack(fill=BOTH, expand=1, side=BOTTOM)

        self.plus.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.three.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.six.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.nine.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.sqrt.pack(fill=BOTH, expand=1, side=BOTTOM)

        self.equal.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.minus.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.times.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.div.pack(fill=BOTH, expand=1, side=BOTTOM)
        self.back.pack(fill=BOTH, expand=1, side=BOTTOM)

app = Calc()
