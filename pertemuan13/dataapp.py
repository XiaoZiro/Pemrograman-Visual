from tkinter import *
from tkinter import ttk

from plotdata import regression_plot
from stats import stats_columns

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Data View")
        self.configure(bg="#F0F0F0")
        self.create_widgets()

    def create_widgets(self):
        self.l0 = Label(self.master, text='CEK STATS & GRAPH', font=('Arial', 16, 'bold'))
        self.l0.configure(background='lightblue', foreground='white')
        self.l0.grid(row=0, columnspan=2, pady=10, sticky='W')

        self.l1 = Label(self.master, text='File Name')
        self.l2 = Label(self.master, text='X Label')
        self.l3 = Label(self.master, text='Y Label')

        self.l1.grid(row=1, sticky='E')
        self.l2.grid(row=2, sticky='E')
        self.l3.grid(row=3, sticky='E')

        self.eFname = Entry(self.master, width=40)
        self.eX = Entry(self.master, width=40)
        self.eY = Entry(self.master, width=40)

        self.eFname.grid(row=1, column=1, sticky='W')
        self.eX.grid(row=2, column=1, sticky='W')
        self.eY.grid(row=3, column=1, sticky='W')

        self.txtX = Text(self.master, width=30, height=10)
        self.txtY = Text(self.master, width=30, height=10)

        self.txtX.grid(row=4, column=0, sticky='W', padx=10)
        self.txtY.grid(row=4, column=1, sticky='W', padx=10)

        self.style = ttk.Style()
        self.style.configure('TButton', foreground='white', font=('Arial', 12, 'bold'))

        self.style.map('TButton',
                       foreground=[('pressed', 'red'), ('active', 'green')],
                       background=[('pressed', '!disabled', 'black'), ('active', 'white')])

        self.btn = ttk.Button(self.master, text='Show Regression Graph', style='TButton')
        self.btn['command'] = self.show_graph
        self.btn.grid(row=5, column=0, sticky='W', pady=10, padx=10)

        self.stats = ttk.Button(self.master, text='Show Stats', style='TButton')
        self.stats['command'] = self.show_stats
        self.stats.grid(row=5, column=1, sticky='W', pady=10, padx=10)

        self.quit = ttk.Button(self.master, text="Quit", style='TButton', command=self.master.destroy)
        self.quit.grid(row=5, column=1, sticky='E', pady=10, padx=10)

    def show_graph(self):
        regression_plot(self.eFname.get(), self.eX.get(), self.eY.get())

    def show_stats(self):
        xstats, ystats = stats_columns(self.eFname.get(), self.eX.get(), self.eY.get())
        self.txtX.delete('1.0', END)
        self.txtY.delete('1.0', END)
        self.txtX.insert(INSERT, xstats)
        self.txtY.insert(INSERT, ystats)

root = Tk()
root.configure(bg="#F0F0F0")
app = Application(master=root)
app.mainloop()