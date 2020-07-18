import os
if __name__ == '__main__':
    if os.name == 'nt':
        if os.path.exists('C:/lDev'):
            pass
            #from source import start
            #start()
        else:
            import tkinter

            path = os.path.dirname(__file__)
            width, height = 500, 300

            os.makedirs('C:/lDev')
            if os.path.exists(path + '/sourcecache'):
                os.replace(path + '/sourcecache', 'C:/lDev/source.py')
            if os.path.exists(path + '/iconcache'):
                os.replace(path + '/iconcache', 'C:/lDev/icon.ico')
            if os.path.exists(path + '/executablecache'):
                os.replace(path + '/executablecache', 'C:/lDev/executable.pyw')

            window = tkinter.Tk()
            window.title('lDev install')
            window.geometry(
                f'{width}x{height}+{window.winfo_screenwidth() // 2 - width // 2}+{window.winfo_screenheight() // 2 - height // 2}')
            window.resizable(False, False)

            label = tkinter.Label(window, text='Install done, open file C:/lDev/executable.pyw')
            label.pack(fill='both', anchor='center', ipady=height // 2)

            window.mainloop()
            
            os.remove(__file__)