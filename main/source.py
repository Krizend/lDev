import tkinter
from tkinter import ttk
import ctypes
import sqlite3
import datetime

myappid = 'pavel-ivanov.lDev.source.1'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)


class mainWindow:
    def __init__(self):
        width, height = 500, 300

        self.btn_settings = {
            'bg': '#c8dd99',
            'fg': '#6b4a4a',
            'activebackground': '#fff798',
            'activeforeground': '#86bfbf',
            'borderwidth': '0',
            'font': 'Calibri 14',
        }

        self.window = tkinter.Tk()
        # not working
        # self.window.iconbitmap('C:\\lDev\\icon.ico')
        self.window.title('lDev')
        self.window.configure(bg='#add19a')
        self.window.geometry(
            f'{width}x{height}+{self.window.winfo_screenwidth() // 2 - width // 2}+{self.window.winfo_screenheight() // 2 - height // 2}')
        self.window.resizable(False, False)

        self.textinput = tkinter.Text(
            self.window, bg='#edff91', font='Calibri 15', height=10)

        self.menuFrame = tkinter.Frame(self.window, bg='#add19a')
        self.button_send = tkinter.Button(
            self.menuFrame, self.btn_settings, text='Send', command=self.btn_send)
        self.button_openlist = tkinter.Button(
            self.menuFrame, self.btn_settings, text='Openlist', command=self.btn_openlist)
        self.button_exit = tkinter.Button(
            self.menuFrame, self.btn_settings, text='Exit', command=self.btn_exit)

    def db_load(self):
        self.db_connect = sqlite3.connect('data.db')
        self.db_cursor = self.db_connect.cursor()

        self.db_cursor.execute(
            'CREATE TABLE IF NOT EXISTS lDev(string text, datetime text)')
        self.db_connect.commit()

    def db_send(self):
        self.db_cursor.execute('INSERT INTO lDev VALUES(?,?)', (self.textinput.get(
            '1.0', 'end'), str(datetime.datetime.now().strftime('%x %X'))))
        self.db_connect.commit()

        self.textinput.delete('1.0', 'end')

    def db_take(self):
        self.db_cursor.execute('SELECT * FROM lDev ')
        self.db_out = self.db_cursor.fetchall()

    def db_close(self):
        self.db_connect.close()

    def childWindow(self):
        width, height = 500, 300

        child = tkinter.Toplevel(self.window)
        # not working
        # child.iconbitmap('C:\\lDev\\icon.ico')
        child.configure(bg='#add19a')
        child.geometry(
            f'{width}x{height}+{child.winfo_screenwidth() // 2 - width // 2}+{child.winfo_screenheight() // 2 - height // 2}')
        child.resizable(False, False)

        #TODO: openlist scrollbar
        self.db_take()
        scrollbar = tkinter.Scrollbar(child)
        scrollbar.pack(side=tkinter.RIGHT, fill='both')

        mylist = tkinter.Listbox(
            child, yscrollcommand=scrollbar.set, height=21)
        for line in self.db_out:
            mylist.insert(tkinter.END, line[0]+'  '+line[1])

        mylist.pack(fill='both', padx=20)
        scrollbar.config(command=mylist.yview)

        child.mainloop()

    def btn_send(self):
        print('Send button')
        self.db_send()

    def btn_openlist(self):
        print('Openlist button')
        self.childWindow()

    def btn_exit(self):
        print('Exit button')
        self.window.destroy()

    def draw_wigets(self):
        self.textinput.pack()

        self.menuFrame.pack(side=tkinter.BOTTOM, fill=tkinter.BOTH)
        self.button_send.pack(side=tkinter.LEFT, ipadx=15, padx=10, pady=8)
        self.button_openlist.pack(side=tkinter.LEFT, ipadx=15, padx=5)
        self.button_exit.pack(side=tkinter.RIGHT, ipadx=15, padx=10)

    def run(self):
        self.db_load()

        self.draw_wigets()
        self.window.mainloop()

        self.db_close()


def start():
    mainWindow().run()


if __name__ == '__main__':
    start()
